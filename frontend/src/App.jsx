import { useState } from 'react'
import RequirementForm from './components/RequirementForm'
import RequirementOutput from './components/RequirementOutput'
import './App.css'

export default function App() {
  const [output, setOutput] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleGenerate = async ({ description, artifactType }) => {
    setLoading(true)
    setError(null)
    try {
      const res = await fetch('http://localhost:8000/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ description, artifact_type: artifactType }),
      })
      if (!res.ok) throw new Error(`Server error: ${res.status}`)
      setOutput(await res.json())
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <header>
        <h1>DiscoveryAI</h1>
        <p>Transform your product idea into structured software artifacts</p>
      </header>
      <main>
        <RequirementForm onGenerate={handleGenerate} loading={loading} />
        {error && <div className="error">{error}</div>}
        {output && <RequirementOutput data={output} />}
      </main>
    </div>
  )
}
