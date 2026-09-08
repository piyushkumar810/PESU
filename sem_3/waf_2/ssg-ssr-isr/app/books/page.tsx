// Static Site Rendering - Data

const books = [
  "Next.js for Fast",
  "React",
  "TypeScript"
];

// The HTML is generated during the build.
export default function Books() {
  return (
    <div>
      <h1>Books</h1>

      <ul>
        {books.map((book) => (
          <li key={book}>{book}</li>
        ))}
      </ul>
    </div>
  );
}