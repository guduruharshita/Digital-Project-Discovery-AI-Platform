export type ArtifactType = "srs" | "user_stories" | "boilerplate";

export interface Requirement {
  id: number;
  type: string;
  description: string;
}

export interface GenerateRequest {
  description: string;
  artifact_type: ArtifactType;
}

export interface GenerateResponse {
  title: string;
  summary: string;
  requirements: Requirement[];
  artifact_type: ArtifactType;
}
