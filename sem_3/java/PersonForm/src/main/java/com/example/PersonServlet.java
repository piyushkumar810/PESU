package com.example;

import java.io.IOException;
import java.util.LinkedHashMap;
import java.util.Map;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * PersonServlet: Controller servlet for Person Registration.
 * 
 * Demonstrates:
 * 1. Extending HttpServlet from javax.servlet.http (Tomcat 9 compatible).
 * 2. URL mapping with @WebServlet("/register").
 * 3. Reading form fields with request.getParameter().
 * 4. Comprehensive server-side validation.
 * 5. Creating a Person object and passing it via request.setAttribute().
 * 6. Forwarding navigation via RequestDispatcher.forward().
 */
@WebServlet("/register")
public class PersonServlet extends HttpServlet {

    private static final long serialVersionUID = 1L;

    /**
     * Handles GET requests: if user accesses /register directly in the browser,
     * forward them back to the registration form (index.jsp).
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        RequestDispatcher dispatcher = request.getRequestDispatcher("index.jsp");
        dispatcher.forward(request, response);
    }

    /**
     * Handles POST requests: processes form submission from index.jsp.
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // Ensure UTF-8 character encoding for submitted text
        request.setCharacterEncoding("UTF-8");

        // 1. Read input fields using request.getParameter()
        String firstName = request.getParameter("firstName");
        String lastName = request.getParameter("lastName");
        String phoneNumber = request.getParameter("phoneNumber");
        String aadhaarNumber = request.getParameter("aadhaarNumber");
        String confirmAadhaar = request.getParameter("confirmAadhaar");

        // 2. Data structure to collect validation error messages
        Map<String, String> errors = new LinkedHashMap<>();

        // 3. Server-side validation rules
        // First Name Validation
        if (firstName == null || firstName.trim().isEmpty()) {
            errors.put("firstName", "First name is required and cannot be blank.");
        } else if (!firstName.trim().matches("^[a-zA-Z\\s]+$")) {
            errors.put("firstName", "First name must contain letters and spaces only.");
        }

        // Last Name Validation
        if (lastName == null || lastName.trim().isEmpty()) {
            errors.put("lastName", "Last name is required and cannot be blank.");
        } else if (!lastName.trim().matches("^[a-zA-Z\\s]+$")) {
            errors.put("lastName", "Last name must contain letters and spaces only.");
        }

        // Phone Number Validation: exactly 10 digits
        if (phoneNumber == null || phoneNumber.trim().isEmpty()) {
            errors.put("phoneNumber", "Phone number is required.");
        } else if (!phoneNumber.trim().matches("^\\d{10}$")) {
            errors.put("phoneNumber", "Phone number must be exactly 10 digits (0-9).");
        }

        // Aadhaar Number Validation: exactly 12 digits
        if (aadhaarNumber == null || aadhaarNumber.trim().isEmpty()) {
            errors.put("aadhaarNumber", "Aadhaar number is required.");
        } else if (!aadhaarNumber.trim().matches("^\\d{12}$")) {
            errors.put("aadhaarNumber", "Aadhaar number must be exactly 12 digits (0-9).");
        }

        // Confirm Aadhaar Validation: must match Aadhaar Number
        if (confirmAadhaar == null || confirmAadhaar.trim().isEmpty()) {
            errors.put("confirmAadhaar", "Please confirm your Aadhaar number.");
        } else if (aadhaarNumber != null && !aadhaarNumber.trim().equals(confirmAadhaar.trim())) {
            errors.put("confirmAadhaar", "Confirm Aadhaar does not match the Aadhaar number entered.");
        }

        // 4. Check if validation failed
        if (!errors.isEmpty()) {
            // Validation failed! Attach errors and original input back to request
            request.setAttribute("errors", errors);
            request.setAttribute("firstName", firstName);
            request.setAttribute("lastName", lastName);
            request.setAttribute("phoneNumber", phoneNumber);
            request.setAttribute("aadhaarNumber", aadhaarNumber);
            request.setAttribute("confirmAadhaar", confirmAadhaar);

            // Forward back to index.jsp so the user can fix the errors without losing inputs
            RequestDispatcher dispatcher = request.getRequestDispatcher("index.jsp");
            dispatcher.forward(request, response);
            return;
        }

        // 5. Validation passed! Create the Person object
        try {
            // Instantiate Person using the 4-argument parameterized constructor
            Person person = new Person(
                firstName.trim(),
                lastName.trim(),
                phoneNumber.trim(),
                aadhaarNumber.trim()
            );

            // 6. Set attributes to share data with result.jsp
            request.setAttribute("person", person);
            request.setAttribute("confirmStatus", "Aadhaar Number Verified & Matched Successfully");

            // 7. Forward request to result.jsp
            RequestDispatcher dispatcher = request.getRequestDispatcher("result.jsp");
            dispatcher.forward(request, response);

        } catch (IllegalArgumentException ex) {
            // If internal setter validation fails unexpectedly
            errors.put("general", ex.getMessage());
            request.setAttribute("errors", errors);
            RequestDispatcher dispatcher = request.getRequestDispatcher("index.jsp");
            dispatcher.forward(request, response);
        }
    }
}
