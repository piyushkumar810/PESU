
"use client";

import { useState } from "react";

export default function Home() {
  const [page, setPage] = useState("home");

  // Student data
  const students = [
    { id: 101, name: "Rahul", course: "BCA" },
    { id: 102, name: "Priya", course: "MCA" },
    { id: 103, name: "Kiran", course: "BCA" },
  ];

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1>Student Management System</h1>

      {/* Navigation */}
      <nav style={{ marginBottom: "25px" }}>
        <button onClick={() => setPage("home")}>
          Home
        </button>

        <button
          onClick={() => setPage("students")}
          style={{ marginLeft: "10px" }}
        >
          Students
        </button>

        <button
          onClick={() => setPage("about")}
          style={{ marginLeft: "10px" }}
        >
          About
        </button>
      </nav>

      {/* Home Page */}
      {page === "home" && (
        <div>
          <h2>Welcome to Student Management System</h2>
          <p>Manage student records easily.</p>
          <p>Total Students: {students.length}</p>
        </div>
      )}

      {/* Students Page */}
      {page === "students" && (
        <div>
          <h2>Student List</h2>

          <table
            border={1}
            cellPadding={12}
            style={{
              borderCollapse: "collapse",
              width: "100%",
              textAlign: "left",
            }}
          >
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Course</th>
              </tr>
            </thead>

            <tbody>
              {students.map((student) => (
                <tr key={student.id}>
                  <td>{student.id}</td>
                  <td>{student.name}</td>
                  <td>{student.course}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* About Page */}
      {page === "about" && (
        <div>
          <h2>About Us</h2>
          <p>
            Welcome to the Student Management System.
          </p>
          <p>
            This application helps manage student
            information, records and courses.
          </p>
          <p>
            It is developed using Next.js and React.
          </p>
        </div>
      )}

    </div>
  );
}
