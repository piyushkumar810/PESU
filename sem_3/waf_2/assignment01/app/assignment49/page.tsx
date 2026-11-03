"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuth } from "@/contexts/AuthContext";

export default function Assignment49() {
  const {
    user,
    privateData,
    logout,
    loading,
  } = useAuth();

  const router = useRouter();

  async function handleLogout() {
    await logout();

    router.push("/login");
  }

  if (loading) {
    return <p className="p-8">Loading session...</p>;
  }

  if (!user) {
    return (
      <main className="p-8">
        <h1 className="text-2xl font-bold">
          Please login first
        </h1>

        <Link
          href="/login"
          className="text-blue-600 underline"
        >
          Go to Login
        </Link>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-gray-100 p-8">

      <div className="mx-auto max-w-2xl rounded-xl bg-white p-8 shadow">

        <h1 className="mb-6 text-3xl font-bold">
          Assignment 49: Context Reset
        </h1>

        <h2 className="mb-3 text-xl font-semibold">
          Welcome, {user.name}
        </h2>

        <div className="mb-6 rounded bg-gray-100 p-4">
          <h3 className="mb-3 font-bold">
            User Information
          </h3>

          <p>Name: {user.name}</p>
          <p>Email: {user.email}</p>
          <p>Role: {user.role}</p>
        </div>

        <div className="mb-6 rounded bg-blue-50 p-4">
          <h3 className="mb-3 font-bold">
            Private Context Data
          </h3>

          {Object.entries(privateData ?? {}).map(
            ([key, value]) => (
              <p key={key}>
                <strong>{key}:</strong>{" "}
                {String(value)}
              </p>
            )
          )}
        </div>

        <button
          onClick={handleLogout}
          className="rounded bg-red-600 px-6 py-3 text-white hover:bg-red-700"
        >
          Logout
        </button>

      </div>
    </main>
  );
}