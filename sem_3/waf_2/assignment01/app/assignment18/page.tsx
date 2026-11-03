"use client";

import Link from "next/link";
import { useAuth } from "@/contexts/AuthContext";
import FeedbackForm from "@/components/FeedbackForm";
import AdminFeedback from "@/components/AdminFeedback";

export default function Assignment18() {
  const { user } = useAuth();

  return (
    <main className="min-h-screen bg-gray-50 p-8 text-gray-900">
      <div className="mx-auto max-w-4xl">

        <h1 className="mb-2 text-3xl font-bold">
          Assignment 18: Feedback Moderation
        </h1>

        <p className="mb-6 text-gray-600">
          Submit feedback and manage its approval status.
        </p>

        {!user ? (
          <div>
            <p>Please login to continue.</p>
            <Link
              href="/login"
              className="text-blue-600 underline"
            >
              Login here
            </Link>
          </div>
        ) : user.role === "student" ? (
          <FeedbackForm />
        ) : (
          <AdminFeedback />
        )}

      </div>
    </main>
  );
}