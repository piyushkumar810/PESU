# =============================================================================
# WAF (WEB APPLICATION FRAMEWORKS) - NEXT.JS
# EXAM-ORIENTED COMPLETE REVISION NOTES
# Units 1 & 2 | 4 x 4 marks + 4 x 2 marks + 16 x 1 marks
# =============================================================================

"""
HOW TO USE THIS FILE
--------------------
1. Read the THEORY blocks first.
2. Memorize the FLOW / TREE / DIFFERENCE tables.
3. Run the small code examples to understand output.
4. Revise the "MCQ POINTS" after every topic.
5. The final section contains a probable exam-oriented question set.

IMPORTANT:
- Next.js examples below use the modern App Router (app/ directory).
- TypeScript is used because it is part of the syllabus.
"""

# =============================================================================
# UNIT 1 - INTRODUCTION TO NEXT.JS + DEVELOPMENT ENVIRONMENT
# =============================================================================

# -----------------------------------------------------------------------------
# 1. WHAT IS NEXT.JS?
# -----------------------------------------------------------------------------

"""
WHAT IS NEXT.JS?
----------------
Next.js is a React-based full-stack web framework used to build modern
web applications.

React -> UI library
Next.js -> Framework built around React

Next.js provides features such as:
- File-based routing
- Server Components
- Client Components
- SSR, SSG, ISR and CSR
- Layouts
- Data fetching
- Image/font optimization
- Error and loading handling
- API/backend capabilities
- Production optimization

EXAM DEFINITION:
"Next.js is a React framework for building full-stack web applications
with built-in routing, rendering, data fetching and performance features."
"""

# -----------------------------------------------------------------------------
# 2. WHY NEXT.JS? KEY FEATURES
# -----------------------------------------------------------------------------

"""
IMPORTANT FEATURES
------------------
1. File-based routing
   Files/folders inside app/ automatically represent routes.

2. Server Components
   Components can execute on the server by default in App Router.

3. Client Components
   Use "use client" when browser-side interactivity/state is required.

4. Multiple rendering strategies
   CSR, SSR, SSG and ISR can be used.

5. Layouts
   Shared UI can be maintained using layout.tsx.

6. Dynamic routing
   Example: app/blog/[id]/page.tsx

7. Loading and error handling
   loading.tsx and error.tsx provide route-level handling.

8. Performance optimization
   Automatic optimizations for images, fonts, code splitting etc.

9. TypeScript support
   Next.js works well with TypeScript.

10. Full-stack capability
    Frontend UI + server-side logic can exist in one application.
"""

# MCQ POINTS
"""
- Next.js is built on React.
- Next.js is a FRAMEWORK, React is primarily a UI LIBRARY.
- App Router uses the app/ directory.
- In App Router, components are Server Components by default.
- "use client" makes a component a Client Component.
- File/folder structure is important for routing.
"""

# -----------------------------------------------------------------------------
# 3. NODE.JS AND NPM BASICS
# -----------------------------------------------------------------------------

"""
NODE.JS
-------
Node.js allows JavaScript to run outside the browser.

NPM
---
NPM = Node Package Manager.
It is used to:
- install packages
- manage dependencies
- run scripts

COMMON COMMANDS
---------------
node -v
npm -v
npm install package-name
npm install
npm run dev
npm run build
npm start
"""

# Example commands:
# node -v
# npm -v
# npm install axios
# npm install
# npm run dev

"""
EXAM TIP:
npm install -> installs dependencies
npm run dev -> starts development server
npm run build -> creates production build
npm start -> starts production server after build
"""

# MCQ POINTS
"""
- package.json stores project metadata, scripts and dependencies.
- node_modules contains installed packages.
- package-lock.json locks dependency versions.
- npm is NOT a programming language.
"""

# -----------------------------------------------------------------------------
# 4. CREATE A NEXT.JS APPLICATION
# -----------------------------------------------------------------------------

"""
COMMON COMMAND
--------------
npx create-next-app@latest my-app

Then:
cd my-app
npm run dev

Default development URL:
http://localhost:3000

FLOW
----
create-next-app
      |
      v
Next.js project created
      |
      v
cd my-app
      |
      v
npm run dev
      |
      v
Development server
      |
      v
localhost:3000
"""

# -----------------------------------------------------------------------------
# 5. IMPORTANT NEXT.JS PROJECT STRUCTURE
# -----------------------------------------------------------------------------

"""
PROJECT TREE
------------
my-app/
|
|-- app/
|   |-- layout.tsx
|   |-- page.tsx
|   |-- globals.css
|   |-- loading.tsx
|   |-- error.tsx
|   |-- not-found.tsx
|
|-- components/
|   |-- Navbar.tsx
|   |-- Button.tsx
|
|-- lib/
|   |-- db.ts
|   |-- api.ts
|
|-- utils/
|   |-- formatDate.ts
|
|-- public/
|   |-- logo.png
|
|-- .env.local
|-- package.json
|-- tsconfig.json
|-- next.config.ts
"""

"""
IMPORTANT FOLDERS
-----------------
app/
    Main App Router. Pages, layouts, routes and route-level files.

components/
    Reusable UI components.

lib/
    Shared application logic such as database/API helper functions.

utils/
    Small reusable utility/helper functions.

public/
    Static assets. Example: images, icons.

.env.local
    Environment variables used locally.

package.json
    Dependencies and scripts.

next.config.ts
    Next.js configuration.
"""

# MCQ POINTS
"""
- page.tsx defines a route's UI.
- layout.tsx defines shared UI around child routes.
- public/ contains static assets.
- app/ is the main App Router directory.
- components/ is a convention for reusable components, not a mandatory
  Next.js routing directory.
"""

# -----------------------------------------------------------------------------
# 6. FILE-BASED ROUTING
# -----------------------------------------------------------------------------

"""
FILE-BASED ROUTING
------------------
In App Router, folders define URL segments and page.tsx defines the page.

TREE:

app/
|
|-- page.tsx                -> /
|
|-- about/
|   |-- page.tsx            -> /about
|
|-- products/
|   |-- page.tsx            -> /products
|
|-- contact/
|   |-- page.tsx            -> /contact

EXAM RULE:
folder name = URL segment
page.tsx   = route page
"""

# Example:
# app/about/page.tsx
"""
export default function About() {
    return <h1>About Page</h1>;
}
"""

# MCQ POINTS
"""
- app/page.tsx -> /
- app/about/page.tsx -> /about
- app/products/page.tsx -> /products
- page.tsx is required to make a folder a page route.
"""

# -----------------------------------------------------------------------------
# 7. TYPESCRIPT BASICS
# -----------------------------------------------------------------------------

"""
WHY TYPESCRIPT?
---------------
TypeScript = JavaScript + static type checking.

It helps detect type errors before runtime.

BASIC TYPES
-----------
string
number
boolean
array
object
any
unknown
null
undefined

TYPE ANNOTATION
---------------
let name: string = "Piyush";
let age: number = 23;
let active: boolean = true;
"""

# -----------------------------------------------------------------------------
# 8. TYPESCRIPT INTERFACE
# -----------------------------------------------------------------------------

"""
INTERFACE
---------
An interface defines the shape/structure of an object.

Example:
"""

interface User {
    name: string
    age: number
}

# Example usage:
# const user: User = {
#     name: "Piyush",
#     age: 23
# }

"""
If age is assigned a string instead of number, TypeScript reports a type error.

EXAM DEFINITION:
"An interface defines the structure and expected types of an object."
"""

# MCQ POINTS
"""
- string -> text
- number -> numeric values
- boolean -> true/false
- interface -> describes object structure
- TypeScript errors can be detected during development/type checking.
"""

# -----------------------------------------------------------------------------
# 9. PROPS TYPING IN TYPESCRIPT
# -----------------------------------------------------------------------------

"""
PROPS
-----
Props are values passed from a parent component to a child component.

Example:
"""

# This is valid Next.js/React TypeScript syntax:
"""
type UserProps = {
    name: string;
    age: number;
};

export default function UserCard({ name, age }: UserProps) {
    return (
        <div>
            <h2>{name}</h2>
            <p>{age}</p>
        </div>
    );
}
"""

"""
FLOW
----
Parent
  |
  | props
  v
Child Component
  |
  v
Rendered UI
"""

# MCQ POINTS
"""
- Props are used to pass data from parent to child.
- Props should be typed in TypeScript.
- Type mismatch in props is caught by TypeScript.
"""

# -----------------------------------------------------------------------------
# 10. ENVIRONMENT VARIABLES
# -----------------------------------------------------------------------------

"""
ENVIRONMENT VARIABLES
---------------------
Used to store configuration values outside source code.

Example .env.local:
"""

# NEXT_PUBLIC_API_URL=https://example.com/api
# DATABASE_URL=your_database_url

"""
IMPORTANT:
- Variables beginning with NEXT_PUBLIC_ can be exposed to browser/client code.
- Server-only secrets should NOT use NEXT_PUBLIC_.
- .env.local is commonly used for local environment configuration.

FLOW
----
.env.local
    |
    v
Next.js reads environment variable
    |
    v
Server/client code uses it according to visibility rules
"""

# Example:
"""
const api = process.env.NEXT_PUBLIC_API_URL;
"""

# MCQ POINTS
"""
- NEXT_PUBLIC_ variables can be exposed to the browser.
- Never put secret keys in client-exposed environment variables.
- .env.local is commonly used for local development.
"""

# -----------------------------------------------------------------------------
# 11. MODULAR ARCHITECTURE
# -----------------------------------------------------------------------------

"""
MODULAR ARCHITECTURE
--------------------
Divide a large application into small reusable modules.

Example:
app/
components/
lib/
utils/

BENEFITS:
- Reusability
- Maintainability
- Easy testing
- Separation of concerns
- Easier debugging

FLOW:
Page -> Component -> Utility/Library -> API/Database
"""

# MCQ POINTS
"""
- Modular architecture reduces code duplication.
- Components should generally focus on UI.
- Utility functions can hold reusable logic.
"""

# =============================================================================
# UNIT 2 - ROUTING, RENDERING AND PERFORMANCE
# =============================================================================

# -----------------------------------------------------------------------------
# 12. APP ROUTER ARCHITECTURE
# -----------------------------------------------------------------------------

"""
APP ROUTER
----------
The App Router uses the app/ directory and supports:
- Nested routes
- Layouts
- Loading UI
- Error UI
- Dynamic routes
- Server Components
- Client Components

TREE:
app/
|
|-- layout.tsx
|-- page.tsx
|
|-- products/
|   |-- page.tsx
|   |
|   |-- [id]/
|       |-- page.tsx
|
|-- blog/
|   |-- [id]/
|       |-- page.tsx
"""

# -----------------------------------------------------------------------------
# 13. LAYOUTS
# -----------------------------------------------------------------------------

"""
LAYOUT
------
A layout is shared UI that wraps child pages.

Example:
app/layout.tsx
"""

"""
export default function RootLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <html lang="en">
            <body>
                <nav>Navbar</nav>
                {children}
                <footer>Footer</footer>
            </body>
        </html>
    );
}
"""

"""
TREE
----
RootLayout
    |
    +-- Navbar
    |
    +-- Page Content
    |
    +-- Footer

IMPORTANT:
A layout persists across navigation for its segment and is useful for
shared UI such as Navbar, Sidebar and Footer.
"""

# MCQ POINTS
"""
- layout.tsx is used for shared UI.
- children represents the nested page/content.
- Root layout is normally app/layout.tsx.
"""

# -----------------------------------------------------------------------------
# 14. ROUTE GROUPS
# -----------------------------------------------------------------------------

"""
ROUTE GROUP
-----------
Folders inside parentheses are route groups.

Example:
app/
|
|-- (auth)/
|   |-- login/
|   |   |-- page.tsx
|   |
|   |-- register/
|       |-- page.tsx

URLs:
login    -> /login
register -> /register

(auth) DOES NOT appear in URL.

USE:
Organize routes without changing URL structure.
"""

# MCQ POINTS
"""
- (group) is a route group.
- Route-group name does not become part of URL.
"""

# -----------------------------------------------------------------------------
# 15. DYNAMIC ROUTING
# -----------------------------------------------------------------------------

"""
DYNAMIC ROUTE
-------------
Use [parameter] for dynamic URL segments.

Example:
app/blog/[id]/page.tsx

/blog/10
/blog/25
/blog/abc

All can match the same dynamic route.

CODE:
"""

"""
export default async function BlogPost({
    params,
}: {
    params: Promise<{ id: string }>
}) {
    const { id } = await params;
    return <h1>Post ID: {id}</h1>;
}
"""

"""
CONCEPT:
[id] = dynamic segment
id = value taken from URL
"""

# MCQ POINTS
"""
- [id] -> dynamic segment.
- /blog/5 gives id = "5".
- Dynamic parameter is normally a string from the URL.
"""

# -----------------------------------------------------------------------------
# 16. NESTED DYNAMIC ROUTING
# -----------------------------------------------------------------------------

"""
TREE
----
app/
|
|-- products/
    |
    |-- [category]/
        |
        |-- [id]/
            |
            |-- page.tsx

URL:
 /products/electronics/101

category = electronics
id       = 101
"""

"""
CODE IDEA:
export default async function Product({
    params
}: {
    params: Promise<{ category: string; id: string }>
}) {
    const { category, id } = await params;
    return <h1>{category} - {id}</h1>;
}
"""

# -----------------------------------------------------------------------------
# 17. CATCH-ALL ROUTES
# -----------------------------------------------------------------------------

"""
Catch-all:
app/docs/[...slug]/page.tsx

Matches:
 /docs/a
 /docs/a/b
 /docs/a/b/c

Optional catch-all:
app/docs/[[...slug]]/page.tsx

Can also match:
 /docs

EXAM TIP:
[...slug] -> one or more segments
[[...slug]] -> zero or more segments
"""

# -----------------------------------------------------------------------------
# 18. LOADING UI
# -----------------------------------------------------------------------------

"""
loading.tsx
-----------
Shows loading UI while a route segment is loading.

TREE:
app/products/
|
|-- page.tsx
|-- loading.tsx

The loading UI is automatically used by Next.js for that segment.
"""

"""
EXAM:
loading.tsx -> loading state
not-found.tsx -> not-found UI
error.tsx -> error UI
"""

# MCQ POINTS
"""
- loading.tsx is for loading UI.
- not-found.tsx is for not-found UI.
- error.tsx handles errors for a route segment.
"""

# -----------------------------------------------------------------------------
# 19. NOT FOUND
# -----------------------------------------------------------------------------

"""
not-found.tsx
-------------
Used to display a custom 404/not-found UI.

You can also call notFound() from next/navigation.

Example:
"""

"""
import { notFound } from "next/navigation";

export default async function Page() {
    const product = null;

    if (!product) {
        notFound();
    }

    return <div>Product</div>;
}
"""

# -----------------------------------------------------------------------------
# 20. ERROR HANDLING
# -----------------------------------------------------------------------------

"""
error.tsx
---------
Used for route-level error UI.

Important:
- error.tsx is a Client Component.
- It can receive error and reset.
"""

"""
'use client';

export default function Error({
    error,
    reset,
}: {
    error: Error & { digest?: string };
    reset: () => void;
}) {
    return (
        <div>
            <h2>Something went wrong!</h2>
            <button onClick={() => reset()}>
                Try again
            </button>
        </div>
    );
}
"""

# MCQ POINTS
"""
- error.tsx must be a Client Component.
- reset() can retry/recover the segment.
- not-found and error handling are different concepts.
"""

# -----------------------------------------------------------------------------
# 21. SERVER COMPONENTS VS CLIENT COMPONENTS
# -----------------------------------------------------------------------------

"""
SERVER COMPONENT
----------------
In App Router, components are Server Components by default.

Good for:
- Fetching data on server
- Database access
- Keeping secrets on server
- Reducing client-side JavaScript

CLIENT COMPONENT
----------------
Add:
'use client';

Needed when component uses:
- useState
- useEffect
- event handlers such as onClick
- browser APIs
- interactive UI

FLOW:
Server Component
      |
      | renders / fetches data
      v
HTML / RSC payload
      |
      v
Browser

Client Component
      |
      | JavaScript + hydration
      v
Interactive browser UI
"""

# MCQ POINTS
"""
- App Router default = Server Component.
- "use client" = Client Component.
- useState/useEffect normally require Client Component.
- Database credentials should stay on the server.
"""

# -----------------------------------------------------------------------------
# 22. CSR - CLIENT-SIDE RENDERING
# -----------------------------------------------------------------------------

"""
CSR = Client-Side Rendering

FLOW:
Browser
  |
  | request
  v
Server sends HTML/JS
  |
  v
Browser downloads JS
  |
  v
React executes in browser
  |
  v
Data fetched / UI rendered
  |
  v
User sees final UI

BEST FOR:
- Highly interactive dashboards
- User-specific browser interactions
- Applications where SEO is less important

ADVANTAGE:
Interactive experience after JavaScript loads.

DISADVANTAGE:
Initial page can depend heavily on JavaScript loading.
"""

# Example CSR component:
"""
'use client';

import { useEffect, useState } from 'react';

export default function Products() {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        fetch('https://fakestoreapi.com/products')
            .then(res => res.json())
            .then(data => setProducts(data));
    }, []);

    return <div>{products.length} products</div>;
}
"""

# -----------------------------------------------------------------------------
# 23. SSR - SERVER-SIDE RENDERING
# -----------------------------------------------------------------------------

"""
SSR = Server-Side Rendering

The page is rendered on the server for a request.

FLOW:
Browser
   |
   | HTTP request
   v
Server
   |
   | fetch latest data
   v
Render HTML
   |
   v
Browser receives HTML
   |
   v
Hydration/interactivity where needed

USE:
- Frequently changing data
- Request-dependent data
- SEO-friendly pages

KEY IDEA:
Render happens on the SERVER at request time.
"""

# -----------------------------------------------------------------------------
# 24. SSG - STATIC SITE GENERATION
# -----------------------------------------------------------------------------

"""
SSG = Static Site Generation

The page is generated ahead of time/build time and can be served as
static content.

FLOW:
Build time
   |
   v
Fetch data
   |
   v
Generate HTML
   |
   v
Static output
   |
   v
User request
   |
   v
Serve static page

USE:
- Blogs
- Documentation
- Marketing pages
- Content that changes infrequently

KEY IDEA:
Generate ahead of the request.
"""

# -----------------------------------------------------------------------------
# 25. ISR - INCREMENTAL STATIC REGENERATION
# -----------------------------------------------------------------------------

"""
ISR = Incremental Static Regeneration

ISR combines static generation with periodic/on-demand revalidation.

FLOW:
Build
 |
 v
Static page
 |
 v
User request
 |
 v
Serve cached/static page
 |
 | after revalidation period
 v
Regenerate updated content
 |
 v
Future users receive updated page

Example:
"""

"""
export default async function Page() {
    const res = await fetch(
        'https://api.example.com/products',
        { next: { revalidate: 60 } }
    );

    const data = await res.json();

    return <pre>{JSON.stringify(data, null, 2)}</pre>;
}
"""

"""
revalidate: 60
--------------
The cached data can be revalidated after 60 seconds.

IMPORTANT:
ISR reduces the need to rebuild the entire application for every content
change.
"""

# -----------------------------------------------------------------------------
# 26. CSR vs SSR vs SSG vs ISR - MUST MEMORIZE
# -----------------------------------------------------------------------------

"""
| Method | Rendering Time | Data Freshness | SEO | Typical Use |
|--------|-----------------|----------------|-----|-------------|
| CSR    | Browser         | Can be dynamic  | Lower initial SEO | Dashboards |
| SSR    | Request/server  | Fresh per request | Good | Dynamic pages |
| SSG    | Build time      | Static          | Excellent | Blogs/docs |
| ISR    | Static + revalidation | Periodically updated | Excellent | Product/content sites |

MEMORY TRICK:
CSR = Client
SSR = Server at Request
SSG = Static at Build
ISR = Static + Revalidate
"""

"""
ONE-LINE DIFFERENCE:
CSR -> browser renders
SSR -> server renders per request
SSG -> build generates static page
ISR -> static page + later regeneration
"""

# MCQ POINTS
"""
- SSR = request-time rendering.
- SSG = build-time generation.
- ISR = static generation with revalidation.
- CSR = browser-side rendering.
- SEO generally benefits from server/static HTML.
"""

# -----------------------------------------------------------------------------
# 27. SSR vs SSG - EXAM COMPARISON
# -----------------------------------------------------------------------------

"""
| Feature | SSR | SSG |
|---------|-----|-----|
| Rendering | Request time | Build time |
| Data | Fresh per request | Build-time data |
| Speed | Usually slower than static | Very fast |
| Dynamic data | Suitable | Less suitable |
| Server work | Every request | Mainly during build |
| SEO | Good | Good |
"""

# -----------------------------------------------------------------------------
# 28. SSR vs ISR
# -----------------------------------------------------------------------------

"""
| Feature | SSR | ISR |
|---------|-----|-----|
| Rendering | Per request | Static + revalidation |
| Freshness | Very high | Periodic/on-demand |
| Performance | More server work | Often faster |
| Use | Highly dynamic | Frequently updated content |
"""

# -----------------------------------------------------------------------------
# 29. DATA FETCHING USING FETCH
# -----------------------------------------------------------------------------

"""
Server Component data fetching:

"""

"""
export default async function Products() {
    const response = await fetch(
        'https://fakestoreapi.com/products'
    );

    const products = await response.json();

    return (
        <div>
            {products.map((product: any) => (
                <p key={product.id}>{product.title}</p>
            ))}
        </div>
    );
}
"""

"""
IMPORTANT FLOW
--------------
Component
   |
   v
fetch(API)
   |
   v
response.json()
   |
   v
data
   |
   v
map()
   |
   v
UI
"""

# -----------------------------------------------------------------------------
# 30. CACHE AND REVALIDATION
# -----------------------------------------------------------------------------

"""
Caching:
-------
Caching avoids repeatedly obtaining the same data when appropriate.

Revalidation:
-------------
Revalidation means updating cached data after a specified period or
through an explicit mechanism.

Example:
fetch(url, { next: { revalidate: 60 } })

Meaning:
Data may be revalidated after 60 seconds.
"""

# -----------------------------------------------------------------------------
# 31. SWR - IMPORTANT CONCEPT
# -----------------------------------------------------------------------------

"""
SWR
---
SWR is a React data-fetching library.

SWR stands for:
Stale-While-Revalidate

Basic idea:
1. Show cached/stale data quickly.
2. Fetch fresh data.
3. Update UI when fresh data arrives.

FLOW:
Cache
  |
  v
Show stale data quickly
  |
  v
Fetch latest data
  |
  v
Update cache/UI
"""

"""
Example:

'use client';

import useSWR from 'swr';

const fetcher = (url: string) =>
    fetch(url).then(res => res.json());

export default function Products() {
    const { data, error, isLoading } =
        useSWR('/api/products', fetcher);

    if (isLoading) return <p>Loading...</p>;
    if (error) return <p>Error</p>;

    return <pre>{JSON.stringify(data, null, 2)}</pre>;
}
"""

# MCQ POINTS
"""
- SWR is commonly used for client-side data fetching.
- SWR follows stale-while-revalidate behavior.
- useSWR is normally used in a Client Component.
"""

# -----------------------------------------------------------------------------
# 32. STYLING IN NEXT.JS
# -----------------------------------------------------------------------------

"""
COMMON STYLING METHODS
----------------------
1. Global CSS
2. CSS Modules
3. Tailwind CSS
4. Inline styles

CSS MODULE:
-----------
Button.module.css
"""

"""
.button {
    background: blue;
    color: white;
    padding: 10px;
}
"""

"""
Component:
import styles from './Button.module.css';

export default function Button() {
    return <button className={styles.button}>Click</button>;
}
"""

"""
CSS Modules provide locally scoped class names.
"""

# MCQ POINTS
"""
- CSS Modules help avoid global class-name conflicts.
- Global CSS applies more broadly.
- Tailwind uses utility classes.
"""

# -----------------------------------------------------------------------------
# 33. BASIC PERFORMANCE OPTIMIZATION
# -----------------------------------------------------------------------------

"""
IMPORTANT PERFORMANCE IDEAS
---------------------------
1. Use Server Components when client interactivity is unnecessary.
2. Avoid unnecessary JavaScript sent to browser.
3. Use optimized images with next/image.
4. Use dynamic imports/code splitting where useful.
5. Cache/revalidate data appropriately.
6. Keep components small and reusable.
7. Avoid unnecessary re-renders.
8. Load only what is needed.

EXAM KEYWORD:
"Reduce client-side JavaScript and unnecessary rendering."
"""

# Example image:
"""
import Image from 'next/image';

export default function Profile() {
    return (
        <Image
            src="/profile.jpg"
            alt="Profile"
            width={300}
            height={300}
        />
    );
}
"""

# -----------------------------------------------------------------------------
# 34. NEXT.JS RENDERING DECISION FLOW
# -----------------------------------------------------------------------------

"""
MEMORIZE THIS FLOW
------------------

Does the page need browser interaction/state?
                |
          +-----+-----+
          |           |
         YES          NO
          |           |
     Client part   Server Component
          |
          v
     "use client"

For rendering/data strategy:

Does data need to be fresh for every request?
                |
             YES -> SSR

Does content rarely change?
                |
             YES -> SSG

Does content change periodically?
                |
             YES -> ISR

Is it primarily browser-driven interactive data?
                |
             YES -> CSR
"""

# =============================================================================
# HIGH-PROBABILITY 4-MARK QUESTIONS
# =============================================================================

"""
Q1. Explain SSR, SSG, ISR and CSR with flow diagrams and differences.

ANSWER STRUCTURE:
- Define all four.
- Draw their flow.
- Give comparison table.
- Mention use cases.
- Write one-line memory trick.

Q2. Explain Next.js App Router architecture with file-based routing,
layouts, route groups and dynamic routes.

ANSWER STRUCTURE:
- app/ tree
- page.tsx
- layout.tsx
- (group)
- [id]
- Example URL mapping.

Q3. Explain Server Components and Client Components with example.

ANSWER STRUCTURE:
- Default behavior
- "use client"
- useState/useEffect
- database/secrets
- comparison table
- code.

Q4. Explain TypeScript in Next.js and demonstrate interface + props typing.

CODE:
"""

"""
type Product = {
    id: number;
    title: string;
    price: number;
};

function ProductCard({ product }: { product: Product }) {
    return (
        <div>
            <h2>{product.title}</h2>
            <p>{product.price}</p>
        </div>
    );
}
"""

# =============================================================================
# HIGH-PROBABILITY 2-MARK QUESTIONS
# =============================================================================

"""
1. What is the purpose of "use client"?
ANSWER:
It marks a component as a Client Component and is needed for browser-side
interactivity such as state, effects and event handlers.

2. Differentiate SSR and SSG.
ANSWER:
SSR renders at request time; SSG generates static content at build time.

3. What is a route group?
ANSWER:
A parenthesized folder such as (auth) used for organization without adding
that folder name to the URL.

4. What is ISR?
ANSWER:
Incremental Static Regeneration serves static content while allowing it
to be revalidated/regenerated over time.
"""

# =============================================================================
# 16 HIGH-PROBABILITY 1-MARK MCQs
# =============================================================================

"""
MCQ 1
Next.js is primarily built on:
A) Angular
B) React
C) Vue
D) Django
ANSWER: B

MCQ 2
The App Router uses which directory?
A) pages/
B) src/
C) app/
D) routes/
ANSWER: C

MCQ 3
app/page.tsx represents:
A) /home
B) /
C) /page
D) /app
ANSWER: B

MCQ 4
Which file is used for shared route UI?
A) shared.tsx
B) layout.tsx
C) common.tsx
D) ui.tsx
ANSWER: B

MCQ 5
What does [id] represent?
A) Static route
B) Route group
C) Dynamic route segment
D) API route only
ANSWER: C

MCQ 6
What does (auth) represent?
A) Dynamic route
B) Route group
C) API
D) Middleware
ANSWER: B

MCQ 7
In App Router, components are by default:
A) Client Components
B) Server Components
C) API Components
D) Static Components
ANSWER: B

MCQ 8
Which directive creates a Client Component?
A) "client"
B) "use browser"
C) "use client"
D) "client component"
ANSWER: C

MCQ 9
Which rendering happens at request time?
A) SSG
B) SSR
C) ISR only
D) CSS
ANSWER: B

MCQ 10
Which rendering happens at build time?
A) SSG
B) SSR
C) CSR
D) AJAX
ANSWER: A

MCQ 11
ISR mainly adds what to static generation?
A) Database
B) Revalidation
C) TypeScript
D) Routing
ANSWER: B

MCQ 12
Which file provides loading UI?
A) wait.tsx
B) loading.tsx
C) pending.tsx
D) loader.tsx
ANSWER: B

MCQ 13
Which file is associated with route-level error UI?
A) error.tsx
B) errors.tsx
C) catch.tsx
D) failed.tsx
ANSWER: A

MCQ 14
Which prefix exposes an environment variable to client/browser code?
A) CLIENT_
B) PUBLIC_
C) NEXT_PUBLIC_
D) BROWSER_
ANSWER: C

MCQ 15
SWR stands for:
A) Server Web Request
B) Stale-While-Revalidate
C) Static Web Rendering
D) Server With React
ANSWER: B

MCQ 16
Which command starts Next.js in development mode?
A) npm start
B) npm build
C) npm run dev
D) node start
ANSWER: C
"""

# =============================================================================
# OUTPUT-PREDICTION / CODE MCQs
# =============================================================================

"""
OUTPUT MCQ 1
------------

CODE:
"""

"""
export default function Page() {
    return <h1>Hello Next.js</h1>;
}

QUESTION:
What is rendered?

ANSWER:
Hello Next.js
"""

"""
OUTPUT MCQ 2
------------

app/blog/[id]/page.tsx

URL:
 /blog/25

If code prints params.id, output is:
25

IMPORTANT:
URL parameters are commonly received as strings.
"""

"""
OUTPUT MCQ 3
------------

CODE:

type User = {
    name: string;
    age: number;
};

const user: User = {
    name: "Piyush",
    age: "23"
};

QUESTION:
What happens?

ANSWER:
TypeScript type error because age must be number.
"""

"""
OUTPUT MCQ 4
------------

CODE:

function add(a: number, b: number): number {
    return a + b;
}

console.log(add(2, 3));

OUTPUT:
5
"""

"""
OUTPUT MCQ 5
------------

Suppose:
app/about/page.tsx

What URL opens the page?

ANSWER:
/about
"""

"""
OUTPUT MCQ 6
------------

Suppose:
app/products/[id]/page.tsx

URL:
/products/101

What is id?

ANSWER:
"101"
"""

# =============================================================================
# LAST-MINUTE EXAM MEMORY SHEET
# =============================================================================

"""
1. NEXT.JS
----------
React framework for full-stack web applications.

2. APP ROUTER
-------------
app/ directory.

3. ROUTING
----------
folder = URL segment
page.tsx = page

4. LAYOUT
---------
Shared UI.

5. ROUTE GROUP
--------------
(auth) -> organization only, does not affect URL.

6. DYNAMIC ROUTE
----------------
[id]

7. SERVER COMPONENT
-------------------
Default in App Router.

8. CLIENT COMPONENT
-------------------
"use client"

9. CSR
------
Browser renders.

10. SSR
-------
Server renders at request time.

11. SSG
-------
Static generation at build time.

12. ISR
-------
Static generation + revalidation.

13. loading.tsx
---------------
Loading UI.

14. error.tsx
-------------
Error UI; Client Component.

15. not-found.tsx
-----------------
Not-found UI.

16. TYPESCRIPT
--------------
Static typing.

17. INTERFACE
-------------
Object structure/type contract.

18. PROPS
---------
Parent -> Child data.

19. ENV
-------
NEXT_PUBLIC_ -> client exposed.
Secrets -> server only.

20. SWR
-------
Stale-While-Revalidate.

21. PERFORMANCE
---------------
Server Components + optimized images + caching + code splitting +
avoid unnecessary client JS.
"""

# =============================================================================
# VERY SHORT "WRITE IN EXAM" DEFINITIONS
# =============================================================================

"""
Next.js:
A React framework for building full-stack web applications.

SSR:
Rendering a page on the server for each request.

SSG:
Generating static pages at build time.

ISR:
Serving static pages while periodically/on-demand revalidating their data.

CSR:
Rendering/updating UI mainly in the browser using JavaScript.

Server Component:
A component that executes on the server and is the default in App Router.

Client Component:
A component marked with "use client" for browser-side interactivity.

Dynamic Route:
A route containing a dynamic segment such as [id].

Route Group:
A parenthesized folder used to organize routes without changing the URL.

Layout:
Reusable shared UI surrounding child routes.

TypeScript:
A typed superset of JavaScript that provides static type checking.

Interface:
A TypeScript construct describing the shape of an object.

SWR:
A data-fetching strategy/library based on stale-while-revalidate.
"""

# =============================================================================
# FINAL 5-MINUTE REVISION
# =============================================================================

"""
IF YOU HAVE ONLY 5 MINUTES, MEMORIZE:

app/page.tsx                 -> /
app/about/page.tsx           -> /about
app/blog/[id]/page.tsx       -> /blog/123
app/(auth)/login/page.tsx    -> /login

layout.tsx                   -> shared UI
loading.tsx                  -> loading UI
error.tsx                    -> error UI
not-found.tsx                -> 404/not-found UI

Default App Router component -> Server Component
"use client"                 -> Client Component

CSR -> Browser
SSR -> Server + Request
SSG -> Static + Build
ISR -> Static + Revalidate

NEXT_PUBLIC_ -> client-visible environment variable

SWR -> Stale-While-Revalidate

MOST IMPORTANT EXAM COMPARISON:
CSR vs SSR vs SSG vs ISR

MOST IMPORTANT CODE:
- Dynamic route [id]
- "use client"
- fetch()
- revalidate
- TypeScript interface
- Props typing
"""

# =============================================================================
# EXAM STRATEGY
# =============================================================================

"""
4-MARK QUESTIONS:
-----------------
Write:
Definition -> Diagram/Flow -> Example/Code -> Key points

2-MARK QUESTIONS:
-----------------
Write:
Definition + 2 important points OR Difference table.

1-MARK MCQs:
------------
Focus on:
- file names
- routing syntax
- default Server Component behavior
- "use client"
- SSR/SSG/ISR/CSR definitions
- TypeScript basics
- environment variable prefix
- npm commands

GOLDEN RULE:
-----------
If asked to compare technologies/rendering methods:
ALWAYS DRAW A TABLE.

If asked about routing:
ALWAYS DRAW THE app/ TREE.

If asked about SSR/SSG/ISR/CSR:
ALWAYS DRAW THE FLOW.

If asked coding:
Write a SMALL working example and explain what each important line does.
"""

# =============================================================================
# END OF NOTES
# =============================================================================
