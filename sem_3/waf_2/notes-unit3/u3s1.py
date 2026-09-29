'''
API Routes & Server-Side Functions

🎯 Goal: Understand how Next.js can work as both Frontend + Backend, and how we can safely execute backend logic on the server.

1. Big Picture 🧠

In a traditional web application:

┌──────────────┐
│   Frontend   │
│ React / HTML │
└──────┬───────┘
       │ HTTP Request
       ▼
┌──────────────┐
│   Backend    │
│ Node / Java  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Database   │
└──────────────┘
In Next.js

Next.js can combine frontend and backend:

              NEXT.JS APPLICATION
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
     Frontend UI           Backend Logic
     React Components      API Routes
                           Server Functions
                                │
                                ▼
                           Database

Remember:

Next.js is not only a frontend framework. It can also provide backend services.

2. API Routes
What is an API Route?

An API Route is a server-side endpoint that receives an HTTP request and sends a response.

Think:

Client
  │
  │ GET /api/users
  ▼
Next.js API Route
  │
  │ Query database
  ▼
Database
  │
  │ Data
  ▼
Next.js API Route
  │
  │ JSON Response
  ▼
Client

3. API Routes in Next.js App Router

In modern Next.js, API endpoints are created using:

app/
│
├── page.tsx
│
└── api/
    └── users/
        └── route.ts

The important file is:

route.ts
Example
// app/api/users/route.ts

export async function GET() {
    return Response.json({
        message: "Hello from API"
    });
}

Now the endpoint is:

GET /api/users
4. HTTP Methods

API routes can handle different HTTP methods.

                    API ROUTE
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
       GET            POST           DELETE
        │              │              │
     Read data      Create data     Delete data

Common methods:

Method	Purpose
GET	    Read data
POST	Create data
PUT	    Replace/update data
PATCH	Partially update data
DELETE	Delete data

Example
export async function GET() {
    return Response.json({ message: "Get users" });
}

export async function POST() {
    return Response.json({ message: "Create user" });
}

export async function DELETE() {
    return Response.json({ message: "Delete user" });
}


5. API Request Flow

Suppose the frontend wants users.

User opens webpage
       ↓
Frontend sends GET request
       ↓
GET /api/users
       ↓
route.ts
       ↓
Server-side logic
       ↓
Database
       ↓
User data
       ↓
JSON response
       ↓
Frontend displays users

This is one of the most important flows to remember.

6. Why API Routes Are Secure? 🔐

Suppose you have a database password.

❌ Don't do this:

const password = "myDatabasePassword";

inside client-side code.

Why?

Client Browser
      ↓
JavaScript visible to user
      ↓
❌ Secret can potentially be exposed

Instead:

Browser
   │
   │ Request
   ▼
API Route
   │
   │ Secret/database credentials
   ▼
Database

The API route runs on the server.

Therefore:

                    SERVER
              ┌─────────────────┐
              │ API Route       │
              │                 │
              │ DB credentials  │
              │ Secret keys     │
              │ Business logic  │
              └────────┬────────┘
                       │
                       ▼
                    Database

              ↑
              │ HTTP
              │
            Browser
⭐ Exam point

Sensitive operations and secret credentials should remain on the server, not in client-side code.

7. Server-Side Functions
A server-side function is a function that executes on the server instead of the user's browser.

Example:

async function getUsers() {
    const data = await db.user.findMany();
    return data;
}

The database operation happens on the server.

Browser
   │
   │ Request
   ▼
Server Function
   │
   ▼
Database
   │
   ▼
Data
8. Server Components vs Client Components

This is very important in Next.js.

                 Next.js Components
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       Server Component       Client Component
              │                     │
        Runs on server          Runs in browser
              │                     │
        DB/API access            useState
        Server logic             useEffect
                                  onClick
Server Component

By default, components in the App Router are Server Components.

export default async function Page() {

    const users = await getUsers();

    return (
        <div>
            {users.map(user => (
                <p>{user.name}</p>
            ))}
        </div>
    );
}

The database/data fetching can happen on the server.

Client Component

When you need browser interaction:

"use client";

import { useState } from "react";

export default function Counter() {

    const [count, setCount] = useState(0);

    return (
        <button onClick={() => setCount(count + 1)}>
            {count}
        </button>
    );
}

"use client" tells Next.js that this component needs to run on the client.

9. Server Actions / Server Functions

Next.js also provides Server Functions for performing server-side operations from application code.

Conceptually:

User clicks button
       ↓
Client UI
       ↓
Server Function
       ↓
Validate data
       ↓
Database operation
       ↓
Return result

Example:

"use server";

export async function createUser(formData: FormData) {

    const name = formData.get("name");

    // database operation
}

The important keyword is:

"use server";

It indicates that the function should execute on the server.

10. API Routes vs Server Functions
API Routes	Server Functions
Expose HTTP endpoints	Server-side functions
Called through URL/request	Called from application code
Useful for APIs	Useful for server-side mutations/actions
Can be consumed by external clients	Mainly used within the Next.js application
Uses HTTP methods	Uses function invocation
Easy memory trick 🧠
API Route
   ↓
URL + HTTP
   ↓
/api/users


Server Function
   ↓
Function call
   ↓
createUser()
11. CRUD Using API Routes

A common exam/real-world structure:

                    /api/users
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
      GET               POST             DELETE
       │                 │                 │
    Read users       Create user       Delete user

Example:

// app/api/users/route.ts

export async function GET() {

    return Response.json([
        { id: 1, name: "Piyush" },
        { id: 2, name: "Rahul" }
    ]);
}

export async function POST(request: Request) {

    const body = await request.json();

    return Response.json({
        message: "User created",
        user: body
    });
}
12. Request → Response

The basic API concept:

             REQUEST
                │
                ▼
       ┌────────────────┐
       │   API Route    │
       └───────┬────────┘
               │
        Process request
               │
               ▼
       ┌────────────────┐
       │ Business Logic │
       └───────┬────────┘
               │
               ▼
             RESPONSE

Example request:

POST /api/users

Body:

{
  "name": "Piyush"
}

Response:

{
  "message": "User created"
}
13. Security Flow 🔐

For secure backend services, remember this architecture:

             USER
              │
              ▼
        ┌─────────────┐
        │   Browser   │
        └──────┬──────┘
               │
          HTTP Request
               │
               ▼
        ┌─────────────┐
        │ Next.js API │
        │    Route    │
        └──────┬──────┘
               │
          Validation
               │
               ▼
       Authentication
               │
               ▼
        Authorization
               │
               ▼
        Business Logic
               │
               ▼
          Database
Security layers
Request
   ↓
Validation
   ↓
Authentication
   ↓
Authorization
   ↓
Business Logic
   ↓
Database

Very important: API routes are server-side code, but simply putting code in an API route does not automatically make an API secure. You still need proper validation, authentication, authorization, and safe handling of secrets.

14. ⭐ Exam Revision
API Route

A server-side endpoint in Next.js that handles HTTP requests and returns responses.

route.ts

File used to define API route handlers in the Next.js App Router.

Server Component

A component that executes on the server and can perform server-side data fetching.

Client Component

A component that executes in the browser and is used when client-side interactivity is required.

"use client"

Marks a component as a Client Component.

"use server"

Marks a function/code for server-side execution.

🧠 Complete Unit Visualization

Remember this single diagram:

                 NEXT.JS
                    │
       ┌────────────┴────────────┐
       │                         │
       ▼                         ▼
   FRONTEND                  BACKEND
       │                         │
       │                  ┌──────┴──────┐
       │                  │             │
       ▼                  ▼             ▼
Client Components     API Routes   Server Functions
       │                  │             │
       │                  └──────┬──────┘
       │                         │
       │                    Server Logic
       │                         │
       │                  Validation 🔐
       │                         │
       │                  Authentication
       │                         │
       │                  Authorization
       │                         │
       │                         ▼
       │                     Database
       │                         │
       └─────────────── Response/Data
🔥 One-line memory

API Route = HTTP endpoint
Server Function = server-side function
Server Component = server-rendered component
Client Component = browser-interactive component
route.ts = API route file
"use client" = client code
"use server" = server code
'''
