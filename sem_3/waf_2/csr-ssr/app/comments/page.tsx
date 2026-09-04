"use client";

import { useState, useEffect } from "react";

export default function Comments() {
  const [comments, setComments] = useState<any[]>([]);

  useEffect(() => {
    async function loadComments() {
      const response = await fetch(
        "https://jsonplaceholder.typicode.com/comments"
      );

      const data = await response.json();

      setComments(data);
    }

    loadComments();
  }, []);

  return (
    <div>
      <h1>Comments - CSR</h1>

      {comments.map((comment: any) => (
        <p key={comment.id}>
          ID: {comment.id}
          <br />
          User Email: {comment.email}
          <br />
          Topic Name: {comment.name}
        </p>
      ))}
    </div>
  );
}