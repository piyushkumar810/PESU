interface ProductPageProps {
  params: Promise<{
    category: string;
    id: string;
  }>;
}

export default async function ProductPage({
  params,
}: ProductPageProps) {
  const { category, id } = await params;

  let product;

  if (id === "101") {
    product = {
      id: "101",
      name: "Mobile",
      price: 25000,
    };
  } else if (id === "102") {
    product = {
      id: "102",
      name: "Laptop",
      price: 50000,
    };
  } else {
    product = {
      id: id,
      name: "Product Not Found",
      price: 0,
    };
  }

  return (
    <div>
      <h1>Product Details</h1>

      <p>Category: {category}</p>

      <p>Product ID: {product.id}</p>

      <p>Product Name: {product.name}</p>

      <p>Product price: {product.price}</p>
    </div>
  );
}