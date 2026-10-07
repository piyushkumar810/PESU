import NextAuth from "next-auth";
import Credentials from "next-auth/providers/credentials";

export const demoUser = {
  id: "1",
  name: "your_name",
  email: "your_name@example.com",
};

export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [
    Credentials({
      name: "Credentials",
      credentials: {
        username: {
          label: "Username",
          type: "text",
          placeholder: "your_name",
        },
        password: {
          label: "Password",
          type: "password",
          placeholder: "12345",
        },
      },
      async authorize(credentials) {
        const username =
          typeof credentials?.username === "string"
            ? credentials.username
            : "";
        const password =
          typeof credentials?.password === "string"
            ? credentials.password
            : "";

        if (username === "piyush kumar" && password === "12345") {
          return demoUser;
        }

        return null;
      },
    }),
  ],
  pages: {
    signIn: "/login",
  },
  session: {
    strategy: "jwt",
  },
});
