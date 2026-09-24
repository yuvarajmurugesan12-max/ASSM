import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Scholarship Matching Agent",
  description:
    "Frontend for the Autonomous Scholarship–Student Matching Agent.",
};

import Link from "next/link";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col bg-slate-950 text-slate-100 font-sans">
        <header className="sticky top-0 z-50 backdrop-blur-md bg-slate-900/80 border-b border-slate-800">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <Link href="/" className="flex items-center gap-2 group">
              <div className="w-9 h-9 rounded-lg bg-indigo-600 flex items-center justify-center font-bold text-white shadow-lg shadow-indigo-500/20 group-hover:scale-105 transition-transform">
                🎓
              </div>
              <span className="font-bold text-lg bg-gradient-to-r from-white via-slate-200 to-indigo-300 bg-clip-text text-transparent">
                ScholarMatch AI
              </span>
            </Link>
            <nav className="flex items-center gap-6 text-sm font-medium">
              <Link
                href="/"
                className="text-slate-300 hover:text-white transition-colors"
              >
                Home
              </Link>
              <Link
                href="/opportunities"
                className="text-slate-300 hover:text-white transition-colors"
              >
                Opportunities
              </Link>
              <Link
                href="/profile"
                className="text-slate-300 hover:text-white transition-colors"
              >
                Student Profile
              </Link>
              <Link
                href="/opportunities"
                className="px-4 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-semibold transition-all shadow-md shadow-indigo-600/30"
              >
                Find Matches
              </Link>
            </nav>
          </div>
        </header>
        <main className="flex-1">{children}</main>
      </body>
    </html>
  );
}
