package com.example;

import java.io.Serializable;

/**
 * Person JavaBean representing a registered person.
 * 
 * Demonstrates Core Java Concepts:
 * 1. Encapsulation: All instance variables are private with public getters/setters.
 * 2. Default Constructor: No-arg constructor required by JavaBeans specification.
 * 3. Parameterized Constructors: Multi-arg constructors with constructor chaining via this().
 * 4. Validation inside Setters: Guarantees object state integrity.
 * 5. Serialization: Implements java.io.Serializable with serialVersionUID.
 */
public class Person implements Serializable {

    // Unique identifier for Serializable class version compatibility
    private static final long serialVersionUID = 1L;

    // Encapsulated (private) data members
    // We use String for phoneNumber and aadhaarNumber to preserve leading zeros
    // and avoid arithmetic overflow (12 digits exceed standard 32-bit int).
    private String firstName;
    private String lastName;
    private String phoneNumber;
    private String aadhaarNumber;

    /**
     * 1. Default (No-Argument) Constructor
     * Mandatory for JavaBeans, frameworks, and reflection-based tools.
     */
    public Person() {
        // Initializes fields to default values (null)
    }

    /**
     * 2. Parameterized Constructor (3 arguments)
     * Initializes basic identity: first name, last name, and phone number.
     * Uses setter methods so that validation rules are strictly enforced.
     */
    public Person(String firstName, String lastName, String phoneNumber) {
        setFirstName(firstName);
        setLastName(lastName);
        setPhoneNumber(phoneNumber);
    }

    /**
     * 3. Parameterized Constructor (4 arguments)
     * Demonstrates Constructor Chaining using this(firstName, lastName, phoneNumber).
     * Reuses the 3-parameter constructor logic to avoid redundant code.
     */
    public Person(String firstName, String lastName, String phoneNumber, String aadhaarNumber) {
        // Constructor Chaining: Calls the 3-arg constructor
        this(firstName, lastName, phoneNumber);
        // Sets and validates the fourth field
        setAadhaarNumber(aadhaarNumber);
    }

    // ==========================================
    // GETTERS AND SETTERS (WITH VALIDATION)
    // ==========================================

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        if (firstName == null || firstName.trim().isEmpty()) {
            throw new IllegalArgumentException("First name cannot be empty.");
        }
        if (!firstName.trim().matches("^[a-zA-Z\\s]+$")) {
            throw new IllegalArgumentException("First name must contain only letters and spaces.");
        }
        this.firstName = firstName.trim();
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        if (lastName == null || lastName.trim().isEmpty()) {
            throw new IllegalArgumentException("Last name cannot be empty.");
        }
        if (!lastName.trim().matches("^[a-zA-Z\\s]+$")) {
            throw new IllegalArgumentException("Last name must contain only letters and spaces.");
        }
        this.lastName = lastName.trim();
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        if (phoneNumber == null || phoneNumber.trim().isEmpty()) {
            throw new IllegalArgumentException("Phone number cannot be empty.");
        }
        String cleanPhone = phoneNumber.trim();
        // Phone number must contain exactly 10 digits
        if (!cleanPhone.matches("^\\d{10}$")) {
            throw new IllegalArgumentException("Phone number must contain exactly 10 numeric digits.");
        }
        this.phoneNumber = cleanPhone;
    }

    public String getAadhaarNumber() {
        return aadhaarNumber;
    }

    public void setAadhaarNumber(String aadhaarNumber) {
        if (aadhaarNumber == null || aadhaarNumber.trim().isEmpty()) {
            throw new IllegalArgumentException("Aadhaar number cannot be empty.");
        }
        String cleanAadhaar = aadhaarNumber.trim();
        // Aadhaar number must contain exactly 12 digits
        if (!cleanAadhaar.matches("^\\d{12}$")) {
            throw new IllegalArgumentException("Aadhaar number must contain exactly 12 numeric digits.");
        }
        this.aadhaarNumber = cleanAadhaar;
    }

    /**
     * Helper method to safely mask the Aadhaar number for security and privacy.
     * Masking hides the first 8 digits and reveals only the last 4 digits (e.g. "XXXXXXXX1234").
     */
    public String getMaskedAadhaar() {
        if (aadhaarNumber != null && aadhaarNumber.length() == 12) {
            return "XXXXXXXX" + aadhaarNumber.substring(8);
        }
        return "N/A";
    }

    /**
     * Returns full name convenience property.
     */
    public String getFullName() {
        return (firstName != null ? firstName : "") + " " + (lastName != null ? lastName : "");
    }

    @Override
    public String toString() {
        return "Person{" +
                "firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", phoneNumber='" + phoneNumber + '\'' +
                ", aadhaarNumber='" + getMaskedAadhaar() + '\'' +
                '}';
    }
}
