# ==============================================================================
#                      NEXT.JS EXAM PREPARATION STUDY GUIDE
#                   COURSE: WEB APPLICATION FRAMEWORKS (WAF)
# ==============================================================================

"""
================================================================================
UNIT 1: INTRODUCTION TO NEXT.JS & DEVELOPMENT ENVIRONMENT
================================================================================

1. INTRODUCTION & KEY FEATURES OF NEXT.JS
----------------------------------------
Next.js is a full-stack React framework developed by Vercel that enables server-side 
rendering, static site generation, and powerful optimizations out of the box.

Key Features & Advantages:
- Hybrid Rendering: Supports SSR, SSG, ISR, and CSR per-route.
- App Router: File-system based router supporting layouts, loading UI, and error boundaries.
- Built-in Optimizations: Automatic image, font, and script optimization.
- Server Components (RSC): Zero-bundle-size React components rendered on the server.
- Full-Stack Capabilities: API routes / Server Actions to handle backend logic.


2. TYPESCRIPT IN NEXT.JS
-----------------------
TypeScript provides static typing for Next.js applications, improving developer 
experience and catch errors at compile time.

Basic Types & Annotations:
  - Primitives: string, number, boolean
  - Collections: Array<T>, [T, U] (tuples)
  - Functions: (param: Type) => ReturnType

Interfaces vs Types:
  - Interfaces are ideal for defining object shapes and props contracts.
  - Types are better for unions, intersections, and primitive aliases.

Props Typing Example:
  interface UserCardProps {
    name: string;
    age: number;
    isAdmin?: boolean; // Optional property
  }


3. NEXT.JS PROJECT STRUCTURE (.app Directory Architecture)
-----------------------------------------------------------
my-next-app/
├── app/                  # App Router directory (Routes & UI)
│   ├── layout.tsx        # Root layout (Required)
│   ├── page.tsx          # Homepage UI (/)
│   ├── globals.css       # Global styles
│   └── dashboard/        # Sub-route (/dashboard)
│       └── page.tsx      # Dashboard page UI
├── components/           # Reusable UI components (buttons, cards)
├── lib/                  # Helper utilities, database clients, API wrappers
├── utils/                # Utility/helper functions (formatting, validation)
├── public/               # Static assets (images, favicon, fonts)
├── .env.local            # Environment variables (secrets)
├── next.config.mjs       # Next.js configuration settings
├── package.json          # Project dependencies and scripts
└── tsconfig.json         # TypeScript configuration


4. ENVIRONMENT VARIABLES (.env)
-------------------------------
- Server-Only Variables:
  DATABASE_URL="postgresql://user:pass@localhost:5432/db"
  (Accessible ONLY on the server side via process.env.DATABASE_URL)

- Client-Exposed Variables:
  NEXT_PUBLIC_API_URL="https://api.example.com"
  (Must be prefixed with `NEXT_PUBLIC_` to be accessible in browser/client components)


--------------------------------------------------------------------------------
HIGH-PROBABILITY CODE EXAMPLES (UNIT 1)
--------------------------------------------------------------------------------

Example 1.1: TypeScript Component with Typed Props
"""


# Definition of TypeScript Component
def typescript_component_code():
    return """
// components/UserCard.tsx
import React from 'react';

interface UserCardProps {
  id: number;
  name: string;
  email: string;
  role?: 'admin' | 'user';
}

export default function UserCard({ id, name, email, role = 'user' }: UserCardProps) {
  return (
    <div className="p-4 border rounded-md">
      <h2>{name} ({role})</h2>
      <p>ID: {id}</p>
      <p>Email: {email}</p>
    </div>
  );
}
"""


"""
================================================================================
UNIT 1: IMPORTANT MCQ & CONCEPTUAL POINTS
================================================================================

1. TypeScript Variable Inference:
   - Code: `let x = "Next.js";` -> The variable is inferred as string.

2. Accessing Environment Variables:
   - Server-side access: `process.env.DB_PASS`
   - Client-side access: `process.env.NEXT_PUBLIC_ANALYTICS_ID`

3. Essential App Router Files:
   - `layout.tsx` is MANDATORY inside the root `app/` folder.
   - `page.tsx` makes a route publicly accessible.

4. Public Asset Pathing:
   - Files inside `public/logo.png` are referenced directly as `/logo.png`.
"""


"""
================================================================================
UNIT 2: ROUTING, RENDERING & PERFORMANCE IN NEXT.JS
================================================================================

1. FILE-BASED ROUTING & APP ROUTER
----------------------------------
Next.js uses a file-system based router where folders define routes.

Special File Conventions:
- `page.tsx`      : Unique UI for a route.
- `layout.tsx`    : Shared UI across multiple routes (persists state, doesn't re-render).
- `loading.tsx`   : Instant loading state wrapped in React Suspense.
- `error.tsx`     : Error boundary UI for catch-all handling (Must be a Client Component).
- `not-found.tsx` : UI for 404 pages.

Folder Special Conventions:
- Route Groups `(groupName)` : Organize routes without affecting URL path.
- Dynamic Routes `[id]`      : Matches single dynamic parameter (`/posts/1`).
- Catch-all `[...slug]`     : Matches nested dynamic paths (`/docs/a/b/c`).


2. RENDERING STRATEGIES (COMPARISON TABLE)
-----------------------------------------
+-------------------+-----------------------------------+------------------------------------+
| Rendering Mode    | When HTML is Generated             | Primary Use Case                   |
+-------------------+-----------------------------------+------------------------------------+
| CSR (Client)      | In Browser via JS                 | Interactive dashboards             |
| SSG (Static)      | At Build Time                     | Blogs, marketing pages, docs       |
| SSR (Server)      | On Every Incoming Request         | Dynamic feeds, personalized pages  |
| ISR (Revalidated) | At Build Time + Background Sync   | E-commerce catalogs, news portals  |
+-------------------+-----------------------------------+------------------------------------+


3. RENDERING FLOW CHART
-----------------------
[ User Request ]
       |
       +---> [ Static Asset in CDN? ] ---> (Yes) ---> [ Serve Cached SSG HTML ]
       |
       +---> [ Dynamic Route? ] ---------> (Yes) ---> [ Execute SSR on Server ] ---> [ Return HTML + Hydrate ]
       |
       +---> [ ISR Expiration Passed? ] -> (Yes) ---> [ Serve Stale HTML ] + [ Revalidate in Background ]


4. SERVER VS CLIENT COMPONENTS
------------------------------
- Server Components (Default):
  - Executed ONLY on the server.
  - Zero JavaScript added to client bundle.
  - Can directly access backend (DB, file system).
  - Cannot use React hooks (`useState`, `useEffect`) or browser APIs.

- Client Components:
  - Opted in using `"use client"` directive at top of file.
  - Executed on client (and pre-rendered on server).
  - Can use hooks (`useState`, `useEffect`), event listeners (`onClick`).


5. DATA FETCHING, CACHING & REVALIDATION
----------------------------------------
Next.js extends `fetch` to configure caching & revalidation behavior:

- Static Data Fetch (SSG behavior):
  fetch('https://api.com/data', { cache: 'force-cache' })

- Dynamic Data Fetch (SSR behavior):
  fetch('https://api.com/data', { cache: 'no-store' })

- Time-based Revalidation (ISR behavior):
  fetch('https://api.com/data', { next: { revalidate: 60 } })


--------------------------------------------------------------------------------
HIGH-PROBABILITY CODE EXAMPLES (UNIT 2)
--------------------------------------------------------------------------------

Example 2.1: Dynamic Route Page with Data Fetching (SSR/ISR)
"""


def dynamic_route_code():
    return """
// app/products/[id]/page.tsx

interface PageProps {
  params: {
    id: string;
  };
}

async function getProduct(id: string) {
  // ISR: Revalidate every 60 seconds
  const res = await fetch(`https://api.example.com/products/${id}`, {
    next: { revalidate: 60 }
  });
  
  if (!res.ok) throw new Error('Failed to fetch product');
  return res.json();
}

export default async function ProductPage({ params }: PageProps) {
  const product = await getProduct(params.id);

  return (
    <main className="p-6">
      <h1 className="text-2xl font-bold">{product.title}</h1>
      <p className="text-gray-600">${product.price}</p>
    </main>
  );
}
"""


"""
Example 2.2: Interactive Client Component ("use client")
"""


def client_component_code():
    return """
// components/Counter.tsx
"use client";

import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState<number>(0);

  return (
    <div className="flex gap-4 items-center">
      <button 
        onClick={() => setCount(count - 1)}
        className="px-4 py-2 bg-red-500 text-white rounded"
      >
        Decrement
      </button>
      <span>Count: {count}</span>
      <button 
        onClick={() => setCount(count + 1)}
        className="px-4 py-2 bg-green-500 text-white rounded"
      >
        Increment
      </button>
    </div>
  );
}
"""


"""
Example 2.3: Error Boundary File (error.tsx)
"""


def error_boundary_code():
    return """
// app/error.tsx
"use client"; // Error components MUST be Client Components

import { useEffect } from 'react';

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <div className="p-8 text-center">
      <h2 className="text-red-600 font-bold">Something went wrong!</h2>
      <button
        onClick={() => reset()}
        className="mt-4 px-4 py-2 bg-blue-600 text-white rounded"
      >
        Try again
      </button>
    </div>
  );
}
"""


"""
================================================================================
UNIT 2: IMPORTANT MCQ & CONCEPTUAL POINTS
================================================================================

1. Purpose of `"use client"`:
   - Mandatory when using React hooks (`useState`, `useEffect`) or browser event handlers.

2. Route Groups Syntax:
   - Folders named with parentheses like `(marketing)` group routes without adding extra segment to URL.

3. Static Site Generation (SSG) Data Cache:
   - Uses `cache: 'force-cache'` in fetch request options.

4. Server-Side Rendering (SSR) Behavior:
   - HTML is generated dynamically for every single incoming request (`cache: 'no-store'`).

5. Incremental Static Regeneration (ISR):
   - Served from cache while stale, regenerated asynchronously in the background once revalidate interval expires.
"""


# ==============================================================================
#                      EXAM PRACTICE QUESTION SET
# ==============================================================================

"""
--------------------------------------------------------------------------------
SECTION A: 4 MARKS QUESTIONS (THEORETICAL + CODING) [4 QUESTIONS]
--------------------------------------------------------------------------------

Q1: Explain the differences between Server Components and Client Components in Next.js App Router.
    Provide code snippets for both.
Answer:
- Server Components:
  Render exclusively on the server. Reduced bundle size, secure database access, zero JS sent for execution.
  Cannot handle interactivity, state, or hooks.
- Client Components:
  Opted into using "use client" directive. Can use state, hooks, click listeners, browser APIs.
  Pre-rendered on server for HTML skeleton, then hydrated on client.

Code:
// Server Component (app/page.tsx)
export default async function Page() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
  return <div>Data: {data.title}</div>;
}

// Client Component (components/Button.tsx)
"use client";
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>Count: {count}</button>;
}


Q2: Compare SSR, SSG, and ISR rendering strategies with their data fetching configurations in Next.js.
Answer:
1. Static Site Generation (SSG):
   - HTML rendered at build time. Ideal for static/infrequent updates.
   - Code: fetch(URL, { cache: 'force-cache' })

2. Server-Side Rendering (SSR):
   - HTML rendered on every request. Ideal for real-time/personalized data.
   - Code: fetch(URL, { cache: 'no-store' })

3. Incremental Static Regeneration (ISR):
   - Re-builds static pages in the background after set interval.
   - Code: fetch(URL, { next: { revalidate: 10 } })


Q3: Explain Special File Conventions in Next.js App Router and show how nested layout routing works.
Answer:
Special Files:
- layout.tsx: Shared wrap layout for routes.
- page.tsx: Main UI file for route segment.
- loading.tsx: Suspense fallback container.
- error.tsx: Error boundary wrapper ("use client").

Nested Layout Structure:
Root Layout (`app/layout.tsx`) wraps Dashboard Layout (`app/dashboard/layout.tsx`),
which wraps Dashboard Page (`app/dashboard/page.tsx`).

Code:
// app/dashboard/layout.tsx
export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <section className="flex">
      <aside>Sidebar Navigation</aside>
      <main>{children}</main>
    </section>
  );
}


Q4: Define TypeScript Interfaces and Props Typing in Next.js. Create a component that receives
    an array of product objects as props and displays them.
Answer:
Interfaces define data structure contracts to enforce type safety in React props.

Code:
interface Product {
  id: number;
  title: string;
  price: number;
}

interface ProductListProps {
  products: Product[];
}

export default function ProductList({ products }: ProductListProps) {
  return (
    <ul>
      {products.map((item) => (
        <li key={item.id}>{item.title} - ${item.price}</li>
      ))}
    </ul>
  );
}


--------------------------------------------------------------------------------
SECTION B: 2 MARKS QUESTIONS (MCQS & OUTPUT PREDICTION) [4 QUESTIONS]
--------------------------------------------------------------------------------

Q1: What will be the output/behavior of the following fetch request?
    fetch('https://api.com/user', { cache: 'no-store' });
    (A) The request is cached permanently at build time.
    (B) HTML is generated dynamically on every incoming request.
    (C) The request revalidates every 60 seconds.
    (D) The component will throw a compile-time error.
Answer: (B) HTML is generated dynamically on every incoming request.


Q2: What happens when a user requests an ISR page whose revalidate time has expired?
    (A) The server returns a 404 error page.
    (B) The request blocks until the page is fully regenerated.
    (C) The cached (stale) page is served immediately, while revalidation runs in the background.
    (D) The site falls back to Client-Side Rendering completely.
Answer: (C) The cached (stale) page is served immediately, while revalidation runs in the background.


Q3: Predict the output/error of the following Next.js code snippet:
    // app/counter/page.tsx
    import { useState } from 'react';
    export default function Page() {
      const [val, setVal] = useState(0);
      return <button onClick={() => setVal(val + 1)}>{val}</button>;
    }
    (A) Renders a working counter button.
    (B) Throws an error because useState works only in Client Components ("use client" missing).
    (C) Converts automatically to static HTML.
    (D) Renders on server without hydration.
Answer: (B) Throws an error because useState works only in Client Components ("use client" missing).


Q4: Given the folder structure `app/docs/[...slug]/page.tsx`, which path will NOT be matched?
    (A) /docs/setup
    (B) /docs/setup/installation
    (C) /docs/setup/installation/nextjs
    (D) /docs
Answer: (D) /docs (Optional catch-all [[...slug]] is needed to match base path /docs).


--------------------------------------------------------------------------------
SECTION C: 1 MARK QUESTIONS (MCQS) [16 QUESTIONS]
--------------------------------------------------------------------------------

1. Which directory is used for the modern App Router in Next.js?
   (A) pages/          (B) app/             (C) routes/          (D) src/router/
   Answer: (B)

2. What is the default component type in the Next.js App Router?
   (A) Client Component(B) Server Component(C) Pure Component  (D) Class Component
   Answer: (B)

3. Which directive makes a Server Component into a Client Component?
   (A) "use server"    (B) "use client"     (C) "client-only"    (D) "use react"
   Answer: (B)

4. Which file convention handles 404 UI in the App Router?
   (A) 404.tsx         (B) error.tsx        (C) not-found.tsx    (D) missing.tsx
   Answer: (C)

5. How do you expose an environment variable to the client browser?
   (A) Prefix NEXT_APP_  (B) Prefix CLIENT_ (C) Prefix NEXT_PUBLIC_ (D) Add export
   Answer: (C)

6. Which file wraps page components and preserves state across navigations?
   (A) page.tsx        (B) layout.tsx       (C) template.tsx     (D) loading.tsx
   Answer: (B)

7. What folder naming convention creates a Route Group without modifying the URL?
   (A) [folderName]    (B) (folderName)     (C) _folderName      (D) {folderName}
   Answer: (B)

8. What default fetch caching strategy mimics Static Site Generation (SSG)?
   (A) cache: 'no-store'                    (B) cache: 'force-cache'
   (C) revalidate: 0                        (D) cache: 'reload'
   Answer: (B)

9. Which file acts as an automatic React Suspense boundary for loading states?
   (A) spinner.tsx     (B) layout.tsx       (C) loading.tsx      (D) error.tsx
   Answer: (C)

10. Must an `error.tsx` file be a Client Component?
    (A) Yes            (B) No               (C) Only in production (D) Only in development
    Answer: (A)

11. What TS type annotation indicates an optional interface property?
    (A) prop!: string   (B) prop?: string    (C) prop: optional   (D) prop|null
    Answer: (B)

12. Static assets placed in `public/avatar.png` can be accessed in browser via:
    (A) /public/avatar.png                   (B) /avatar.png
    (C) ./assets/avatar.png                  (D) /assets/public/avatar.png
    Answer: (B)

13. What is the function of `revalidate` option in fetch requests?
    (A) Triggers server restart             (B) Re-fetches data after specified seconds (ISR)
    (C) Clears browser localStorage          (D) Cancels API call if slow
    Answer: (B)

14. Dynamic dynamic routes `app/blog/[id]/page.tsx` pass route parameters via:
    (A) props.query     (B) props.params     (C) props.router     (D) props.path
    Answer: (B)

15. What package manager command installs Next.js dependencies?
    (A) npm start       (B) npm run build    (C) npm install      (D) npm compile
    Answer: (C)

16. Which framework features pre-rendering of pages out of the box?
    (A) Express.js      (B) Plain React SPA  (C) Next.js          (D) Node.js
    Answer: (C)
"""

if __name__ == "__main__":
    print("Next.js WAF Syllabus Exam Preparation Notes Successfully Executed.")