"use client";

import { useState } from "react";

export default function ProfilePage() {
  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    age: "",
    location: "",
    college: "",
    course: "",
    branch: "",
    year: "",
    semester: "",
    percentage: "",
    cgpa: "",
    preferred_opportunity_type: "",
  });

  const [message, setMessage] = useState<{ type: "success" | "error"; text: string } | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setMessage(null);

    try {
      // Basic type conversion
      const payload = {
        ...formData,
        age: formData.age ? parseInt(formData.age) : null,
        year: formData.year ? parseInt(formData.year) : null,
        semester: formData.semester ? parseInt(formData.semester) : null,
        percentage: formData.percentage ? parseFloat(formData.percentage) : null,
        cgpa: formData.cgpa ? parseFloat(formData.cgpa) : null,
      };

      const response = await fetch("http://localhost:8000/students", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Failed to save profile");
      }

      setMessage({ type: "success", text: "Profile saved successfully!" });
    } catch (err: any) {
      setMessage({ type: "error", text: err.message || "An error occurred" });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-3xl mx-auto bg-white rounded-xl shadow-md overflow-hidden">
        <div className="px-8 py-6 border-b border-gray-200">
          <h2 className="text-2xl font-bold text-gray-900">Student Profile</h2>
          <p className="mt-1 text-sm text-gray-500">
            Please fill in your details to create your profile.
          </p>
        </div>
        
        <form onSubmit={handleSubmit} className="px-8 py-6 space-y-6">
          {message && (
            <div
              className={`p-4 rounded-md ${
                message.type === "success" ? "bg-green-50 text-green-800" : "bg-red-50 text-red-800"
              }`}
            >
              {message.text}
            </div>
          )}

          <div className="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-2">
            <div>
              <label className="block text-sm font-medium text-gray-700">Full Name</label>
              <input
                type="text"
                name="full_name"
                required
                value={formData.full_name}
                onChange={handleChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border text-gray-900"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Email Address</label>
              <input
                type="email"
                name="email"
                required
                value={formData.email}
                onChange={handleChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border text-gray-900"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Age</label>
              <input
                type="number"
                name="age"
                value={formData.age}
                onChange={handleChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border text-gray-900"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Location</label>
              <input
                type="text"
                name="location"
                value={formData.location}
                onChange={handleChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border text-gray-900"
              />
            </div>

            <div className="sm:col-span-2">
              <label className="block text-sm font-medium text-gray-700">College / University</label>
              <input
                type="text"
                name="college"
                value={formData.college}
                onChange={handleChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border text-gray-900"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Course / Degree</label>
              <input
                type="text"
                name="course"
                value={formData.course}
                onChange={handleChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border text-gray-900"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Branch / Major</label>
              <input
                type="text"
                name="branch"
                value={formData.branch}
                onChange={handleChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border text-gray-900"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Year of Study</label>
              <input
                type="number"
                name="year"
                value={formData.year}
                onChange={handleChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border text-gray-900"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Semester</label>
              <input
                type="number"
                name="semester"
                value={formData.semester}
                onChange={handleChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border text-gray-900"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Percentage</label>
              <input
                type="number"
                step="0.01"
                name="percentage"
                value={formData.percentage}
                onChange={handleChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border text-gray-900"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">CGPA</label>
              <input
                type="number"
                step="0.01"
                name="cgpa"
                value={formData.cgpa}
                onChange={handleChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border text-gray-900"
              />
            </div>

            <div className="sm:col-span-2">
              <label className="block text-sm font-medium text-gray-700">Preferred Opportunity Type</label>
              <select
                name="preferred_opportunity_type"
                value={formData.preferred_opportunity_type}
                onChange={handleChange}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border text-gray-900 bg-white"
              >
                <option value="">Select an option</option>
                <option value="Scholarship">Scholarship</option>
                <option value="Internship">Internship</option>
                <option value="Job">Job</option>
                <option value="Fellowship">Fellowship</option>
              </select>
            </div>
          </div>

          <div className="pt-4 border-t border-gray-200">
            <button
              type="submit"
              disabled={isLoading}
              className={`w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 ${
                isLoading ? "opacity-75 cursor-not-allowed" : ""
              }`}
            >
              {isLoading ? "Saving..." : "Save Profile"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
