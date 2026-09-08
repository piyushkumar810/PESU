import { headers } from "next/headers";

export default async function ServerInfo() {
  const headerList = await headers();

  const userAgent = headerList.get("user-agent");
  const host = headerList.get("host");
  const language = headerList.get("accept-language");
  const encoding = headerList.get("accept-encoding");

  return (
    <div>
      <h1>Server Information</h1>

      <p>
        <strong>Host:</strong> {host}
      </p>

      <p>
        <strong>User Agent:</strong> {userAgent}
      </p>

      <p>
        <strong>Language:</strong> {language}
      </p>

      <p>
        <strong>Encoding:</strong> {encoding}
      </p>
    </div>
  );
}