"use client";

import { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div className="text-center mt-20">
      <h1 className="text-3xl font-bold mb-5">Counter Application</h1>

      <h2 className="text-2xl mb-5">Count: {count}</h2>

      <button
        onClick={() => setCount(count - 1)}
        className="bg-red-500 text-white px-5 py-2 rounded mr-3 hover:bg-red-700"
      >
        - Decrement
      </button>

      <button
        onClick={() => setCount(count + 1)}
        className="bg-green-500 text-white px-5 py-2 rounded hover:bg-green-700"
      >
        + Increment
      </button>
    </div>
  );
}