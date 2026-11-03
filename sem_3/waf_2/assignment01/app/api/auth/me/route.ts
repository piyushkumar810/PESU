import { NextResponse } from "next/server";
import { getSession } from "@/lib/auth";

const privateData: Record<string, object> = {
  student01: {
    course: "MCA",
    semester: 3,
    department: "Computer Applications",
  },
  admin01: {
    department: "Administration",
    access: "Full Access",
  },
};

export async function GET() {
  const user = await getSession();

  if (!user) {
    return NextResponse.json(
      { message: "Unauthorized" },
      { status: 401 }
    );
  }

  return NextResponse.json({
    user,
    privateData: privateData[user.userId],
  });
}