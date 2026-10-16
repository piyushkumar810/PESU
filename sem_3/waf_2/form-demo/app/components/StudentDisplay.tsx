
type Props = {
  name: string;
  email: string;
};

export default function StudentDisplay({ name, email }: Props) {
  return (
    <div>
      <h2>Student Details</h2>

      <p>Name: {name}</p>
      <p>Email: {email}</p>
    </div>
  );
}
