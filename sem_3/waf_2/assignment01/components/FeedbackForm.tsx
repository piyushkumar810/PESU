
"use client";

import { useState } from "react";

type Feedback = {
  id: string;
  rating: number;
  comment: string;
  status: "pending" | "approved";
  createdAt: string;
};

export default function FeedbackForm() {
  const [rating, setRating] = useState(5);
  const [comment, setComment] = useState("");
  const [message, setMessage] = useState("");
  const [submittedFeedback, setSubmittedFeedback] =
    useState<Feedback | null>(null);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    setMessage("");

    try {
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

      if (!response.ok) {
        setMessage(data.message);
        return;
      }

      setMessage(data.message);

      // Display submitted feedback
      setSubmittedFeedback(data.feedback);

      // Reset form
      setComment("");
      setRating(5);

    } catch {
      setMessage("Something went wrong. Try again.");
    }
  }

  return (
    <div className="max-w-2xl rounded-xl border border-gray-300 bg-white p-6 shadow-sm">

      <h2 className="mb-5 text-2xl font-bold">
        Submit Feedback
      </h2>

      <form onSubmit={handleSubmit} className="space-y-5">

        <div>
          <label className="block font-medium">
            Rating (1-5)
          </label>

          <select
            value={rating}
            onChange={(e) =>
              setRating(Number(e.target.value))
            }
            className="mt-2 w-full rounded border p-3"
          >
            {[1, 2, 3, 4, 5].map((value) => (
              <option key={value} value={value}>
                {value} Stars
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
          className="rounded bg-blue-600 px-6 py-3 text-white hover:bg-blue-700"
        >
          Submit Feedback
        </button>

      </form>

      {message && (
        <p className="mt-4 font-medium">
          {message}
        </p>
      )}

      {/* Display submitted feedback */}
      {submittedFeedback && (
        <div className="mt-6 rounded-lg border border-gray-300 bg-gray-50 p-5">

          <h3 className="mb-4 text-xl font-bold">
            Submitted Feedback
          </h3>

          <p>
            <strong>Rating:</strong>{" "}
            {submittedFeedback.rating}/5
          </p>

          <p className="mt-2">
            <strong>Comment:</strong>{" "}
            {submittedFeedback.comment}
          </p>

          <p className="mt-2">
            <strong>Status:</strong>{" "}
            <span className="rounded bg-yellow-100 px-3 py-1 text-yellow-800">
              {submittedFeedback.status}
            </span>
          </p>

          <p className="mt-3 text-sm text-gray-500">
            Your feedback is waiting for admin approval.
          </p>

        </div>
      )}

    </div>
  );
}
