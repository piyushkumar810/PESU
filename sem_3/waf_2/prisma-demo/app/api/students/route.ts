
import { NextResponse } from "next/server";
import { prisma } from "../../../lib/prisma";

// GET: Fetch all student records
export async function GET() {
  try {
    const students = await prisma.student.findMany();

    return NextResponse.json(students);
  } catch (error) {
    console.error(error);
    return NextResponse.json(
      { message: "Failed to fetch students" },
      { status: 500 }
    );
  }
}

// POST: Insert a new student
export async function POST(request: Request) {
  try {
    const body = await request.json();

    const student = await prisma.student.create({
      data: {
        name: body.name,
        email: body.email,
        age: body.age,
      },
    });

    return NextResponse.json(student, { status: 201 });
  } catch (error) {
    console.error(error);
    return NextResponse.json(
      { message: "Failed to create student" },
      { status: 500 }
    );
  }
}
