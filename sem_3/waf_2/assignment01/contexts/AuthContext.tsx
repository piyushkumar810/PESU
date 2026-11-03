"use client";

import {
  createContext,
  useContext,
  useState,
  useEffect,
  ReactNode,
} from "react";

type User = {
  userId: string;
  name: string;
  email: string;
  role: "student" | "admin";
};

type AuthContextType = {
  user: User | null;
  privateData: Record<string, unknown> | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  resetContext: () => void;
  loading: boolean;
};

const AuthContext = createContext<AuthContextType | undefined>(
  undefined
);

export function AuthProvider({
  children,
}: {
  children: ReactNode;
}) {
  const [user, setUser] = useState<User | null>(null);

  const [privateData, setPrivateData] =
    useState<Record<string, unknown> | null>(null);

  const [loading, setLoading] = useState(true);

  // Clear all user-specific Context data
  function resetContext() {
    setUser(null);
    setPrivateData(null);
  }

  // Login function
  async function login(email: string, password: string) {
    const response = await fetch("/api/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message);
    }

    setUser(data.user);
    setPrivateData(data.privateData);
  }

  // Restore existing server session on page refresh
  useEffect(() => {
    async function checkSession() {
      try {
        const response = await fetch("/api/auth/me");

        if (!response.ok) {
          resetContext();
          return;
        }

        const data = await response.json();

        setUser(data.user);
        setPrivateData(data.privateData);
      } catch {
        resetContext();
      } finally {
        setLoading(false);
      }
    }

    checkSession();
  }, []);

  // Logout and reset Context concurrently
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

  return (
    <AuthContext.Provider
      value={{
        user,
        privateData,
        login,
        logout,
        resetContext,
        loading,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error(
      "useAuth must be used inside AuthProvider"
    );
  }

  return context;
}