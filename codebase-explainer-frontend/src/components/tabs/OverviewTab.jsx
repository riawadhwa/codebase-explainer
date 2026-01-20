function Info({ label, value }) {
  return (
    <div className="bg-[#020617] border border-slate-800 rounded-xl p-4">
      <p className="text-xs uppercase tracking-wide text-slate-500 mb-1">
        {label}
      </p>
      <p className="text-slate-100 font-medium">{value}</p>
    </div>
  );
}

export default function OverviewTab({ data }) {
  return (
    <div className="grid grid-cols-2 gap-6">
      <Info label="Project Type" value={data.project_type} />
      <Info label="Primary Language" value={data.primary_language} />
      <Info label="Frameworks" value={data.frameworks.join(", ") || "None"} />
      <Info label="Entry Points" value={data.entry_points.join(", ")} />
    </div>
  );
}
