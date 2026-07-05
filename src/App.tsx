import { ArrowRight, Database, FileText, Search, Sparkles } from 'lucide-react'

const focusItems = [
  ['PRD', 'Define workflows and boundaries', FileText],
  ['Architecture', 'Choose local Docker backend', Database],
  ['Research loop', 'Map evidence to theses', Search],
] as const

function App() {
  return (
    <main className="min-h-screen bg-[#F6F4EF] text-stone-950">
      <header className="border-b border-stone-200 bg-white">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-5">
          <div>
            <p className="text-xs uppercase tracking-[0.18em] text-stone-400">Personal Research OS</p>
            <h1 className="mt-1 text-xl font-semibold tracking-tight">Investment Research Agent</h1>
          </div>
          <div className="rounded-full border border-stone-200 bg-stone-50 px-3 py-1 text-xs text-stone-500">
            PRD first
          </div>
        </div>
      </header>

      <section className="mx-auto grid max-w-6xl gap-6 px-6 py-8 lg:grid-cols-[1.3fr_0.7fr]">
        <div className="rounded-lg border border-stone-200 bg-white p-6">
          <div className="flex items-center gap-2 text-sm font-medium text-stone-500">
            <Sparkles className="h-4 w-4" />
            Research direction
          </div>
          <h2 className="mt-4 max-w-3xl text-3xl font-semibold tracking-tight">
            Collect evidence, maintain theses, and turn scattered research into decision-grade memos.
          </h2>
          <p className="mt-4 max-w-2xl text-sm leading-6 text-stone-600">
            This repository starts as a clean product and architecture shell. The first milestone is the product definition,
            followed by backend selection and then the investment research data model.
          </p>
          <div className="mt-6 flex flex-wrap gap-2">
            {['Public information', 'Financial data', 'Interview notes', 'Investment memos'].map(item => (
              <span key={item} className="rounded-full border border-stone-200 bg-stone-50 px-3 py-1 text-xs text-stone-600">
                {item}
              </span>
            ))}
          </div>
        </div>

        <div className="rounded-lg border border-stone-200 bg-white p-5">
          <div className="text-sm font-semibold text-stone-900">Current focus</div>
          <div className="mt-4 space-y-3">
            {focusItems.map(([title, body, Icon]) => (
              <div key={title} className="flex gap-3 rounded-md border border-stone-100 bg-stone-50 p-3">
                <Icon className="mt-0.5 h-4 w-4 text-stone-500" />
                <div>
                  <div className="text-sm font-medium text-stone-900">{title}</div>
                  <div className="text-xs text-stone-500">{body}</div>
                </div>
              </div>
            ))}
          </div>
          <div className="mt-5 inline-flex items-center gap-2 text-sm font-medium text-stone-700">
            Product docs in <span className="font-mono text-xs">docs/</span> <ArrowRight className="h-4 w-4" />
          </div>
        </div>
      </section>
    </main>
  )
}

export default App
