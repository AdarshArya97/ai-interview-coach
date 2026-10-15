
import { apiRequest } from "./api";
import type { ResumeAnalysisResult } from "../types/resume";

export async function analyzeResume(
  file: File,
  jobRole: string,
  jobDescription?: string,
): Promise<ResumeAnalysisResult> {
  const formData = new FormData();

  formData.append("file", file);
  formData.append("job_role", jobRole);

  if (jobDescription?.trim()) {
    formData.append("job_description", jobDescription.trim());
  }

  return apiRequest<ResumeAnalysisResult>("/resume/analyze", {
    method: "POST",
    body: formData,
  });
}
