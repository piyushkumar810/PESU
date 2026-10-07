import Link from "next/link";
import { redirect } from "next/navigation";
import { auth } from "../../auth";
import SignOutButton from "../sign-out-button";

export const instant = false;

export default async function DashboardPage() {
  const session = await auth();

  if (!session?.user) {
    redirect("/login");
  }

  return (
    <main className="page-shell">
      <section className="card">
        <p className="eyebrow">Protected page</p>
        <h1>Dashboard</h1>
        <p>
          Welcome, <strong>{session.user.name}</strong>.
        </p>
        <p className="helper">Email: {session.user.email}</p>
        <div className="actions">
          <Link className="button secondary" href="/">
            Home
          </Link>
          <SignOutButton />
        </div>
      </section>
    </main>
  );
}
