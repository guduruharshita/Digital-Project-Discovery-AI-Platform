import type { GenerateRequest, GenerateResponse, ArtifactType } from "../types";

const BASE_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

export async function generateArtifacts(request: GenerateRequest): Promise<GenerateResponse> {
  const res = await fetch(`${BASE_URL}/api/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(request),
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: "Unknown error" }));
    throw new Error((err as { detail: string }).detail ?? `HTTP ${res.status}`);
  }

  return res.json() as Promise<GenerateResponse>;
}

export async function fetchArtifactTypes(): Promise<ArtifactType[]> {
  const res = await fetch(`${BASE_URL}/api/artifact-types`);
  if (!res.ok) throw new Error("Failed to fetch artifact types");
  const data = (await res.json()) as { types: ArtifactType[] };
  return data.types;
}
