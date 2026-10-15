
import { useState } from "react";
import { analyzeResume } from "../../services/resume.service";
import type { ResumeAnalysisResult } from "../../types/resume";

export function useResume() {
  const [result, setResult] = useState<ResumeAnalysisResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function submitResume(
    file: File,
    jobRole: string,
    jobDescription: string,
  ) {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const data = await analyzeResume(file, jobRole, jobDescription);
      setResult(data);
    } catch (err) {
      setError(
        err instanceof Error ? err.message : "Resume analysis failed.",
      );
    } finally {
      setLoading(false);
    }
  }

  return { result, loading, error, submitResume };
}
