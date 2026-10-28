
import { cookies } from "next/headers";
import { redirect } from "next/navigation";

export default async function SettingsPage() {
  const cookieStore = await cookies();
  const session = cookieStore.get("session");

  if (!session || session.value !== "admin") {
    redirect("/login");
  }

  return (
    <main>
      <h1>Settings Page</h1>

      <p>Manage your account settings here.</p>

      <a href="/dashboard">Back to Dashboard</a>
    </main>
  );
}