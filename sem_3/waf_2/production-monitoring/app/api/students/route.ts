import { NextResponse } from "next/server";

export async function GET() {
  try {
    console.log("API request received");

    throw new Error("Something went wrong!");

  } catch (error) {
    console.error("API Error:", error);

    return NextResponse.json(
      { success:false,
        message: "Unable to fetch students" 
      },
      { status: 500 }
    );
  }
}