import ReactMarkdown from 'react-markdown'

export default function Md({ content }: { content: string }) {
  return (
    <div className="prose prose-sm max-w-none dark:prose-invert prose-headings:font-semibold prose-p:leading-relaxed">
      <ReactMarkdown
        components={{
          a({ href, children, ...props }) {
            if (href?.startsWith('#digest-')) {
              return (
                <a
                  href={href}
                  {...props}
                  className="mx-0.5 align-super text-[10px] leading-none no-underline rounded-full border border-stone-200 bg-stone-50 px-1 py-0 text-stone-500 hover:border-stone-400 hover:bg-stone-100 hover:text-stone-900"
                >
                  {children}
                </a>
              )
            }
            return <a href={href} {...props}>{children}</a>
          },
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  )
}
