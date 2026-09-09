export const revalidate = 60;

export default async function ProductsPage() {
  const response = await fetch(
    "https://fakestoreapi.com/products"
  );

  if (!response.ok) {
    throw new Error("Failed to fetch products");
  }

  const products = await response.json();

  return (
    <div>
      <h1>Products</h1>

      {products.map((product: any) => (
        <div key={product.id}>
          <h2>{product.title}</h2>
          <p>Price: ${product.price}</p>
          <p>{product.description}</p>
        </div>
      ))}
    </div>
  );
}