import { stripPreamble } from './llm'

const VISION_ENDPOINT = import.meta.env.VITE_LLM_VISION_ENDPOINT as string
const VISION_MODEL = import.meta.env.VITE_LLM_VISION_MODEL as string
const API_KEY = import.meta.env.VITE_LLM_API_KEY as string

export type VisionResult = { text: string; pages: number }

async function toBase64(blob: Blob): Promise<string> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.onload = () => resolve((reader.result as string).split(',')[1])
    reader.onerror = reject
    reader.readAsDataURL(blob)
  })
}

export async function analyzeImage(
  imageBlob: Blob,
  prompt: string,
  mediaType = 'image/jpeg'
): Promise<string> {
  const b64 = await toBase64(imageBlob)
  const resp = await fetch(VISION_ENDPOINT, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${API_KEY}` },
    body: JSON.stringify({
      model: VISION_MODEL,
      max_tokens: 800,
      messages: [{
        role: 'user',
        content: [
          { type: 'image', source: { type: 'base64', media_type: mediaType, data: b64 } },
          { type: 'text', text: prompt },
        ],
      }],
    }),
  })
  if (!resp.ok) throw new Error(`Vision API ${resp.status}`)
  const data = await resp.json()
  return stripPreamble(data.content?.[0]?.text ?? '')
}

export async function analyzeMultipleImages(
  blobs: Blob[],
  prompt: string,
  mediaType = 'image/jpeg'
): Promise<string> {
  const content: unknown[] = []
  for (const blob of blobs) {
    const b64 = await toBase64(blob)
    content.push({ type: 'image', source: { type: 'base64', media_type: mediaType, data: b64 } })
  }
  content.push({ type: 'text', text: prompt })

  const resp = await fetch(VISION_ENDPOINT, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${API_KEY}` },
    body: JSON.stringify({ model: VISION_MODEL, max_tokens: 1000, messages: [{ role: 'user', content }] }),
  })
  if (!resp.ok) throw new Error(`Vision API ${resp.status}`)
  const data = await resp.json()
  return stripPreamble(data.content?.[0]?.text ?? '')
}

export const EXTERNAL_RESEARCH_PROMPT = `你是战略研究团队的分析助手。直接输出结构化内容，不要有任何开场白。

**核心信息**
- （关键数据/结论，2-3条）

**相关信号**
- （技术、产品、商业化或竞争变化，1-2条，不写行动建议）

中文，简洁，每条不超过2句话。如有图表请提炼数字结论。`
