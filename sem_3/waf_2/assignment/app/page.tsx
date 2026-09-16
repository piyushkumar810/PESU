import Link from "next/link";

export default function Home() {
  return (
    <div>
      <h1>My Next.js Assignments</h1>

      <ul>
        <li>
          <Link href="/counter03">Q3 - Counter</Link>
        </li>

        <li>
          <Link href="/tailwind-heading08">
            Q8 - Tailwind Heading
          </Link>
        </li>

        <li>
          <Link href="/hover-button09">
            Q9 - Hover Button
          </Link>
        </li>

        <li>
          <Link href="/navigation14">
            Q14 - Navigation
          </Link>
        </li>
      </ul>
    </div>
  );
}