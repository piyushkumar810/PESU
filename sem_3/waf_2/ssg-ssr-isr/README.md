
<!-- --------------------concepts for this project------------------------------ -->

============================================================
              NEXT.JS RENDERING CONCEPTS
============================================================

Our project contains:

app/
│
├── books/
│   └── page.tsx
│
├── users/
│   └── page.tsx
│
├── server-info/
│   └── page.tsx
│
├── post/
│   └── page.tsx
│
├── blog/
│   └── [id]/
│       └── page.tsx
│
├── not-found.tsx
├── page.tsx
├── layout.tsx
└── globals.css


============================================================
1. SSG — STATIC SITE GENERATION
============================================================

Folder:
    app/books/page.tsx

Purpose:
    Used when the data does not change frequently.

Example:
    const books = ["Next.js", "React", "TypeScript"];

The page can be generated as static HTML.

Flow:

    Build time
        ↓
    Next.js generates the page
        ↓
    HTML is stored/cached
        ↓
    User requests /books
        ↓
    Static HTML is served


Why use SSG?

    - Very fast
    - Good for static content
    - Good for documentation, blogs, product information, etc.
    - Less server work


============================================================
2. SSR — SERVER-SIDE RENDERING
============================================================

Folder:
    app/users/page.tsx

Important code:

    fetch(url, {
        cache: "no-store"
    })

Meaning:
    Always fetch fresh data from the server.

Flow:

    User requests /users
            ↓
    Next.js server runs page.tsx
            ↓
    API is called
            ↓
    Fresh users data is received
            ↓
    HTML is generated
            ↓
    HTML is sent to browser


Why use SSR?

    - Data must be fresh
    - Data changes frequently
    - Useful for dashboards, live information, user-specific data, etc.


KEY POINT:

    cache: "no-store"

    = Do not cache the fetched data.
    = Fetch fresh data for every request.


============================================================
3. SERVER INFORMATION — headers()
============================================================

Folder:
    app/server-info/page.tsx

Important code:

    import { headers } from "next/headers";

    const headerList = await headers();

Purpose:

    Read HTTP request headers on the server.

Examples:

    user-agent
    host
    accept-language
    accept-encoding


Flow:

    Browser sends request
            ↓
    Request contains HTTP headers
            ↓
    Next.js server receives request
            ↓
    headers() reads the headers
            ↓
    Information is displayed


Why use this?

    - Get browser/client information
    - Read request information
    - Read cookies/headers when required
    - Perform server-side logic based on request data


IMPORTANT:

    This is server-side functionality because
    headers() is used on the server.


============================================================
4. ISR — INCREMENTAL STATIC REGENERATION
============================================================

Folder:
    app/post/page.tsx

Important code:

    fetch(url, {
        next: {
            revalidate: 10
        }
    })


Meaning:

    Cache the result and allow Next.js to regenerate
    the data/page after 10 seconds.


Flow:

    First user request
            ↓
    Next.js generates/fetches the page
            ↓
    Result is cached
            ↓
    Other users receive cached result
            ↓
    After 10 seconds
            ↓
    Next.js can regenerate fresh data
            ↓
    New version is cached


Why use ISR?

    - Data changes occasionally
    - We don't need fresh data on every request
    - Better performance than fetching everything every time
    - Useful for blogs, news, product pages, etc.


KEY POINT:

    revalidate: 10

    = Revalidation period is 10 seconds.


============================================================
5. DYNAMIC ROUTING
============================================================

Folder:

    app/blog/[id]/page.tsx


Here:

    [id]

is a dynamic route parameter.


Examples:

    /blog/1
    /blog/2
    /blog/10


All of these use:

    app/blog/[id]/page.tsx


Code:

    const { id } = await params;


For:

    /blog/5

we get:

    id = "5"


Then we can fetch:

    https://jsonplaceholder.typicode.com/posts/5


Flow:

    User visits /blog/5
            ↓
    Next.js matches [id]
            ↓
    id = 5
            ↓
    page.tsx receives id
            ↓
    API request is made for post 5
            ↓
    Post 5 is displayed


Why use Dynamic Routing?

    When the URL contains a value that changes.

Examples:

    /product/101
    /product/102

    /user/1
    /user/2

    /blog/1
    /blog/2


============================================================
6. DYNAMIC ROUTING + ISR
============================================================

Our:

    app/blog/[id]/page.tsx

can also use:

    next: {
        revalidate: 10
    }


Therefore we are combining:

    Dynamic Routing
          +
        ISR


Example:

    /blog/1
    /blog/2
    /blog/3


Each URL has a different id, and the fetched data
can be revalidated.


============================================================
7. NOT FOUND PAGE
============================================================

File:

    app/not-found.tsx


This is a special Next.js file.

Purpose:

    Display a custom 404 page when a requested page
    does not exist.


Example:

    User visits:

        /hello

    But /hello does not exist.

    ↓

    Next.js displays:

        404 - Page Not Found


Code:

    export default function NotFound() {
        return (
            <div>
                <h1>404 - Page Not Found</h1>
                <p>
                    Sorry, the page you are looking for
                    does not exist.
                </p>
            </div>
        );
    }


============================================================
8. notFound() FUNCTION
============================================================

In dynamic routes we can manually trigger the
Not Found page.

Example:

    import { notFound } from "next/navigation";


If API data doesn't exist:

    if (!response.ok) {
        notFound();
    }


Flow:

    /blog/999
        ↓
    API request
        ↓
    Post 999 doesn't exist
        ↓
    notFound()
        ↓
    app/not-found.tsx
        ↓
    404 page displayed


IMPORTANT DIFFERENCE:

    not-found.tsx
        → Defines WHAT the 404 page looks like.

    notFound()
        → Tells Next.js WHEN to show the 404 page.


============================================================
9. COMPLETE PROJECT FLOW
============================================================


                    USER REQUEST
                         |
                         ↓
                ┌─────────────────┐
                │    Next.js      │
                │     Router      │
                └─────────────────┘
                         |
          ┌──────────────┼───────────────┐
          ↓              ↓               ↓
       /books         /users          /post
          ↓              ↓               ↓
        SSG             SSR             ISR
          ↓              ↓               ↓
     Static HTML    Fresh API data    Cached data
                                      + revalidate
         


Dynamic Blog:

    /blog/5
       ↓
    [id]
       ↓
    id = 5
       ↓
    Fetch post 5
       ↓
    Display post


If post doesn't exist:

    API fails
       ↓
    notFound()
       ↓
    app/not-found.tsx
       ↓
    404 Page


============================================================
10. QUICK REVISION
============================================================

BOOKS
    app/books/page.tsx
    ↓
    SSG
    ↓
    Static content


USERS
    app/users/page.tsx
    ↓
    SSR
    ↓
    cache: "no-store"
    ↓
    Fresh data every request


SERVER INFO
    app/server-info/page.tsx
    ↓
    headers()
    ↓
    Read request headers on server


POST
    app/post/page.tsx
    ↓
    ISR
    ↓
    revalidate: 10
    ↓
    Cached + periodically regenerated


BLOG
    app/blog/[id]/page.tsx
    ↓
    Dynamic Routing
    ↓
    /blog/1, /blog/2, /blog/3...


BLOG + ISR
    [id] + revalidate
    ↓
    Dynamic Routing + ISR


NOT FOUND
    app/not-found.tsx
    ↓
    Custom 404 page


notFound()
    ↓
    Manually triggers 404 page


============================================================
11. MOST IMPORTANT INTERVIEW POINT
============================================================

SSG:
    "Generate static content and serve it."

SSR:
    "Generate the page on the server for each request."

ISR:
    "Serve cached/static content and regenerate it
     after a specified revalidation period."

Dynamic Routing:
    "Use [id] when part of the URL is dynamic."

not-found.tsx:
    "Defines the custom 404 UI."

notFound():
    "Programmatically triggers the 404 page."


============================================================
ONE-LINE MEMORY TRICK
============================================================

SSG  → Static
SSR  → Fresh every request
ISR  → Cached + Revalidate
[id] → Dynamic URL
headers() → Request information
notFound() → Trigger 404
not-found.tsx → 404 UI
============================================================