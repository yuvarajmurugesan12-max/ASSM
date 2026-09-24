"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

interface Opportunity {
  id: number;
  title: string;
  provider: string;
  opportunity_type: string;
  location: string | null;
  deadline: string | null;
  status: string;
}

export default function OpportunitiesPage() {
  const [opportunities, setOpportunities] = useState<Opportunity[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");
  const [typeFilter, setTypeFilter] = useState("");
  const [locationFilter, setLocationFilter] = useState("");
  const [sortOrder, setSortOrder] = useState<"asc" | "desc" | "">("");

  useEffect(() => {
    fetch("http://localhost:8000/opportunities")
      .then((res) => res.json())
      .then((data) => {
        setOpportunities(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching opportunities:", err);
        setLoading(false);
      });
  }, []);

  const filteredOpportunities = opportunities
    .filter((opp) => {
      const matchesSearch =
        opp.title.toLowerCase().includes(search.toLowerCase()) ||
        opp.provider.toLowerCase().includes(search.toLowerCase());
      const matchesType = typeFilter ? opp.opportunity_type === typeFilter : true;
      const matchesLocation = locationFilter
        ? opp.location?.toLowerCase().includes(locationFilter.toLowerCase())
        : true;
      return matchesSearch && matchesType && matchesLocation;
    })
    .sort((a, b) => {
      if (!sortOrder) return 0;
      const dateA = a.deadline ? new Date(a.deadline).getTime() : Infinity;
      const dateB = b.deadline ? new Date(b.deadline).getTime() : Infinity;
      return sortOrder === "asc" ? dateA - dateB : dateB - dateA;
    });

  if (loading) {
    return <div className="p-8 text-center">Loading opportunities...</div>;
  }

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8 text-gray-900">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-3xl font-extrabold text-gray-900 mb-8">
          Browse Opportunities (Demo Data)
        </h1>

        <div className="bg-white p-6 rounded-lg shadow-sm mb-8 flex flex-col sm:flex-row gap-4 border border-gray-200">
          <input
            type="text"
            placeholder="Search title or provider..."
            className="flex-1 p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
          <select
            className="p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500 bg-white"
            value={typeFilter}
            onChange={(e) => setTypeFilter(e.target.value)}
          >
            <option value="">All Types</option>
            <option value="scholarship">Scholarship</option>
            <option value="internship">Internship</option>
            <option value="fellowship">Fellowship</option>
          </select>
          <input
            type="text"
            placeholder="Filter by location..."
            className="p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
            value={locationFilter}
            onChange={(e) => setLocationFilter(e.target.value)}
          />
          <select
            className="p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500 bg-white"
            value={sortOrder}
            onChange={(e) => setSortOrder(e.target.value as any)}
          >
            <option value="">Sort by Deadline</option>
            <option value="asc">Deadline: Soonest</option>
            <option value="desc">Deadline: Latest</option>
          </select>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {filteredOpportunities.map((opp) => (
            <div
              key={opp.id}
              className="bg-white overflow-hidden shadow rounded-lg border border-gray-200 flex flex-col"
            >
              <div className="px-6 py-5 flex-1">
                <div className="flex items-center justify-between mb-2">
                  <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-indigo-100 text-indigo-800 capitalize">
                    {opp.opportunity_type}
                  </span>
                  <span
                    className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${
                      opp.status === "open"
                        ? "bg-green-100 text-green-800"
                        : "bg-red-100 text-red-800"
                    } capitalize`}
                  >
                    {opp.status}
                  </span>
                </div>
                <h3 className="text-xl font-bold text-gray-900 mb-2 truncate" title={opp.title}>
                  {opp.title}
                </h3>
                <p className="text-sm font-medium text-gray-600 mb-4">{opp.provider}</p>
                
                <dl className="grid grid-cols-1 gap-x-4 gap-y-4 sm:grid-cols-2">
                  <div className="sm:col-span-1">
                    <dt className="text-xs font-medium text-gray-500 uppercase">Location</dt>
                    <dd className="mt-1 text-sm text-gray-900">{opp.location || "N/A"}</dd>
                  </div>
                  <div className="sm:col-span-1">
                    <dt className="text-xs font-medium text-gray-500 uppercase">Deadline</dt>
                    <dd className="mt-1 text-sm text-gray-900">
                      {opp.deadline ? new Date(opp.deadline).toLocaleDateString() : "No deadline"}
                    </dd>
                  </div>
                </dl>
              </div>
              <div className="bg-gray-50 px-6 py-4 border-t border-gray-200">
                <Link
                  href={`/opportunities/${opp.id}`}
                  className="w-full inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
                >
                  View Details
                </Link>
              </div>
            </div>
          ))}
          {filteredOpportunities.length === 0 && (
            <div className="col-span-full text-center py-12 text-gray-500">
              No opportunities found matching your filters.
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
