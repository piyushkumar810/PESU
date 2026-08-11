interface StudentProps {
  name: string;
  age: number;
  course: string;
}

function Student(props: StudentProps) {
  return (
    <div>
      <h2>Student Details</h2>
      <p>Name: {props.name}</p>
      <p>Age: {props.age}</p>
      <p>Course: {props.course}</p>
    </div>
  );
}

export default Student;