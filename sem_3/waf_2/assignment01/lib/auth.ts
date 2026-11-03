import { cookies } from "next/headers";
import { jwtVerify } from "jose";

const secret = new TextEncoder().encode(
  process.env.JWT_SECRET!
);

export type SessionUser = {
  userId: string;
  email: string;
  role: "student" | "admin";
  name: string;
};

export async function getSession(): Promise<SessionUser | null> {
  const cookieStore = await cookies();

  const token = cookieStore.get("session")?.value;

  if (!token) {
    return null;
  }

  try {
    const { payload } = await jwtVerify(token, secret);

    return {
      userId: String(payload.userId),
      email: String(payload.email),
      role: payload.role as "student" | "admin",
      name: String(payload.name),
    };
  } catch {
    return null;
  }
}