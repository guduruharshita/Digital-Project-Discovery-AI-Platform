export default function RequirementOutput({ data }) {
  const handleCopy = () => {
    const text = data.requirements.map(r => `[${r.type}] ${r.description}`).join('\n')
    navigator.clipboard.writeText(text)
  }
  return (
    <div className="output">
      <div className="output-header">
        <h2>{data.title}</h2>
        <button onClick={handleCopy}>Copy All</button>
      </div>
      <p className="summary">{data.summary}</p>
      <ul>
        {data.requirements.map(r => (
          <li key={r.id}>
            <span className="req-type">{r.type}</span>
            <span>{r.description}</span>
          </li>
        ))}
      </ul>
    </div>
  )
}
