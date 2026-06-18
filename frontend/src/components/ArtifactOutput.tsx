import type { GenerateResponse } from "../types";

const BADGE_COLORS: Record<string, string> = {
  FR: "bg-blue-100 text-blue-700",
  NFR: "bg-purple-100 text-purple-700",
  Story: "bg-green-100 text-green-700",
  Module: "bg-amber-100 text-amber-700",
};

interface Props {
  data: GenerateResponse;
}

export default function ArtifactOutput({ data }: Props) {
  function copyAll() {
    const text = [
      data.title,
      data.summary,
      "",
      ...data.requirements.map((r) => `[${r.type}-${r.id}] ${r.description}`),
    ].join("\n");
    void navigator.clipboard.writeText(text);
  }

  return (
    <div className="space-y-4">
      <div className="flex items-start justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-gray-900">{data.title}</h2>
          <p className="text-sm text-gray-500 mt-1">{data.summary}</p>
        </div>
        <button
          onClick={copyAll}
          className="shrink-0 px-3 py-1.5 text-xs font-medium bg-gray-100 hover:bg-gray-200 rounded-lg transition-colors"
        >
          Copy All
        </button>
      </div>

      <ul className="space-y-2">
        {data.requirements.map((req) => (
          <li
            key={req.id}
            className="flex items-start gap-3 p-3 bg-gray-50 rounded-lg border border-gray-100"
          >
            <span
              className={`shrink-0 mt-0.5 px-2 py-0.5 text-xs font-semibold rounded ${
                BADGE_COLORS[req.type] ?? "bg-gray-200 text-gray-700"
              }`}
            >
              {req.type}-{req.id}
            </span>
            <p className="text-sm text-gray-700 leading-relaxed">{req.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
