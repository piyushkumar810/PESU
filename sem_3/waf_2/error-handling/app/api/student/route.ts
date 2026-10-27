
import { NextResponse } from "next/server";

const students = [
  { id: 101, name: "Piyush Kumar", course: "MCA", age: 23 },
  { id: 102, name: "Avinash Kumar", course: "BCA", age: 22 },
  { id: 103, name: "Aman Singh", course: "B.Tech", age: 21 },
];

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const studentId = searchParams.get("id");

  // Check if student ID is missing
  if (studentId === null || studentId.trim() === "") {
    return NextResponse.json(
      { message: "Student ID required" },
      { status: 400 }
    );
  }

  // Check if student ID is valid
  const id = Number(studentId);

  if (!Number.isInteger(id) || id <= 0) {
    return NextResponse.json(
      { message: "Invalid student ID" },
      { status: 400 }
    );
  }

  // Find student
  const student = students.find((s) => s.id === id);

  if (!student) {
    return NextResponse.json(
      { message: "Student not found" },
      { status: 404 }
    );
  }

  // Student found successfully
  return NextResponse.json(
    {
      message: "Record fetched successfully",
      student,
    },
    { status: 200 }
  );
}
