"use client";

import { useEffect, useState } from "react";

type Feedback = {
  id: string;
  userId: string;
  rating: number;
  comment: string;
  status: "pending" | "approved";
};

export default function AdminFeedback() {
  const [feedback, setFeedback] = useState<Feedback[]>([]);
  const [message, setMessage] = useState("");

  async function loadFeedback() {
    const response = await fetch("/api/admin/feedback");
    const data = await response.json();

    if (!response.ok) {
      setMessage(data.message);
      return;
    }

    setFeedback(data.feedback);
    setMessage("");
  }

  async function approveFeedback(id: string) {
    const response = await fetch("/api/admin/feedback", {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id }),
    });

    const data = await response.json();

    setMessage(data.message);

    if (response.ok) {
      await loadFeedback();
    }
  }

  useEffect(() => {
    loadFeedback();
  }, []);

  return (
    <div className="mt-8 rounded-xl border p-6 shadow">
      <h2 className="mb-4 text-2xl font-bold">
        Admin Feedback Dashboard
      </h2>

      {message && (
        <p className="mb-4 text-sm">{message}</p>
      )}

      {feedback.length === 0 ? (
        <p>No feedback available.</p>
      ) : (
        <div className="space-y-4">
          {feedback.map((item) => (
            <div
              key={item.id}
              className="rounded border p-4"
            >
              <p>
                <strong>Rating:</strong> {item.rating}/5
              </p>

              <p>
                <strong>Comment:</strong> {item.comment}
              </p>

              <p>
                <strong>Status:</strong>{" "}
                <span
                  className={
                    item.status === "approved"
                      ? "text-green-600"
                      : "text-orange-600"
                  }
                >
                  {item.status}
                </span>
              </p>

              {item.status === "pending" && (
                <button
                  onClick={() =>
                    approveFeedback(item.id)
                  }
                  className="mt-3 rounded bg-green-600 px-4 py-2 text-white"
                >
                  Approve
                </button>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}