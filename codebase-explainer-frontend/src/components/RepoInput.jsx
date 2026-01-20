import { useState } from "react";

export default function RepoInput({ onAnalyze, loading }) {
  const [repoUrl, setRepoUrl] = useState("");

  return (
    <div className="bg-[#111827] border border-slate-800 rounded-2xl p-6 mb-10 shadow-lg">
      <label className="block text-sm font-medium text-slate-300 mb-3">
        GitHub Repository
      </label>

      <div className="flex gap-3">
        <input
          className="flex-1 bg-[#0b0f14] border border-slate-700 rounded-lg px-4 py-3 text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          placeholder="https://github.com/username/repo"
          value={repoUrl}
          onChange={(e) => setRepoUrl(e.target.value)}
        />

        <button
          onClick={() => onAnalyze(repoUrl)}
          disabled={!repoUrl || loading}
          className="px-6 py-3 rounded-lg bg-indigo-600 hover:bg-indigo-500 
             text-white font-medium disabled:opacity-50
             transition-all duration-200"
        >
          {loading ? "Analyzing…" : "Analyze"}
        </button>
      </div>

      <p className="text-xs text-slate-500 mt-3">
        Public repositories only. Analysis is read-only.
      </p>
    </div>
  );
}
