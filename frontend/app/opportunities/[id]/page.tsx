"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import Link from "next/link";

interface Requirement {
  id: number;
  requirement_type: string;
  requirement_value: string;
  operator: string;
  description: string | null;
}

interface Document {
  id: number;
  document_name: string;
  document_type: string | null;
  mandatory: boolean;
  description: string | null;
}

interface OpportunityDetails {
  id: number;
  title: string;
  provider: string;
  opportunity_type: string;
  description: string | null;
  application_url: string | null;
  source_url: string | null;
  location: string | null;
  deadline: string | null;
  status: string;
  requirements: Requirement[];
  documents: Document[];
}

export default function OpportunityDetailsPage() {
  const { id } = useParams();
  const router = useRouter();
  const [opportunity, setOpportunity] = useState<OpportunityDetails | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!id) return;
    
    fetch(`http://localhost:8000/opportunities/${id}`)
      .then((res) => {
        if (!res.ok) throw new Error("Opportunity not found");
        return res.json();
      })
      .then((data) => {
        setOpportunity(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, [id]);

  if (loading) {
    return <div className="p-8 text-center text-gray-900">Loading opportunity details...</div>;
  }

  if (error || !opportunity) {
    return (
      <div className="p-8 text-center text-gray-900">
        <h2 className="text-xl font-bold text-red-600 mb-4">{error || "Opportunity not found"}</h2>
        <button onClick={() => router.back()} className="text-indigo-600 hover:underline">
          &larr; Go Back
        </button>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8 text-gray-900">
      <div className="max-w-4xl mx-auto">
        <Link href="/opportunities" className="text-indigo-600 hover:underline mb-6 inline-block font-medium">
          &larr; Back to Opportunities
        </Link>
        
        <div className="bg-white shadow overflow-hidden sm:rounded-lg border border-gray-200">
          <div className="px-4 py-5 sm:px-6 flex justify-between items-start">
            <div>
              <h3 className="text-2xl leading-6 font-bold text-gray-900 mb-2">{opportunity.title}</h3>
              <p className="mt-1 max-w-2xl text-sm text-gray-500 font-medium">
                Provided by {opportunity.provider}
              </p>
            </div>
            <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-indigo-100 text-indigo-800 capitalize">
              {opportunity.opportunity_type}
            </span>
          </div>
          
          <div className="border-t border-gray-200 px-4 py-5 sm:px-6">
            <dl className="grid grid-cols-1 gap-x-4 gap-y-8 sm:grid-cols-2">
              <div className="sm:col-span-1">
                <dt className="text-sm font-medium text-gray-500 uppercase">Location</dt>
                <dd className="mt-1 text-sm text-gray-900">{opportunity.location || "N/A"}</dd>
              </div>
              
              <div className="sm:col-span-1">
                <dt className="text-sm font-medium text-gray-500 uppercase">Deadline</dt>
                <dd className="mt-1 text-sm text-gray-900">
                  {opportunity.deadline ? new Date(opportunity.deadline).toLocaleDateString() : "No deadline"}
                </dd>
              </div>
              
              <div className="sm:col-span-1">
                <dt className="text-sm font-medium text-gray-500 uppercase">Status</dt>
                <dd className={`mt-1 text-sm font-bold capitalize ${opportunity.status === 'open' ? 'text-green-600' : 'text-red-600'}`}>
                  {opportunity.status}
                </dd>
              </div>
              
              <div className="sm:col-span-1">
                <dt className="text-sm font-medium text-gray-500 uppercase">Application Link</dt>
                <dd className="mt-1 text-sm text-gray-900">
                  {opportunity.application_url ? (
                    <a href={opportunity.application_url} target="_blank" rel="noreferrer" className="text-indigo-600 hover:underline break-all">
                      {opportunity.application_url}
                    </a>
                  ) : (
                    "Not provided"
                  )}
                </dd>
              </div>

              <div className="sm:col-span-2">
                <dt className="text-sm font-medium text-gray-500 uppercase">Description</dt>
                <dd className="mt-1 text-sm text-gray-900 whitespace-pre-wrap">
                  {opportunity.description || "No description provided."}
                </dd>
              </div>
            </dl>
          </div>
          
          <div className="border-t border-gray-200 px-4 py-5 sm:px-6 bg-gray-50">
            <h4 className="text-lg font-bold text-gray-900 mb-4">Eligibility Requirements</h4>
            {opportunity.requirements.length > 0 ? (
              <ul className="divide-y divide-gray-200 border border-gray-200 rounded-md bg-white">
                {opportunity.requirements.map((req) => (
                  <li key={req.id} className="p-4 flex items-start">
                    <div className="min-w-0 flex-1">
                      <p className="text-sm font-medium text-gray-900 capitalize">
                        {req.requirement_type} {req.operator} {req.requirement_value}
                      </p>
                      {req.description && <p className="text-sm text-gray-500 mt-1">{req.description}</p>}
                    </div>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-sm text-gray-500">No specific eligibility requirements listed.</p>
            )}
          </div>
          
          <div className="border-t border-gray-200 px-4 py-5 sm:px-6 bg-gray-50">
            <h4 className="text-lg font-bold text-gray-900 mb-4">Required Documents</h4>
            {opportunity.documents.length > 0 ? (
              <ul className="divide-y divide-gray-200 border border-gray-200 rounded-md bg-white">
                {opportunity.documents.map((doc) => (
                  <li key={doc.id} className="p-4 flex items-start justify-between">
                    <div className="min-w-0 flex-1">
                      <p className="text-sm font-medium text-gray-900">
                        {doc.document_name}
                        {doc.mandatory && <span className="ml-2 text-xs font-bold text-red-600">(Mandatory)</span>}
                      </p>
                      <p className="text-sm text-gray-500 mt-1">
                        Type: {doc.document_type || "Any"}
                        {doc.description ? ` - ${doc.description}` : ""}
                      </p>
                    </div>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-sm text-gray-500">No specific documents required.</p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
