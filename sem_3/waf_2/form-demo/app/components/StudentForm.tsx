
"use client";

import { useState } from "react";

type Props = {
  onSubmit: (name: string, email: string) => void;
};

export default function StudentForm({ onSubmit }: Props) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!name.trim() || !email.trim()) {
      alert("Please enter both name and email.");
      return;
    }

    onSubmit(name, email);

    setName("");
    setEmail("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Student Registration</h2>

      <label htmlFor="name">Name:</label>
      <br />

      <input
        id="name"
        type="text"
        placeholder="Enter Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
      />

      <br />
      <br />

      <label htmlFor="email">Email:</label>
      <br />

      <input
        id="email"
        type="email"
        placeholder="Enter Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />

      <br />
      <br />

      <button type="submit">Register Student</button>
    </form>
  );
}
