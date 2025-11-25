export default function RequirementOutput({ data }) {
  const handleCopy = () => {
    const text = data.requirements.map(r => `[${r.type}] ${r.description}`).join('\n')
    navigator.clipboard.writeText(text)
  }

  return (
    <div className="output">
      <div className="output-header">
        <h2>{data.title}</h2>
        <button onClick={handleCopy} className="copy-btn">Copy All</button>
      </div>
      <p className="summary">{data.summary}</p>
      <ul className="requirements-list">
        {data.requirements.map((req) => (
          <li key={req.id} className={`req-item ${req.type.toLowerCase()}`}>
            <span className="req-type">{req.type}</span>
            <span className="req-desc">{req.description}</span>
          </li>
        ))}
      </ul>
    </div>
  )
}
