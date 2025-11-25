import { useState } from 'react'

const ARTIFACT_TYPES = [
  { value: 'srs', label: 'Software Requirements Spec (SRS)' },
  { value: 'user_stories', label: 'User Stories' },
  { value: 'boilerplate', label: 'Boilerplate Code Structure' },
]

export default function RequirementForm({ onGenerate, loading }) {
  const [description, setDescription] = useState('')
  const [artifactType, setArtifactType] = useState('srs')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!description.trim()) return
    onGenerate({ description, artifactType })
  }

  return (
    <form onSubmit={handleSubmit} className="form">
      <textarea
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="Describe your product idea..."
        rows={5}
        required
      />
      <div className="form-row">
        <select value={artifactType} onChange={(e) => setArtifactType(e.target.value)}>
          {ARTIFACT_TYPES.map((t) => (
            <option key={t.value} value={t.value}>{t.label}</option>
          ))}
        </select>
        <button type="submit" disabled={loading}>
          {loading ? 'Generating...' : 'Generate'}
        </button>
      </div>
    </form>
  )
}
