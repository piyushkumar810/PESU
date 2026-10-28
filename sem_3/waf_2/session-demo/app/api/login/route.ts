import { NextResponse } from "next/server";

export async function POST(request: Request) {
  let body: unknown;

  // Parse request body
  try {
    body = await request.json();
  } catch {
    return NextResponse.json(
      { message: "Request body must be valid JSON" },
      { status: 400 }
    );
  }

  // Validate request body
  if (
    typeof body !== "object" ||
    body === null ||
    Array.isArray(body)
  ) {
    return NextResponse.json(
      { message: "Request body must be a JSON object" },
      { status: 400 }
    );
  }

  const { username, password } = body as {
    username?: unknown;
    password?: unknown;
  };

  // Validate username
  if (
    typeof username !== "string" ||
    username.trim() === ""
  ) {
    return NextResponse.json(
      { message: "Username is required" },
      { status: 400 }
    );
  }

  // Validate password
  if (
    typeof password !== "string" ||
    password.trim() === ""
  ) {
    return NextResponse.json(
      { message: "Password is required" },
      { status: 400 }
    );
  }

  // Demo login response
  const response = NextResponse.json(
    {
      message: "Login successful",
      user: {
        username: username.trim(),
      },
    },
    { status: 200 }
  );

  // Set a demo session cookie
  response.cookies.set("session", username.trim(), {
    httpOnly: true,
    secure: process.env.NODE_ENV === "production",
    sameSite: "lax",
    path: "/",
    maxAge: 60 * 60,
  });

  return response;
}
