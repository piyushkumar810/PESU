
"use client";

import { useState } from "react";

export default function Home() {
  const [Id, setId] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  async function getStudent() {
    setMessage("");
    setLoading(true);

    try {
      const url = `/api/student?id=${encodeURIComponent(Id)}`;

      const response = await fetch(url);
      const data = await response.json();

      if (!response.ok) {
        setMessage(data.message);
      } else {
        setMessage(
          `${data.message}\n${JSON.stringify(data.student, null, 2)}`
        );
      }
    } catch (error) {
      setMessage("Something went wrong!");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex min-h-screen flex-col items-center justify-center gap-5 p-6">
      <h1 className="text-3xl font-bold">Student Details</h1>

      <input
        type="text"
        placeholder="Enter Student ID"
        value={Id}
        onChange={(e) => setId(e.target.value)}
        className="w-72 rounded border border-gray-400 p-3"
      />

      <button
        onClick={getStudent}
        disabled={loading}
        className="rounded bg-blue-600 px-6 py-2 text-white hover:bg-blue-700"
      >
        {loading ? "Loading..." : "Get Student"}
      </button>

      {message && (
        <pre className="w-full max-w-md whitespace-pre-wrap rounded bg-gray-100 p-4 text-black">
          {message}
        </pre>
      )}
    </div>
  );
}
