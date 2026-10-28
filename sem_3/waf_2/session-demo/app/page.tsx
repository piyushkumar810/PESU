"use client";

import { useRouter } from "next/navigation";

export default function HomePage() {
  const router = useRouter();

  return (
    <main>
      <h1>Session Demo</h1>

      <p>Welcome to the Session Demo project.</p>

      <button onClick={() => router.push("/login")}>
        Login
      </button>
    </main>
  );
}