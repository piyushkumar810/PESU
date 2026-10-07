import Link from "next/link";
import { auth } from "../auth";
import SignOutButton from "./sign-out-button";

export const instant = false;

export default async function Home() {
  const session = await auth();

  return (
    <main className="page-shell">
      <section className="card">
        <p className="eyebrow">Auth.js + Next.js</p>
        <h1>Authentication Demo</h1>
        {session?.user ? (
          <>
            <p>
              You are signed in as <strong>{session.user.name}</strong>.
            </p>
            <div className="actions">
              <Link className="button primary" href="/dashboard">
                Open dashboard
              </Link>
              <SignOutButton />
            </div>
          </>
        ) : (
          <>
            <p>Sign in to access the protected dashboard.</p>
            <Link className="button primary" href="/login">
              Sign in
            </Link>
          </>
        )}
      </section>
    </main>
  );
}
