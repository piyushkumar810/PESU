"use client";

export default function Dashboard() {
  function handleLogout() {
    document.cookie = "token=; Max-Age=0; path=/";
    window.location.href = "/login";
  }

  return (
    <main>
      <h1>Student Dashboard</h1>

      <p>Welcome! You can access the dashboard.</p>

      <ul>
        <li>Student Name-1</li>
        <li>Student Name-2</li>
        <li>Student Name-3</li>
      </ul>

      <button onClick={handleLogout}>
        Logout
      </button>
    </main>
  );
}