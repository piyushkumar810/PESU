import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "JWT Authentication Demo",
  description: "Next.js JWT authentication and authorization demo",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}