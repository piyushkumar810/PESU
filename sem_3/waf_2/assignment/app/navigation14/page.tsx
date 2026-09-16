import Link from "next/link";

export default function Navigation() {
  return (
    <div>
      <nav className="flex gap-6 p-5 bg-gray-800">
        <Link
          href="/"
          className="text-white hover:text-yellow-400"
        >
          Home
        </Link>

        <Link
          href="/about"
          className="text-white hover:text-yellow-400"
        >
          About
        </Link>

        <Link
          href="/services"
          className="text-white hover:text-yellow-400"
        >
          Services
        </Link>

        <Link
          href="/contact"
          className="text-white hover:text-yellow-400"
        >
          Contact
        </Link>
      </nav>

      <h1 className="text-3xl font-bold p-10">
        Navigation Page
      </h1>
    </div>
  );
}