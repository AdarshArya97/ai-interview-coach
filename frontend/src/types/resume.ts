
export interface ResumeAnalysisResult {
  job_role: string;
  resume_skills: string[];
  matched_skills: string[];
  missing_skills: string[];
  match_score: number;
  strengths: string[];
  improvement_suggestions: string[];
  likely_interview_questions: string[];
}
