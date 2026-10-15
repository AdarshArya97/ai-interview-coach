
import { useState, type FormEvent } from "react";
import { useResume } from "../features/resume/useResume";
import "./ResumeAnalysis.css";

export default function ResumeAnalysis() {
  const [file, setFile] = useState<File | null>(null);
  const [jobRole, setJobRole] = useState("Machine Learning Engineer");
  const [jobDescription, setJobDescription] = useState("");

  const { result, loading, error, submitResume } = useResume();

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (!file) return;
    await submitResume(file, jobRole, jobDescription);
  }

  return (
    <main className="resume-page">
      <header className="hero">
        <p className="eyebrow">AI INTERVIEW COACH</p>
        <h1>Resume Analyzer</h1>
        <p>
          Discover your strengths, identify skill gaps, and prepare for
          your next interview.
        </p>
      </header>

      <form className="resume-form" onSubmit={handleSubmit}>
        <label htmlFor="resume-file">Resume (PDF, max 10 MB)</label>
        <input
          id="resume-file"
          type="file"
          accept="application/pdf,.pdf"
          required
          onChange={(event) => {
            const selected = event.target.files?.[0] ?? null;
            setFile(
              selected &&
                selected.type === "application/pdf" &&
                selected.size <= 10 * 1024 * 1024
                ? selected
                : null,
            );
          }}
        />
        {file === null && (
          <p className="hint">Choose a PDF file smaller than 10 MB.</p>
        )}

        <label htmlFor="job-role">Target job role</label>
        <input
          id="job-role"
          value={jobRole}
          onChange={(event) => setJobRole(event.target.value)}
          minLength={2}
          maxLength={150}
          required
        />

        <label htmlFor="job-description">
          Job description (optional)
        </label>
        <textarea
          id="job-description"
          value={jobDescription}
          onChange={(event) => setJobDescription(event.target.value)}
          maxLength={15000}
          rows={5}
          placeholder="Paste the job description or required skills..."
        />

        {error && <p className="error-message">{error}</p>}

        <button type="submit" disabled={!file || !jobRole.trim() || loading}>
          {loading ? "Analyzing resume..." : "Analyze Resume"}
        </button>
      </form>

      {loading && (
        <p className="loading-message">
          Analyzing your resume with AI. This may take a little while...
        </p>
      )}

      {result && (
        <section className="results">
          <h2>Your analysis</h2>

          <div className="score-card">
            <p>Resume match score</p>
            <strong>{result.match_score.toFixed(2)}%</strong>
          </div>

          <div className="result-grid">
            <ResultList title="Skills found" items={result.resume_skills} />
            <ResultList title="Matched skills" items={result.matched_skills} />
            <ResultList title="Missing skills" items={result.missing_skills} />
            <ResultList title="Strengths" items={result.strengths} />
            <ResultList
              title="Improvement suggestions"
              items={result.improvement_suggestions}
            />
            <ResultList
              title="Likely interview questions"
              items={result.likely_interview_questions}
            />
          </div>
        </section>
      )}
    </main>
  );
}

function ResultList({
  title,
  items,
}: {
  title: string;
  items: string[];
}) {
  return (
    <article className="result-card">
      <h3>{title}</h3>
      {items.length ? (
        <ul>
          {items.map((item, index) => (
            <li key={`${item}-${index}`}>{item}</li>
          ))}
        </ul>
      ) : (
        <p>None identified.</p>
      )}
    </article>
  );
}
