This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.


<!-- details how to run and both project explanation -->
<!-- 
# NEXT.JS PRACTICAL ASSIGNMENTS
## Assignment 18 – Feedback Moderation
## Assignment 49 – Context Reset on Logout

---

# PART 1: RUNNING THE NEXT.JS APPLICATION

## Step 1: Open the Project

1. Open Visual Studio Code.
2. Open your existing Next.js project.
3. Open the terminal using:

   `Ctrl + ``

4. Make sure the terminal is inside your project folder.

## Step 2: Start the Development Server

Execute the following command:

```bash
npm run dev
```

Wait until the terminal displays:

```text
▲ Next.js
- Local: http://localhost:3000

✓ Ready
```

This means your Next.js development server has started successfully.

## Step 3: Open the Application

Open Google Chrome and enter:

```text
http://localhost:3000
```

### Expected Output: Home Page

The homepage displays:

- Next.js Assignments
- Assignment 18 – Feedback Moderation
- Assignment 49 – Context Reset on Logout
- Login

There are two assignment buttons:

1. Open Assignment 18
2. Open Assignment 49

---

# PART 2: ASSIGNMENT 18 – FEEDBACK MODERATION

## 1. Understanding the Assignment

**Problem Statement:**

Validate rating/comment, let students submit pending feedback, and restrict approval to admins.

**Main requirements:**

1. Validate student ratings.
2. Validate student comments.
3. Save valid feedback with `pending` status.
4. Allow admins to approve feedback.
5. Prevent students from approving feedback.

## 2. Open Assignment 18

From the homepage:

1. Click **Open Assignment 18**.
2. The browser opens:

```text
http://localhost:3000/assignment18
```

### Expected Output (When Not Logged In)

```text
Assignment 18: Feedback Moderation

Submit feedback and manage its approval status.

Please login to continue.

Login here
```

**Why does this happen?**

The application checks whether a user is logged in.

If no authenticated user exists, it displays the login link instead of the feedback form.

## 3. Login as a Student

Click **Login here**.

The login page opens.

Enter the following credentials:

```text
Email: student@gmail.com
Password: student123
```

Click the Login button.

### Expected Output

You will be redirected to Assignment 18 because you selected Login from the Assignment 18 page.

The application now recognizes you as a student.

## 4. Submit Valid Feedback

On the Assignment 18 page, you will see the Submit Feedback form.

Enter the following details:

```text
Rating: 4

Comment: need hard work
```

Click **Submit Feedback**.

### Expected Output

```text
Feedback submitted successfully

Submitted Feedback

Rating: 4/5

Comment: need hard work

Status: pending

Your feedback is waiting for admin approval.
```

**Explanation:**

The feedback has been successfully submitted.

The backend automatically assigns:

```typescript
status: "pending"
```

This means students cannot directly approve their own feedback.

The feedback must wait for an administrator.

## 5. Test Invalid Rating – HTTP 400

Now we will test whether the backend correctly validates the rating.

### Step 1: Open Chrome Developer Tools

While logged in as a student:

1. Open the Assignment 18 page.
2. Press `Ctrl + Shift + J`.

Alternative:

- Press `Fn + F12` if supported by your ASUS keyboard.
- Or open Chrome menu (three dots).
- Select More tools → Developer tools.
- Click the Console tab.

The Chrome Console will appear.

### Step 2: Enter Invalid Rating Code

Copy and paste this code into the Console:

```javascript
fetch("/api/feedback", {
  method: "POST",
  credentials: "same-origin",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    rating: 8,
    comment: "Good teaching"
  })
})
.then(async res => ({
  status: res.status,
  data: await res.json()
}))
.then(console.log);
```

Press Enter.

### Expected Output

```text
{
  status: 400,
  data: {
    message: "Rating must be an integer between 1 and 5"
  }
}
```

**Explanation:**

The rating is 8.

However, the application only accepts ratings between 1 and 5.

Therefore, the server rejects the request.

HTTP 400 means **Bad Request**.

This proves that rating validation is working.

## 6. Test Invalid Comment – HTTP 400

Now we will check whether the backend validates comments.

Keep the Console open.

Paste this code:

```javascript
fetch("/api/feedback", {
  method: "POST",
  credentials: "same-origin",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    rating: 5,
    comment: "Hi"
  })
})
.then(async res => ({
  status: res.status,
  data: await res.json()
}))
.then(console.log);
```

Press Enter.

### Expected Output

```text
{
  status: 400,
  data: {
    message: "Comment must contain 5 to 500 characters"
  }
}
```

**Explanation:**

The comment contains only two characters.

Our backend requires a comment of at least 5 characters and no more than 500 characters.

Therefore, the server rejects the request.

HTTP 400 means **Bad Request**.

This proves that comment validation is working.

## 7. Test Student Approval Restriction – HTTP 403

This is one of the most important requirements of Assignment 18.

Only administrators should approve feedback.

A student must not have permission to approve feedback.

### Step 1: Make Sure You Are Logged In as Student

Use:

```text
Email: student@gmail.com
Password: student123
```

Open Assignment 18.

Open Chrome Console:

`Ctrl + Shift + J`

### Step 2: Execute This Code

```javascript
fetch("/api/admin/feedback", {
  method: "PATCH",
  credentials: "same-origin",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    id: "anything"
  })
})
.then(async res => ({
  status: res.status,
  data: await res.json()
}))
.then(console.log);
```

Press Enter.

### Expected Output

```text
{
  status: 403,
  data: {
    message: "Only admins can approve feedback"
  }
}
```

**Explanation:**

The server checks the logged-in user's role.

The current user has the role:

```text
student
```

But only users with the role:

```text
admin
```

can approve feedback.

Therefore, the server returns HTTP 403.

HTTP 403 means **Forbidden**.

This proves that student approval is restricted.

## 8. Login as Admin

Now we will test the administrator's approval functionality.

### Step 1: Logout from Student Account

Open:

```text
http://localhost:3000/assignment49
```

Click the red Logout button.

You will be redirected to the Login page.

### Step 2: Enter Admin Credentials

```text
Email: admin@gmail.com
Password: admin123
```

Click Login.

### Step 3: Open Assignment 18

Enter:

```text
http://localhost:3000/assignment18
```

Because you are logged in as an administrator, the application displays:

```text
Assignment 18: Feedback Moderation

Admin Feedback Dashboard
```

### Expected Output

You should see the submitted feedback records.

Example:

```text
Rating: 4/5

Comment: need hard work

Status: pending

[Approve]
```

You may see multiple feedback records if you submitted feedback more than once.

## 9. Approve Feedback as Admin

Click the green **Approve** button.

### Expected Output

Before approval:

```text
Status: pending
```

After approval:

```text
Status: approved
```

The Approve button disappears after successful approval.

**Explanation:**

The admin sends a PATCH request to the backend.

The backend checks the admin's role, finds the feedback using its ID, and changes its status.

The status changes from:

```text
pending → approved
```

This proves that administrator approval is working.

## 10. Assignment 18 – Final Expected Results

| Test Case | Expected Result |
|---|---|
| Valid feedback submission | 201 Created |
| Invalid rating | 400 Bad Request |
| Invalid comment | 400 Bad Request |
| Student attempts approval | 403 Forbidden |
| Admin views feedback | Feedback displayed |
| Admin approves feedback | 200 OK |
| Initial feedback status | pending |
| Final feedback status | approved |

**Assignment 18 is completed.**

---

# PART 3: ASSIGNMENT 49 – CONTEXT RESET ON LOGOUT

## 1. Understanding the Assignment

**Problem Statement:**

Store user-specific data in Context and clear it on sign-out while invalidating the server session.

**Technical Hint:**

Create a `resetContext()` function inside the React Context provider that runs concurrently with logout handlers.

**Main requirements:**

1. Store user-specific data in React Context.
2. Create a `resetContext()` function.
3. Clear user information when the user logs out.
4. Invalidate the server session.
5. Ensure the next user sees only their own data.

## 2. Login as Student

Open:

```text
http://localhost:3000/login
```

Enter:

```text
Email: student@gmail.com
Password: student123
```

Click Login.

Open:

```text
http://localhost:3000/assignment49
```

### Expected Output

```text
Assignment 49: Context Reset

Welcome, Piyush Kumar

User Information

Name: Piyush Kumar
Email: student@gmail.com
Role: student

Private Context Data

course: MCA
semester: 3
department: Computer Applications

[Logout]
```

**Explanation:**

The application stores the student's information in React Context.

The private data belongs to the currently logged-in student.

React Context allows different components to access shared data without passing it through multiple levels of props.

## 3. Understand resetContext()

In the file:

```text
contexts/AuthContext.tsx
```

The following function is implemented:

```typescript
function resetContext() {
  setUser(null);
  setPrivateData(null);
}
```

**Explanation:**

There are two important state variables:

1. `user` – stores user information.
2. `privateData` – stores private information.

When `resetContext()` executes:

```typescript
setUser(null);
setPrivateData(null);
```

Both values become null.

This removes the previous user's information from React Context.

## 4. Logout from Student Account

On Assignment 49, click the red Logout button.

The logout function executes:

```typescript
async function logout() {
  const logoutRequest = fetch("/api/auth/logout", {
    method: "POST",
  });

  const contextReset = Promise.resolve().then(() => {
    resetContext();
  });

  await Promise.allSettled([
    logoutRequest,
    contextReset,
  ]);
}
```

**Explanation:**

Two operations happen concurrently:

**Operation 1: Server Logout**

```typescript
fetch("/api/auth/logout", {
  method: "POST",
});
```

This calls the logout API.

The server expires the authentication cookie.

**Operation 2: Context Reset**

```typescript
resetContext();
```

This clears user-specific information from React Context.

**Promise.allSettled():**

This waits for both operations to settle, without allowing a failed server request to prevent the local Context reset.

### Expected Output

After clicking Logout:

- Student information disappears.
- Private Context data is cleared.
- Server session cookie is expired.
- Browser redirects to Login.

## 5. Verify Server Session Invalidation

Now we will verify that the server no longer recognizes the logged-out user.

### Step 1: Open Chrome Console

After logout, open Chrome Developer Tools.

Press:

```text
Ctrl + Shift + J
```

Click the Console tab if necessary.

### Step 2: Execute This Code

```javascript
fetch("/api/auth/me", {
  credentials: "same-origin"
})
.then(async res => ({
  status: res.status,
  data: await res.json()
}))
.then(console.log);
```

Press Enter.

### Expected Output

```text
{
  status: 401,
  data: {
    message: "Unauthorized"
  }
}
```

**Explanation:**

The `/api/auth/me` endpoint checks whether a valid session cookie exists.

After logout, the session cookie is expired.

Therefore, the server does not recognize the previous user.

HTTP 401 means **Unauthorized**.

This proves that server session invalidation is working.

## 6. Login as a Different User (Admin)

Now we will verify that the next user sees only their own information.

Open:

```text
http://localhost:3000/login
```

Enter:

```text
Email: admin@gmail.com
Password: admin123
```

Click Login.

Open:

```text
http://localhost:3000/assignment49
```

### Expected Output

```text
Assignment 49: Context Reset

Welcome, Admin

User Information

Name: Admin
Email: admin@gmail.com
Role: admin

Private Context Data

department: Administration
access: Full Access

[Logout]
```

**Explanation:**

The previous student information is no longer displayed.

The new admin session loads the admin's own information.

This proves that user-specific data is being cleared and correctly replaced after logout and the next login.

---

# PART 4: ASSIGNMENT 49 – FINAL EXPECTED RESULTS

| Test Case | Expected Result |
|---|---|
| Student login | Student data displayed |
| Context stores user data | User-specific data available |
| Logout button | Logout function executes |
| resetContext() | User and private data cleared |
| Server logout API | Session cookie expired |
| Check session after logout | 401 Unauthorized |
| Admin login | Admin data displayed |
| Previous student data | Not displayed |

**Assignment 49 is completed.**

---

# PART 5: IMPORTANT HTTP STATUS CODES

These are the status codes used in our practical assignments.

| Status Code | Meaning | Where Used |
|---|---|---|
| 200 | OK | Admin successfully approves feedback |
| 201 | Created | Feedback successfully submitted |
| 400 | Bad Request | Invalid rating or comment |
| 401 | Unauthorized | No valid login session |
| 403 | Forbidden | Student attempts admin approval |
| 404 | Not Found | Feedback ID does not exist |

### Easy Way to Remember

- 200 – Request successful.
- 201 – New data created.
- 400 – Invalid input.
- 401 – Not logged in.
- 403 – Logged in, but not allowed.
- 404 – Requested item not found.

---

# PART 6: FINAL PROJECT VERIFICATION

## Assignment 18 – Feedback Moderation

- Student can submit feedback.
- Rating validation works.
- Comment validation works.
- New feedback starts with pending status.
- Admin can view feedback.
- Only admin can approve feedback.
- Approved feedback displays approved status.

## Assignment 49 – Context Reset on Logout

- User-specific data is stored in React Context.
- `resetContext()` clears user information.
- Logout executes Context reset and server logout.
- Server session becomes invalid after logout.
- Next user sees only their own information.

---

# IMPORTANT NOTES

1. Always start the project using `npm run dev`.
2. Keep the terminal running while testing.
3. Login as a student when testing student operations.
4. Login as an admin when testing approval.
5. Use Chrome Console for API validation tests.
6. Use the correct account before executing API test code.

**Note about the current implementation:** Feedback is stored in an in-memory array, so it is suitable for this local practical demonstration but will be cleared when the server restarts. The login credentials are demonstration credentials, not production authentication.

---

# CONCLUSION

In these two Next.js assignments, we implemented and tested backend API validation, role-based authorization, feedback moderation, React Context API, logout functionality, Context state reset and server session invalidation.

Both assignments were tested step by step, and the expected outputs were successfully verified.

**Final Result: Assignment 18 – Completed. Assignment 49 – Completed.** 

-->