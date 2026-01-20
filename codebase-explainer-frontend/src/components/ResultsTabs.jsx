import { useState } from "react";
import OverviewTab from "./tabs/OverviewTab";
import ArchitectureTab from "./tabs/ArchitectureTab";
import ExecutionFlowTab from "./tabs/ExecutionFlowTab";

const TABS = [
  { id: "overview", label: "Overview" },
  { id: "architecture", label: "Architecture" },
  { id: "flow", label: "Execution Flow" },
];

export default function ResultsTabs({ data }) {
  const [active, setActive] = useState("overview");

  return (
    <div className="mt-10">
      {/* Tab bar */}
      <div className="flex gap-2 bg-[#0f172a] border border-slate-800 rounded-xl p-3 w-fit mx-auto">
        {TABS.map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActive(tab.id)}
            className={`px-7 py-3.5 text-base rounded-2xl font-semibold transition-all duration-200
  ${
    active === tab.id
      ? "bg-indigo-600 text-white shadow-lg"
      : "text-slate-400 hover:text-slate-200 hover:bg-slate-800"
  }`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Content */}
      <div className="mt-6 bg-[#0f172a] border border-slate-800 rounded-2xl p-8 max-w-5xl mx-auto">
        {active === "overview" && <OverviewTab data={data.repo_summary} />}

        {active === "architecture" && (
          <ArchitectureTab data={data.architecture} />
        )}

        {active === "flow" && <ExecutionFlowTab data={data.execution_flow} />}
      </div>
    </div>
  );
}
