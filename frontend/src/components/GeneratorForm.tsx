import { useState, type FormEvent } from "react";
import type { ArtifactType } from "../types";

const ARTIFACT_LABELS: Record<ArtifactType, string> = {
  srs: "SRS Document",
  user_stories: "User Stories",
  boilerplate: "Code Boilerplate",
};

interface Props {
  onSubmit: (description: string, artifactType: ArtifactType) => void;
  loading: boolean;
}

export default function GeneratorForm({ onSubmit, loading }: Props) {
  const [description, setDescription] = useState("");
  const [artifactType, setArtifactType] = useState<ArtifactType>("srs");

  function handleSubmit(e: FormEvent) {
    e.preventDefault();
    if (description.trim().length >= 10) onSubmit(description.trim(), artifactType);
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Product Description
        </label>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Describe your product or system in plain English..."
          rows={6}
          minLength={10}
          maxLength={2000}
          required
          className="w-full px-4 py-3 border border-gray-300 rounded-xl resize-none focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm transition"
        />
        <p className="text-xs text-gray-400 mt-1 text-right">{description.length} / 2000</p>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">Artifact Type</label>
        <div className="flex flex-wrap gap-2">
          {(Object.keys(ARTIFACT_LABELS) as ArtifactType[]).map((type) => (
            <button
              key={type}
              type="button"
              onClick={() => setArtifactType(type)}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                artifactType === type
                  ? "bg-indigo-600 text-white shadow-sm"
                  : "bg-gray-100 text-gray-600 hover:bg-gray-200"
              }`}
            >
              {ARTIFACT_LABELS[type]}
            </button>
          ))}
        </div>
      </div>

      <button
        type="submit"
        disabled={loading || description.trim().length < 10}
        className="w-full py-3 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
      >
        {loading ? "Generating…" : "Generate Artifacts"}
      </button>
    </form>
  );
}
