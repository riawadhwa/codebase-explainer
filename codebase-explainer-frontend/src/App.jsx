import { useState } from "react";
import RepoInput from "./components/RepoInput";
import LoadingState from "./components/LoadingState";
import ErrorCard from "./components/ErrorCard";
import ResultsTabs from "./components/ResultsTabs";

const API_URL = "/analyze"; // update after deploy

export default function App() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  const analyzeRepo = async (repoUrl) => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const res = await fetch(`${API_URL}/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          source_type: "github",
          repo_url: repoUrl,
          max_files: 200,
        }),
      });

      if (!res.ok) {
        const err = await res.json();
        throw new Error(err.detail || "Analysis failed");
      }

      const data = await res.json();
      setResult(data);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#0b0f14] text-slate-200">
      <div className="max-w-6xl mx-auto px-6 py-12">
        {/* Hero */}
        <header className="mt-20 mb-16 max-w-3xl">
          <h1 className="text-7xl font-semibold tracking-tight text-slate-100 mb-3">
            RepoLens
          </h1>

          <p className="text-lg text-slate-400 max-w-2xl leading-relaxed">
            Dropped into a new codebase?
            <br />
            RepoLens explains what it does, how it works, and how to run it.
          </p>
        </header>

        {/* Input */}
        <RepoInput onAnalyze={analyzeRepo} loading={loading} />

        {/* States */}
        {loading && <LoadingState />}
        {error && <ErrorCard message={error} />}
        {result && <ResultsTabs data={result} />}
      </div>
    </div>
  );
}
