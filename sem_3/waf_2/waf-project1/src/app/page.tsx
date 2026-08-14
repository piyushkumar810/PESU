export default function Home() {
    const appName = process.env.APP_NAME;
    const apiUrl = process.env.API_URL;
    const databaseUrl = process.env.DATABASE_URL;
    const universityName = process.env.UNIVERSITY_NAME;

    const appTitle = process.env.NEXT_PUBLIC_APP_TITLE;
    const publicApiUrl = process.env.NEXT_PUBLIC_API_URL;

    const jwtSecret = process.env.JWT_SECRET;
    const emailUser = process.env.EMAIL_USER;


    
    return (
        <div>
            <h1>{appName}</h1>

            <p>API URL: {apiUrl}</p>
            <p>Database URL: {databaseUrl}</p>
            <p>University: {universityName}</p>

            <hr />

            <p>Public App Title: {appTitle}</p>
            <p>Public API URL: {publicApiUrl}</p>

            <hr />

            <p>JWT Secret: {jwtSecret ? "Loaded" : "Not found"}</p>
            <p>Email User: {emailUser}</p>
        </div>
    );
}