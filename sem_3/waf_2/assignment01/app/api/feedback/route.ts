import { NextRequest, NextResponse } from "next/server";
import { getSession } from "@/lib/auth";
import { feedbackData } from "@/lib/store";

export async function POST(request: NextRequest) {
  try {
    const user = await getSession();

    if (!user) {
      return NextResponse.json(
        { message: "Please login first" },
        { status: 401 }
      );
    }

    if (user.role !== "student") {
      return NextResponse.json(
        { message: "Only students can submit feedback" },
        { status: 403 }
      );
    }

    const { rating, comment } = await request.json();

    // Validate rating
    if (
      !Number.isInteger(rating) ||
      rating < 1 ||
      rating > 5
    ) {
      return NextResponse.json(
        { message: "Rating must be an integer between 1 and 5" },
        { status: 400 }
      );
    }

    // Validate comment
    if (
      typeof comment !== "string" ||
      comment.trim().length < 5 ||
      comment.trim().length > 500
    ) {
      return NextResponse.json(
        { message: "Comment must contain 5 to 500 characters" },
        { status: 400 }
      );
    }

    // Create feedback
    const newFeedback = {
      id: crypto.randomUUID(),
      userId: user.userId,
      rating,
      comment: comment.trim(),
      status: "pending" as const,
      createdAt: new Date().toISOString(),
    };

    feedbackData.push(newFeedback);

    return NextResponse.json(
      {
        message: "Feedback submitted successfully",
        feedback: newFeedback,
      },
      { status: 201 }
    );

  } catch {
    return NextResponse.json(
      { message: "Invalid request" },
      { status: 400 }
    );
  }
}