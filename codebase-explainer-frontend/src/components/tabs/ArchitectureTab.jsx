export default function ArchitectureTab({ data }) {
  return (
    <div className="space-y-8">
      {/* Overview */}
      <p className="text-slate-300 leading-relaxed">{data.overview}</p>

      {/* Run Commands — PROMOTED */}
      {data.run_commands.length > 0 && (
        <div className="bg-[#020617] border border-slate-800 rounded-xl p-5">
          <p className="text-xs uppercase tracking-wide text-slate-500 mb-3">
            Run Commands
          </p>

          <div className="space-y-2">
            {data.run_commands.map((cmd) => (
              <div
                key={cmd}
                className="font-mono text-sm bg-[#0b0f14] border border-slate-700 rounded-lg px-4 py-2 text-indigo-400"
              >
                {cmd}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Components */}
      <div className="space-y-3">
        <p className="text-xs uppercase tracking-wide text-slate-500">
          Components
        </p>

        {Object.entries(data.components).map(([key, value]) => (
          <div
            key={key}
            className="bg-[#020617] border border-slate-800 rounded-lg p-4"
          >
            <p className="font-mono text-indigo-400">{key}</p>
            <p className="text-slate-400 mt-1">{value}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
