import { useState } from "react";
import { generateArtifacts } from "../lib/api";
import type { ArtifactType, GenerateResponse } from "../types";

interface State {
  data: GenerateResponse | null;
  loading: boolean;
  error: string | null;
}

export function useGenerate() {
  const [state, setState] = useState<State>({ data: null, loading: false, error: null });

  async function generate(description: string, artifactType: ArtifactType) {
    setState({ data: null, loading: true, error: null });
    try {
      const result = await generateArtifacts({ description, artifact_type: artifactType });
      setState({ data: result, loading: false, error: null });
    } catch (err) {
      setState({ data: null, loading: false, error: (err as Error).message });
    }
  }

  return { ...state, generate };
}
