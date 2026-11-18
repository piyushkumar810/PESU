
import { NextResponse } from "next/server";
import pool from "@/lib/db";

export async function GET() {
  try {
    // Check database connection
    await pool.query("SELECT 1");

    console.log("Database connection successful");

    return NextResponse.json({
      success: true,
      message: "Database connection successful",
    });

  } catch (error) {
    console.error("Database connection failed:", error);

    return NextResponse.json(
      {
        success: false,
        message: "Database connection failed",
      },
      { status: 500 }
    );
  }
}
