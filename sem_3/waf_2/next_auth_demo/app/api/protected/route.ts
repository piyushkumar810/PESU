import { NextResponse } from "next/server";
import { auth } from "../../../auth";

export const GET = auth((request) => {
  if (!request.auth) {
    return NextResponse.json(
      { message: "Authentication required." },
      { status: 401 },
    );
  }

  return NextResponse.json({
    message: "You have accessed a protected API route.",
    user: request.auth.user,
  });
});
