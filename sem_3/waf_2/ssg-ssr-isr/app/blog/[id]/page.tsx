interface BlogPageProps {
  params: Promise<{
    id: string;
  }>;
}

export default async function BlogPage({
  params,
}: BlogPageProps) {
  const { id } = await params;

  const response = await fetch(
    `https://jsonplaceholder.typicode.com/posts/${id}`,
    {
      next: {
        revalidate: 10,
      },
    }
  );

  if (!response.ok) {
    throw new Error("Failed to fetch blog post");
  }

  const post = await response.json();

  return (
    <div>
      <h1>Blog Post</h1>

      <h2>
        {post.id}. {post.title}
      </h2>

      <p>{post.body}</p>
    </div>
  );
}