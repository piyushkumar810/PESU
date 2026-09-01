interface CategoryPageProps {
  params: Promise<{
    category: string;
  }>;
}

export default async function CategoryPage({
  params,
}: CategoryPageProps) {
  const { category } = await params;

  return (
    <div>
      <h1>Category Page</h1>

      <p>Category: {category}</p>

      <h2>Products</h2>

      <p>
        <a href={`/products/${category}/101`}>
          Product 101
        </a>
      </p>

      <p>
        <a href={`/products/${category}/102`}>
          Product 102
        </a>
      </p>
    </div>
  );
}