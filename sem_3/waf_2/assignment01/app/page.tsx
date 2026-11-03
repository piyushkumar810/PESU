import Link from "next/link";

export default function Home() {
  return (
    <main className="dashboard">

      <h1>Next.js Assignments</h1>

      <p className="subtitle">
        Welcome! Select an assignment to continue.
      </p>

      {/* Assignment 18 */}
      <div className="assignment-box">

        <h2>Assignment 18 – Feedback Moderation</h2>

        <p>
          Submit feedback with ratings and comments.
          Admins can review and approve pending feedback.
        </p>

        <Link
          href="/assignment18"
          className="assignment-button"
        >
          Open Assignment 18
        </Link>

      </div>

      {/* Assignment 49 */}
      <div className="assignment-box">

        <h2>Assignment 49 – Context Reset on Logout</h2>

        <p>
          Manage user-specific data using React Context
          and clear the data when the user logs out.
        </p>

        <Link
          href="/assignment49"
          className="assignment-button"
        >
          Open Assignment 49
        </Link>

      </div>

      <Link href="/login" className="login-link">
        Login
      </Link>

    </main>
  );
}