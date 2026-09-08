export default async function PostsPage() {
  const response = await fetch(
    "https://jsonplaceholder.typicode.com/posts",
    {
      next: {
        revalidate: 10,
      },
    }
  );

  if (!response.ok) {
    throw new Error("Failed to fetch posts");
  }

  const posts = await response.json();

  return (
    <div>
      <h1>Posts</h1>

      {posts.slice(0, 10).map((post: any) => (
        <div key={post.id}>
          <h2>{post.id}. {post.title}</h2>

          <p>{post.body}</p>

          <hr />
        </div>
      ))}
    </div>
  );
}


/*
Most important ISR code
next: {
  revalidate: 10,
}

It means the fetched data can be regenerated after 10 seconds.
*/