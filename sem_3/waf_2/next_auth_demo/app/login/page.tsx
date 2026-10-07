import LoginForm from "./login-form";

export default function LoginPage() {
  return (
    <main className="page-shell">
      <section className="card">
        <p className="eyebrow">Credentials provider</p>
        <h1>Sign in</h1>
        <p className="helper">
          Demo credentials: <strong>your_name</strong> / <strong>12345</strong>
        </p>
        <LoginForm />
      </section>
    </main>
  );
}
