"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/contexts/AuthContext";

export default function LoginPage() {
  const { login } = useAuth();

  const router = useRouter();

  const [email, setEmail] = useState("student@gmail.com");
  const [password, setPassword] = useState("student123");
  const [message, setMessage] = useState("");

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault();

    try {
      await login(email, password);

      setMessage("Login successful!");

      router.push("/assignment49");
    } catch (error) {
      setMessage(
        error instanceof Error
          ? error.message
          : "Login failed"
      );
    }
  }

  return (
    <main className="flex min-h-screen items-center justify-center bg-gray-100 p-5">

      <form
        onSubmit={handleLogin}
        className="w-full max-w-md space-y-4 rounded-xl bg-white p-8 shadow"
      >
        <h1 className="text-3xl font-bold">
          Login
        </h1>

        <div>
          <label>Email</label>

          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="mt-1 w-full rounded border p-3"
            required
          />
        </div>

        <div>
          <label>Password</label>

          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="mt-1 w-full rounded border p-3"
            required
          />
        </div>

        <button
          type="submit"
          className="w-full rounded bg-blue-600 p-3 text-white"
        >
          Login
        </button>

        {message && (
          <p className="text-sm">{message}</p>
        )}

        <p className="text-xs text-gray-500">
          Student: student@gmail.com / student123
        </p>

        <p className="text-xs text-gray-500">
          Admin: admin@gmail.com / admin123
        </p>
      </form>
    </main>
  );
}