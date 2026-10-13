import { NextResponse } from "next/server";
import jwt, { JwtPayload } from "jsonwebtoken";

export async function GET(request: Request) {
  const authHeader = request.headers.get("Authorization");

  if (!authHeader) {
    return NextResponse.json(
      { message: "Authorization header missing" },
      { status: 401 }
    );
  }

  if (!authHeader.startsWith("Bearer ")) {
    return NextResponse.json(
      { message: "Authorization header must use the Bearer scheme" },
      { status: 401 }
    );
  }

  const token = authHeader.slice(7);

  if (!token) {
    return NextResponse.json(
      { message: "JWT token missing" },
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

  try {
    const decoded = jwt.verify(token, secret, {
      algorithms: ["HS256"],
    });

    if (
      typeof decoded === "string" ||
      !("role" in decoded) ||
      decoded.role !== "Admin"
    ) {
      return NextResponse.json(
        { message: "Forbidden: Admin access required" },
        { status: 403 }
      );
    }

    return NextResponse.json({
      message: "JWT is valid",
      user: decoded,
    });
  } catch {
    return NextResponse.json(
      { message: "Invalid or expired JWT" },
      { status: 401 }
    );
  }
}