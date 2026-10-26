<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="com.example.Person" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Details - PES University</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">
    <div class="card">

        <%
            // Retrieve the Person object passed from PersonServlet via request.setAttribute("person", person)
            Person person = (Person) request.getAttribute("person");
            String confirmStatus = (String) request.getAttribute("confirmStatus");

            // Safeguard: If user directly navigates to result.jsp without submitting the form
            if (person == null) {
        %>
            <div class="card-header">
                <span class="badge" style="background:#fee2e2; color:#b91c1c;">No Data Found</span>
                <h1>Session Expired or Direct Access</h1>
                <p>No registration data was found in the current request. Please submit the form first.</p>
            </div>
            <a href="index.jsp" class="btn-secondary">Go to Registration Form</a>
        <%
            } else {
        %>
            <div class="card-header">
                <span class="badge">Success</span>
                <h1>Registration Successful!</h1>
                <p>The Person object was successfully created and validated on the server.</p>
            </div>

            <div class="alert alert-success">
                <strong>Status:</strong> Registration details have been validated and saved into the Java object.
            </div>

            <!-- Display all five fields / confirmation status -->
            <div class="details-list">
                <div class="details-row">
                    <span class="details-label">1. First Name:</span>
                    <span class="details-value"><%= person.getFirstName() %></span>
                </div>
                <div class="details-row">
                    <span class="details-label">2. Last Name:</span>
                    <span class="details-value"><%= person.getLastName() %></span>
                </div>
                <div class="details-row">
                    <span class="details-label">3. Phone Number:</span>
                    <span class="details-value"><%= person.getPhoneNumber() %></span>
                </div>
                <div class="details-row">
                    <span class="details-label">4. Aadhaar Number (Masked):</span>
                    <span class="details-value">
                        <code><%= person.getMaskedAadhaar() %></code>
                    </span>
                </div>
                <div class="details-row">
                    <span class="details-label">5. Aadhaar Confirmation:</span>
                    <span class="details-value">
                        <span class="status-badge">
                            <%= confirmStatus != null ? confirmStatus : "Verified" %>
                        </span>
                    </span>
                </div>
            </div>

            <!-- Action buttons -->
            <a href="index.jsp" class="btn-secondary">&larr; Register Another Person</a>

            <div class="footer-note">
                Security Notice: Aadhaar number is masked (first 8 digits hidden) to adhere to UIDAI security guidelines.
            </div>
        <%
            }
        %>

    </div>
</div>

</body>
</html>
