import { NextRequest, NextResponse } from "next/server";
import { SignJWT } from "jose";

const secret = new TextEncoder().encode(
  process.env.JWT_SECRET!
);

const users = [
  {
    id: "student01",
    name: "Piyush Kumar",
    email: "student@gmail.com",
    password: "student123",
    role: "student" as const,
    privateData: {
      course: "MCA",
      semester: 3,
      department: "Computer Applications",
    },
  },
  {
    id: "admin01",
    name: "Admin",
    email: "admin@gmail.com",
    password: "admin123",
    role: "admin" as const,
    privateData: {
      department: "Administration",
      access: "Full Access",
    },
  },
];

export async function POST(request: NextRequest) {
  try {
    const { email, password } = await request.json();

    const user = users.find(
      (u) =>
        u.email === email &&
        u.password === password
    );

    if (!user) {
      return NextResponse.json(
        { message: "Invalid email or password" },
        { status: 401 }
      );
    }

    const token = await new SignJWT({
      userId: user.id,
      email: user.email,
      role: user.role,
      name: user.name,
    })
      .setProtectedHeader({ alg: "HS256" })
      .setIssuedAt()
      .setExpirationTime("1d")
      .sign(secret);

    const response = NextResponse.json({
      message: "Login successful",
      user: {
        id: user.id,
        name: user.name,
        email: user.email,
        role: user.role,
      },
      privateData: user.privateData,
    });

    response.cookies.set("session", token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === "production",
      sameSite: "lax",
      path: "/",
      maxAge: 60 * 60 * 24,
    });

    return response;
  } catch {
    return NextResponse.json(
      { message: "Invalid request" },
      { status: 400 }
    );
  }
}