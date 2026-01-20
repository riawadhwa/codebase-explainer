export default function LoadingState() {
  return (
    <div className="mt-10 max-w-5xl mx-auto">
      <div className="bg-[#0f172a] border border-slate-800 rounded-2xl p-6">
        <div className="flex items-center gap-3 mb-4">
          <div className="w-3 h-3 rounded-full bg-indigo-500 animate-pulse" />
          <p className="text-slate-300 font-medium">Analyzing repository</p>
        </div>

        <ul className="space-y-2 text-sm text-slate-400 font-mono">
          <li>→ Cloning repository</li>
          <li>→ Scanning file structure</li>
          <li>→ Detecting architecture</li>
          <li>→ Inferring execution flow</li>
        </ul>
      </div>
    </div>
  );
}
