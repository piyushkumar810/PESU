import { NextResponse } from "next/server";
import jwt from "jsonwebtoken";

export async function POST(request: Request) {
  try {
    const { username, password } = await request.json();

    const users = [
      {
        id: 1,
        username: "admin",
        password: "1234",
        name: "Alice",
        role: "Admin",
      },
      {
        id: 2,
        username: "student",
        password: "1234",
        name: "Bob",
        role: "Student",
      },
    ];

    const user = users.find(
      (u) => u.username === username && u.password === password
    );

    if (!user) {
      return NextResponse.json(
        { message: "Invalid username or password" },
        { status: 401 }
      );
    }

    const secret = process.env.JWT_SECRET;

    if (!secret) {
      return NextResponse.json(
        { message: "JWT secret is not configured" },
        { status: 500 }
      );
    }

    const token = jwt.sign(
      {
        id: user.id,
        name: user.name,
        role: user.role,
      },
      secret,
      {
        expiresIn: "1h",
        algorithm: "HS256",
      }
    );

    return NextResponse.json({
      message: "Login successful",
      token,
    });
  } catch {
    return NextResponse.json(
      { message: "Invalid request body" },
      { status: 400 }
    );
  }
}