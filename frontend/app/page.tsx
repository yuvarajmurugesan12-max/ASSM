import Link from "next/link";

export default function Home() {
  return (
    <div className="relative overflow-hidden min-h-[calc(100vh-4rem)]">
      {/* Background glow effects */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-indigo-600/20 blur-[140px] rounded-full pointer-events-none" />
      <div className="absolute bottom-10 right-10 w-[400px] h-[400px] bg-purple-600/15 blur-[120px] rounded-full pointer-events-none" />

      {/* Hero Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 pb-16 text-center relative z-10">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-950/80 border border-indigo-700/50 text-indigo-300 text-xs font-semibold mb-6">
          <span className="flex h-2 w-2 rounded-full bg-emerald-400 animate-pulse" />
          Autonomous Multi-Agent Matching Engine
        </div>

        <h1 className="text-4xl sm:text-6xl font-extrabold tracking-tight text-white mb-6 leading-tight">
          Smart Matching for <br />
          <span className="bg-gradient-to-r from-indigo-400 via-purple-300 to-pink-400 bg-clip-text text-transparent">
            Scholarships & Internships
          </span>
        </h1>

        <p className="max-w-2xl mx-auto text-lg text-slate-300 mb-10 leading-relaxed">
          ScholarMatch AI leverages autonomous agents to automatically crawl, analyze, and match students with relevant scholarships, grants, and internships based on eligibility and profile skills.
        </p>

        <div className="flex flex-wrap items-center justify-center gap-4">
          <Link
            href="/opportunities"
            className="px-6 py-3.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold transition-all shadow-lg shadow-indigo-600/30 flex items-center gap-2"
          >
            <span>Explore Opportunities</span>
            <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
            </svg>
          </Link>

          <Link
            href="/profile"
            className="px-6 py-3.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-200 font-semibold transition-all"
          >
            Manage Student Profile
          </Link>
        </div>

        {/* Quick Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl mx-auto mt-16 text-left">
          <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800/80 backdrop-blur-sm hover:border-slate-700 transition-colors">
            <div className="text-3xl font-bold text-indigo-400 mb-1">10+</div>
            <div className="text-sm font-semibold text-white mb-2">Curated Opportunities</div>
            <p className="text-xs text-slate-400">Merit-based scholarships, financial aid, and tech fellowships ready for matching.</p>
          </div>

          <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800/80 backdrop-blur-sm hover:border-slate-700 transition-colors">
            <div className="text-3xl font-bold text-emerald-400 mb-1">AI Agents</div>
            <div className="text-sm font-semibold text-white mb-2">Automated Discovery</div>
            <p className="text-xs text-slate-400">LangGraph workflow parses criteria, requirements, and document requirements automatically.</p>
          </div>

          <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800/80 backdrop-blur-sm hover:border-slate-700 transition-colors">
            <div className="text-3xl font-bold text-purple-400 mb-1">Instant</div>
            <div className="text-sm font-semibold text-white mb-2">Eligibility Verification</div>
            <p className="text-xs text-slate-400">Instant check on CGPA, branch, location, and key skill requirements.</p>
          </div>
        </div>
      </section>
    </div>
  );
}
