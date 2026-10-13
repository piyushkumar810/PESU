"use client";

import { useState } from "react";

export default function Home() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [token, setToken] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  async function login() {
    setLoading(true);
    setMessage("");
    setToken("");

    try {
      const response = await fetch("/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username,
          password,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        setMessage(data.message);
        return;
      }

      setMessage(data.message);
      setToken(data.token);
    } catch {
      setMessage("Unable to connect to the server");
    } finally {
      setLoading(false);
    }
  }

  async function getProfile() {
    if (!token) {
      setMessage("Please login first");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("/api/profile", {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await response.json();

      setMessage(
        `HTTP Status: ${response.status}\n${JSON.stringify(data, null, 2)}`
      );
    } catch {
      setMessage("Unable to connect to the server");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main
      style={{
        maxWidth: "700px",
        margin: "50px auto",
        padding: "30px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <h1>JWT Authentication Demo</h1>

      <p>Login to generate a JWT and access the protected profile.</p>

      <form
        onSubmit={(e) => {
          e.preventDefault();
          login();
        }}
      >
        <div style={{ marginBottom: "15px" }}>
          <label htmlFor="username">Username</label>
          <br />
          <input
            id="username"
            type="text"
            placeholder="Enter username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            style={{ width: "100%", padding: "10px", marginTop: "5px" }}
          />
        </div>

        <div style={{ marginBottom: "20px" }}>
          <label htmlFor="password">Password</label>
          <br />
          <input
            id="password"
            type="password"
            placeholder="Enter password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={{ width: "100%", padding: "10px", marginTop: "5px" }}
          />
        </div>

        <button type="submit" disabled={loading}>
          {loading ? "Please wait..." : "Login"}
        </button>
      </form>

      <hr style={{ margin: "25px 0" }} />

      <h3>Response</h3>

      <pre
        style={{
          padding: "15px",
          background: "#f2f2f2",
          color: "#222",
          whiteSpace: "pre-wrap",
          overflowWrap: "anywhere",
          borderRadius: "5px",
        }}
      >
        {message || "Login to see the response"}
      </pre>

      {token && (
        <>
          <h3>JWT Token</h3>

          <textarea
            value={token}
            readOnly
            rows={6}
            style={{
              width: "100%",
              padding: "10px",
              overflowWrap: "anywhere",
              boxSizing: "border-box",
            }}
          />

          <p>
            <strong>Token structure:</strong> HEADER.PAYLOAD.SIGNATURE
          </p>

          <button onClick={getProfile} disabled={loading}>
            {loading ? "Please wait..." : "Access Protected Profile"}
          </button>
        </>
      )}
    </main>
  );
}