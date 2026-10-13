// import { NextRequest, NextResponse } from "next/server";

// export function middleware(request: NextRequest) {
//   const token = request.cookies.get("token");

//   if (!token) {
//     return NextResponse.redirect(
//       new URL("/login", request.url)
//     );
//   }

//   return NextResponse.next();
// }

// export const config = {
//   matcher: ["/dashboard/:path*"],
// };


import { NextRequest, NextResponse } from "next/server";

export function middleware(request: NextRequest) {
  const token = request.cookies.get("token");

  console.log("Middleware is running");
  console.log("Token:", token?.value);

  if (!token?.value) {
    return NextResponse.redirect(
      new URL("/login", request.url)
    );
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*"],
};
