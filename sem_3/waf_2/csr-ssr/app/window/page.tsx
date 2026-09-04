"use client";

import { useEffect, useState } from "react";

export default function BrowserInfo() {
    const [url, setUrl] = useState("");
    const [title, setTitle] = useState("");
    const [browser, setBrowser] = useState("");
    const [localData, setLocalData] = useState("");
    const [sessionData, setSessionData] = useState("");

    useEffect(() => {

        // 1. window
        setUrl(window.location.href);

        // 2. document
        setTitle(document.title);

        // 3. navigator
        setBrowser(navigator.userAgent);

        // 4. localStorage
        localStorage.setItem("username", "Student");
        setLocalData(localStorage.getItem("username") || "");

        // 5. sessionStorage
        sessionStorage.setItem("sessionUser", "Student");
        setSessionData(sessionStorage.getItem("sessionUser") || "");

    }, []);

    return (
        <div>
            <h1>Browser Information</h1>

            <p><strong>Window URL:</strong> {url}</p>

            <p><strong>Document Title:</strong> {title}</p>

            <p><strong>Browser:</strong> {browser}</p>

            <p><strong>Local Storage:</strong> {localData}</p>

            <p><strong>Session Storage:</strong> {sessionData}</p>
        </div>
    );
}