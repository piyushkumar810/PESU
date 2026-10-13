"use client";

export default function LoginPage() {
  function handleLogin() {
    document.cookie = "token=student123; path=/";
    window.location.href = "/dashboard";
  }

  return (
    <main>
      <h1>Student Login</h1>
      <p>Click the button to simulate login.</p>
      <button onClick={handleLogin}>Login</button>
    </main>
  );
}
