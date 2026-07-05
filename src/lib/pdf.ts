import * as pdfjsLib from 'pdfjs-dist'

pdfjsLib.GlobalWorkerOptions.workerSrc = new URL(
  'pdfjs-dist/build/pdf.worker.mjs',
  import.meta.url
).toString()

export type ExtractResult = {
  method: 'text' | 'vision-pages'
  text?: string
  pageBlobs?: Blob[]
  pageCount: number
}

export async function extractPdf(file: File, maxPages = 6): Promise<ExtractResult> {
  const arrayBuffer = await file.arrayBuffer()
  const pdf = await pdfjsLib.getDocument({ data: arrayBuffer }).promise
  const pageCount = Math.min(pdf.numPages, maxPages)

  // 先尝试提取文字
  let allText = ''
  for (let i = 1; i <= pageCount; i++) {
    const page = await pdf.getPage(i)
    const content = await page.getTextContent()
    const pageText = content.items.map((item: unknown) => (item as { str: string }).str).join(' ')
    allText += pageText + '\n'
  }

  const cleanText = allText.replace(/\s+/g, ' ').trim()

  // 文字超过200字认为是文字型PDF
  if (cleanText.length > 200) {
    return { method: 'text', text: cleanText.slice(0, 12000), pageCount }
  }

  // 扫描型 PDF：每页渲染为图片
  const pageBlobs: Blob[] = []
  for (let i = 1; i <= pageCount; i++) {
    const page = await pdf.getPage(i)
    const viewport = page.getViewport({ scale: 1.5 })
    const canvas = document.createElement('canvas')
    canvas.width = viewport.width
    canvas.height = viewport.height
    const ctx = canvas.getContext('2d')!
    await page.render({ canvasContext: ctx, viewport }).promise
    const blob = await new Promise<Blob>(resolve =>
      canvas.toBlob(b => resolve(b!), 'image/jpeg', 0.85)
    )
    pageBlobs.push(blob)
  }

  return { method: 'vision-pages', pageBlobs, pageCount }
}

export async function fileToBlob(file: File): Promise<Blob> {
  return new Blob([await file.arrayBuffer()], { type: file.type })
}
