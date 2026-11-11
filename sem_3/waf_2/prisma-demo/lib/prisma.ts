import "server-only";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../app/generated/prisma/client";

// Prevent multiple Prisma instances during development
const globalForPrisma = globalThis as unknown as {
  prisma?: PrismaClient;
};

// PostgreSQL adapter
const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL!,
});

// Create or reuse Prisma Client
const prisma =
  globalForPrisma.prisma ??
  new PrismaClient({ adapter });

// Save instance during development
if (process.env.NODE_ENV !== "production") {
  globalForPrisma.prisma = prisma;
}

export { prisma };