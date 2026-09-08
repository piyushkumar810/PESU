export default async function UsersPage() {
  const response = await fetch(
    "https://jsonplaceholder.typicode.com/users",
    {
      cache: "no-store",
    }
  );

  // Check whether the request was successful
  if (!response.ok) {
    throw new Error("Failed to fetch users");
  }

  // Convert API response to JSON
  const users = await response.json();

  return (
    <div>
      <h1>User List</h1>

      {users.map((user: any) => (
        <p key={user.id}>
          {user.id} - {user.name}
        </p>
      ))}
    </div>
  );
}