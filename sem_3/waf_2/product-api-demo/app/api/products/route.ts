import { NextResponse } from "next/server";
import { z } from "zod";

const ProductSchema = z.object({
  name: z
    .string()
    .trim()
    .min(2, "Name must have at least 2 characters"),

  price: z
    .number()
    .positive("Price must be greater than zero"),
});

export async function POST(request: Request) {
  try {
    const body: unknown = await request.json();

    const result = ProductSchema.safeParse(body);

    if (!result.success) {
      return NextResponse.json(
        {
          message: "Validation failed",
          errors: result.error.flatten().fieldErrors,
        },
        { status: 400 }
      );
    }

    return NextResponse.json(
      {
        message: "Product created successfully",
        product: result.data,
      },
      { status: 201 }
    );
  } catch {
    return NextResponse.json(
      { message: "Invalid JSON body" },
      { status: 400 }
    );
  }
}