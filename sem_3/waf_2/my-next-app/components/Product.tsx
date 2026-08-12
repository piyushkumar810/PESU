interface ProductProps {
    name: string;
    price: number;
}

function Product({ name, price }: ProductProps): string {
    const result = `${name} - ₹${price}`;

    console.log(result);

    return result;
}

export default Product;