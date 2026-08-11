import Student from "../components/Student";

export default function Home() {
  return (
    <div>
      <h2>Executing prop types in NextJs</h2>

      <Student
        name="Akansha"
        age={20}
        course="MCA"
      />
    </div>
  );
}