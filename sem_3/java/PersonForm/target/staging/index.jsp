<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.util.Map" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Person Registration Form</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">
    <div class="card">
        <div class="card-header">
            <span class="badge">PES University - Java Web App</span>
            <h1>Person Registration</h1>
            <p>Please enter your details below. All fields are mandatory.</p>
        </div>

        <%-- Server-Side Error Notification Banner --%>
        <%
            @SuppressWarnings("unchecked")
            Map<String, String> errors = (Map<String, String>) request.getAttribute("errors");
            if (errors != null && !errors.isEmpty()) {
        %>
            <div class="alert alert-danger" role="alert">
                <h4>Submission Errors:</h4>
                <ul>
                    <% for (String msg : errors.values()) { %>
                        <li><%= msg %></li>
                    <% } %>
                </ul>
            </div>
        <%
            }
        %>

        <%-- Registration Form --%>
        <%-- Submits via HTTP POST to /register mapped to PersonServlet --%>
        <form action="<%= request.getContextPath() %>/register" method="POST" novalidate>

            <%-- Row for First Name and Last Name --%>
            <div class="form-row">
                <div class="form-group">
                    <label for="firstName">First Name <span class="required-star">*</span></label>
                    <input 
                        type="text" 
                        id="firstName" 
                        name="firstName" 
                        placeholder="e.g. Piyush"
                        value="<%= request.getAttribute("firstName") != null ? request.getAttribute("firstName") : "" %>"
                        required>
                    <% if (errors != null && errors.containsKey("firstName")) { %>
                        <div class="field-error-msg"><%= errors.get("firstName") %></div>
                    <% } %>
                </div>

                <div class="form-group">
                    <label for="lastName">Last Name <span class="required-star">*</span></label>
                    <input 
                        type="text" 
                        id="lastName" 
                        name="lastName" 
                        placeholder="e.g. Kumar"
                        value="<%= request.getAttribute("lastName") != null ? request.getAttribute("lastName") : "" %>"
                        required>
                    <% if (errors != null && errors.containsKey("lastName")) { %>
                        <div class="field-error-msg"><%= errors.get("lastName") %></div>
                    <% } %>
                </div>
            </div>

            <%-- Phone Number Field --%>
            <div class="form-group">
                <label for="phoneNumber">Phone Number (10 Digits) <span class="required-star">*</span></label>
                <input 
                    type="tel" 
                    id="phoneNumber" 
                    name="phoneNumber" 
                    placeholder="e.g. 9876543210"
                    maxlength="10"
                    pattern="[0-9]{10}"
                    value="<%= request.getAttribute("phoneNumber") != null ? request.getAttribute("phoneNumber") : "" %>"
                    required>
                <div class="helper-text">Must be exactly 10 numeric digits. Leading zeros are preserved.</div>
                <% if (errors != null && errors.containsKey("phoneNumber")) { %>
                    <div class="field-error-msg"><%= errors.get("phoneNumber") %></div>
                <% } %>
            </div>

            <%-- Aadhaar Number Field --%>
            <div class="form-group">
                <label for="aadhaarNumber">Aadhaar Number (12 Digits) <span class="required-star">*</span></label>
                <input 
                    type="password" 
                    id="aadhaarNumber" 
                    name="aadhaarNumber" 
                    placeholder="Enter 12-digit Aadhaar number"
                    maxlength="12"
                    pattern="[0-9]{12}"
                    value="<%= request.getAttribute("aadhaarNumber") != null ? request.getAttribute("aadhaarNumber") : "" %>"
                    required>
                <div class="helper-text">Must be exactly 12 numeric digits without hyphens or spaces.</div>
                <% if (errors != null && errors.containsKey("aadhaarNumber")) { %>
                    <div class="field-error-msg"><%= errors.get("aadhaarNumber") %></div>
                <% } %>
            </div>

            <%-- Confirm Aadhaar Number Field --%>
            <div class="form-group">
                <label for="confirmAadhaar">Confirm Aadhaar Number <span class="required-star">*</span></label>
                <input 
                    type="password" 
                    id="confirmAadhaar" 
                    name="confirmAadhaar" 
                    placeholder="Re-enter 12-digit Aadhaar number"
                    maxlength="12"
                    pattern="[0-9]{12}"
                    value="<%= request.getAttribute("confirmAadhaar") != null ? request.getAttribute("confirmAadhaar") : "" %>"
                    required>
                <div class="helper-text">Must match the Aadhaar number entered above exactly.</div>
                <% if (errors != null && errors.containsKey("confirmAadhaar")) { %>
                    <div class="field-error-msg"><%= errors.get("confirmAadhaar") %></div>
                <% } %>
            </div>

            <%-- Submit Button --%>
            <button type="submit" class="btn-submit">Submit Registration</button>
        </form>

        <div class="footer-note">
            Built with Java Servlet, JSP, and Apache Tomcat 9.0
        </div>
    </div>
</div>

</body>
</html>
