export default function ExecutionFlowTab({ data }) {
  return (
    <div className="space-y-6">
      <p className="text-slate-300 leading-relaxed">{data.summary}</p>

      <ol className="space-y-4">
        {data.steps.map((step, i) => (
          <li key={i} className="flex gap-4">
            <div className="text-indigo-400 font-mono">{i + 1}</div>
            <div className="bg-[#020617] border border-slate-800 rounded-lg p-4 flex-1">
              {step}
            </div>
          </li>
        ))}
      </ol>

      {data.notes.length > 0 && (
        <div>
          <p className="text-sm text-slate-400 mb-2">Notes</p>
          <ul className="list-disc list-inside text-slate-400">
            {data.notes.map((note, i) => (
              <li key={i}>{note}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
