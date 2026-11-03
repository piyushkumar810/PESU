import Link from "next/link";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-6 bg-gray-100">

      <h1 className="text-4xl font-bold">
        Next.js Assignments
      </h1>

      <Link
        href="/assignment18"
        className="rounded bg-blue-600 px-6 py-3 text-white"
      >
        Assignment 18 - Feedback Moderation
      </Link>

      <Link
        href="/assignment49"
        className="rounded bg-green-600 px-6 py-3 text-white"
      >
        Assignment 49 - Context Reset
      </Link>

      <Link
        href="/login"
        className="rounded bg-gray-800 px-6 py-3 text-white"
      >
        Login
      </Link>

    </main>
  );
}