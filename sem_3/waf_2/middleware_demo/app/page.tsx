import Link from "next/link";

export default function Home() {
  return (
    <main>
      <h1>Middleware Demo</h1>

      <p>Welcome to the Students Home page.</p>

      <Link href="/login">Login First</Link>

      <br />

      <Link href="/dashboard">Open Dashboard</Link>
    </main>
  );
}
