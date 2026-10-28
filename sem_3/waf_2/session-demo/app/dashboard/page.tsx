
import { cookies } from "next/headers";
import { redirect } from "next/navigation";

export default async function DashboardPage() {
  const cookieStore = await cookies();
  const session = cookieStore.get("session");

  if (!session || session.value !== "admin") {
    redirect("/login");
  }

  return (
    <main>
      <h1>Dashboard</h1>

      <p>Welcome, Admin!</p>

      <nav>
        <ul>
          <li>
            <a href="/profile">Profile</a>
          </li>

          <li>
            <a href="/settings">Settings</a>
          </li>
        </ul>
      </nav>

      <form action="/api/logout" method="POST">
        <button type="submit">Logout</button>
      </form>
    </main>
  );
}
