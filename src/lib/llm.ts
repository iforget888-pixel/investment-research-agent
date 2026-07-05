const ENDPOINT = import.meta.env.VITE_LLM_ENDPOINT as string
const API_KEY = import.meta.env.VITE_LLM_API_KEY as string
const MODEL = import.meta.env.VITE_LLM_MODEL as string

export function stripPreamble(text: string): string {
  const match = text.match(/(^#{1,3}\s|^\d+\.\s|\*\*)/m)
  if (match?.index && match.index > 10) {
    return text.slice(match.index).trim()
  }
  return text.trim()
}

export async function summarize(content: string, prompt: string): Promise<string> {
  const resp = await fetch(`${ENDPOINT}/chat/completions`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${API_KEY}`,
    },
    body: JSON.stringify({
      model: MODEL,
      stream: false,
      messages: [
        { role: 'system', content: prompt },
        { role: 'user', content },
      ],
      max_tokens: 800,
    }),
  })

  if (!resp.ok) throw new Error(`LLM API error: ${resp.status}`)
  const data = await resp.json()
  return stripPreamble(data.choices?.[0]?.message?.content ?? '')
}

export const REPORT_SUMMARY_PROMPT = `你是战略研究团队的行业分析助手。直接输出结构化内容，不要有任何开场白或对话性前缀。

对以下报告进行摘要，格式如下（严格按此输出）：

**核心观点**
- （1-2句，最多3条）

**关键数据**（如有，否则省略此节）
- （数字+结论，1-2条）

**技术/产品/商业化信号**
- （1-2条，只写观察到的变化或信号，不写行动建议）

中文，简洁，每条不超过2句话。`

export const INTEL_SUMMARY_PROMPT = `你是战略研究团队的竞品分析助手。直接输出结构化内容，不要有任何开场白。

对以下竞品情报进行分析：

**竞品动向**
- （核心变化，2-3条）

**后续观察点**
- （值得继续跟踪的问题，1-2条）

中文，简洁，每条不超过2句话。`
