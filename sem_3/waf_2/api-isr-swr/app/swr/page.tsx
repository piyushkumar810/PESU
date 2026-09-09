"use client";

import useSWR from "swr";

const fetcher = (url: string) =>
  fetch(url).then((res) => res.json());

export default function UsersPage() {
  const { data, error, isLoading } = useSWR(
    "https://jsonplaceholder.typicode.com/users",
    fetcher
  );

  if (isLoading) {
    return <h2>Loading users...</h2>;
  }

  if (error) {
    return <h2>Error loading users</h2>;
  }

  return (
    <div>
      <h1>User List</h1>

      {data.map((user: any) => (
        <p key={user.id}>
          {user.id} - {user.name}
        </p>
      ))}
    </div>
  );
}