
import Link from "next/link";

export default function Home() {
  return (
    <main className="dashboard">
      <div className="container">

        {/* Header */}
        <header className="header">
          <span className="tag">
            NEXT.JS PRACTICAL PROJECT
          </span>

          <h1>Next.js Assignments</h1>

          <p>
            Welcome to your assignment dashboard.
            Explore practical implementations of
            authentication, feedback moderation
            and React Context API.
          </p>
        </header>

        {/* Assignment Cards */}
        <section className="cards">

          {/* Assignment 18 */}
          <div className="assignment-card">

            <div className="card-icon blue-icon">
              ⭐
            </div>

            <span className="card-label">
              Assignment 18
            </span>

            <h2>Feedback Moderation</h2>

            <p>
              Submit student feedback, validate
              ratings and comments, and allow
              administrators to approve pending
              feedback.
            </p>

            <div className="features">
              <span>API Validation</span>
              <span>Admin Authorization</span>
              <span>HTTP 400 / 403</span>
            </div>

            <Link
              href="/assignment18"
              className="card-button blue-button"
            >
              Open Assignment →
            </Link>

          </div>

          {/* Assignment 49 */}
          <div className="assignment-card">

            <div className="card-icon purple-icon">
              🔐
            </div>

            <span className="card-label">
              Assignment 49
            </span>

            <h2>Context Reset on Logout</h2>

            <p>
              Manage user-specific information
              using React Context and securely
              clear application state when a
              user logs out.
            </p>

            <div className="features">
              <span>React Context</span>
              <span>Authentication</span>
              <span>Session Management</span>
            </div>

            <Link
              href="/assignment49"
              className="card-button purple-button"
            >
              Open Assignment →
            </Link>

          </div>

        </section>

        {/* Login */}
        <div className="login-section">
          Already have an account?{" "}
          <Link href="/login">
            Login here →
          </Link>
        </div>

        <footer className="footer">
          Built with Next.js · React · TypeScript
        </footer>

      </div>
    </main>
  );
}
