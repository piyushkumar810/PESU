This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.



## study for this project
<!--
🧪 Next.js Project — Testing Guide
1. Start the Development Server

Run:

npm run dev

Then open the application in your browser.

2. Test the Routes
🏠 Home Page

http://localhost:3000/

Expected: Home Page

↓

📦 Products Page

http://localhost:3000/products

Expected: Products Page with product categories

↓

📱 Electronics Category

http://localhost:3000/products/electronics

Expected: Category Page
Category: electronics

↓

📱 Product 101

http://localhost:3000/products/electronics/101

Expected:

Product Details
Category: electronics
Product ID: 101
Product Name: Mobile
Product Price: ₹25,000

↓

💻 Product 102

http://localhost:3000/products/electronics/102

Expected:

Product Details
Category: electronics
Product ID: 102
Product Name: Laptop
Product Price: ₹50,000

↓

❌ Invalid Product

http://localhost:3000/products/electronics/999

Expected:

Product Details
Category: electronics
Product ID: 999
Product Name: Product Not Found
Product Price: ₹0
🔑 Key Concept: Nested Dynamic Routing

Nested Dynamic Routing allows Next.js to create dynamic URLs using folders such as [category] and [id].

Route Structure

app → products → [category] → [id] → page.tsx

[category]

Captures the category name from the URL.

Example:

/products/electronics

→ Category = electronics

[id]

Captures the product ID from the URL.

Example:

/products/electronics/101

→ Product ID = 101

Complete Example

/products/electronics/101

→ category: electronics
→ id: 101

This is the main concept demonstrated by the project. 
 -->

 ## important
<!--

| Syntax      | Meaning                  | Example                                |
| ----------- | ------------------------ | -------------------------------------- |
| `[product]` | **Dynamic route**        | `/products/mobile`                     |
| `(product)` | **Route Group**          | Organizes folders without changing URL |
| `product`   | **Normal/static folder** | `/product`                             |
 -->