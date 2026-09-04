"use client"
import Link from "next/link";

export default function Home() {
  return (
    <div>
      <h1>CSR and SSR Demo</h1>

      <h2>Client Side Rendering</h2>
      <Link href="/comments">Comments - CSR</Link>

      <br />
      <br />

      <h2>Browser Information</h2>
      <Link href="/window">Window Information</Link>
    </div>
  );
}