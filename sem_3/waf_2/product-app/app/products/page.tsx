import Link from "next/link";

export default function ProductsPage() {
  return (
    <div>
      <h1>Products Page</h1>

      <h2>Categories</h2>

      <ul>
        <li>
          <Link href="/products/electronics">
            Electronics
          </Link>
        </li>

        <li>
          <Link href="/products/clothing">
            Clothing
          </Link>
        </li>
      </ul>
    </div>
  );
}