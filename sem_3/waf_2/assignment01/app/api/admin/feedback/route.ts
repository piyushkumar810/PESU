import { NextRequest, NextResponse } from "next/server";
import { getSession } from "@/lib/auth";
import { feedbackData } from "@/lib/store";

// GET: View all feedback (admin only)
export async function GET() {
  const user = await getSession();

  if (!user || user.role !== "admin") {
    return NextResponse.json(
      { message: "Admin access required" },
      { status: 403 }
    );
  }

  return NextResponse.json({
    feedback: feedbackData,
  });
}

// PATCH: Approve feedback (admin only)
export async function PATCH(request: NextRequest) {
  const user = await getSession();

  if (!user || user.role !== "admin") {
    return NextResponse.json(
      { message: "Only admins can approve feedback" },
      { status: 403 }
    );
  }

  try {
    const { id } = await request.json();

    const feedback = feedbackData.find(
      (item) => item.id === id
    );

    if (!feedback) {
      return NextResponse.json(
        { message: "Feedback not found" },
        { status: 404 }
      );
    }

    feedback.status = "approved";

    return NextResponse.json({
      message: "Feedback approved successfully",
      feedback,
    });

  } catch {
    return NextResponse.json(
      { message: "Invalid request" },
      { status: 400 }
    );
  }
}