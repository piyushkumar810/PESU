
"use client";

import { useState } from "react";
import StudentForm from "./components/StudentForm";
import StudentDisplay from "./components/StudentDisplay";

export default function Home() {
  const [student, setStudent] = useState({
    name: "",
    email: "",
  });

  function onSubmit(name: string, email: string) {
    setStudent({ name, email });
  }

  return (
    <div>
      <h1>Student Application</h1>

      <StudentForm onSubmit={onSubmit} />

      <StudentDisplay
        name={student.name}
        email={student.email}
      />
    </div>
  );
}
