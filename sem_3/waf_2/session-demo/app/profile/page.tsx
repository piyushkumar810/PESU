import { cookies } from "next/headers";
import { redirect } from "next/navigation";

export default async function ProfilePage() {
  const cookieStore = await cookies();
  const session = cookieStore.get("session");

  if (!session || session.value !== "admin") {
    redirect("/login");
  }

  return (
    <main>
      <h1>Profile Page</h1>

      <p>Username: admin</p>
      <p>Role: Administrator</p>

      <a href="/dashboard">Back to Dashboard</a>
    </main>
  );
}