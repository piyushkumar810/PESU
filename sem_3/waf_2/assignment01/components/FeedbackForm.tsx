"use client";

import { useState } from "react";

export default function FeedbackForm() {
  const [rating, setRating] = useState(5);
  const [comment, setComment] = useState("");
  const [message, setMessage] = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    const response = await fetch("/api/feedback", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        rating,
        comment,
      }),
    });

    const data = await response.json();

    setMessage(data.message);

    if (response.ok) {
      setComment("");
      setRating(5);
    }
  }

  return (
    <div className="max-w-lg rounded-xl border p-6 shadow">
      <h2 className="mb-4 text-2xl font-bold">
        Submit Feedback
      </h2>

      <form onSubmit={handleSubmit} className="space-y-4">

        <div>
          <label className="block font-medium">
            Rating (1–5)
          </label>

          <select
            value={rating}
            onChange={(e) =>
              setRating(Number(e.target.value))
            }
            className="mt-2 w-full rounded border p-2"
          >
            {[1, 2, 3, 4, 5].map((value) => (
              <option key={value} value={value}>
                {value} Star{value > 1 ? "s" : ""}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label className="block font-medium">
            Your Comment
          </label>

          <textarea
            value={comment}
            onChange={(e) =>
              setComment(e.target.value)
            }
            placeholder="Write your feedback..."
            className="mt-2 w-full rounded border p-3"
            rows={4}
          />
        </div>

        <button
          type="submit"
          className="rounded bg-blue-600 px-5 py-2 text-white hover:bg-blue-700"
        >
          Submit Feedback
        </button>

        {message && (
          <p className="text-sm font-medium">
            {message}
          </p>
        )}
      </form>
    </div>
  );
}