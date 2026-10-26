package com.example;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

/**
 * SerializationDemo
 * 
 * Standalone demonstration showing how Java Serialization and Deserialization work
 * with the Person class.
 * 
 * Concepts demonstrated:
 * 1. ObjectOutputStream.writeObject() -> Converts Person object to byte stream (saved to person.ser).
 * 2. ObjectInputStream.readObject()   -> Reconstructs Person object from byte stream back into heap memory.
 * 3. Serializable interface and serialVersionUID usage.
 */
public class SerializationDemo {

    public static void main(String[] args) {
        String filename = "person.ser";

        System.out.println("==================================================");
        System.out.println("     JAVA OBJECT SERIALIZATION DEMO");
        System.out.println("==================================================");

        // 1. Create a Person object
        Person originalPerson = new Person("Piyush", "Kumar", "9876543210", "123456789012");
        System.out.println("\n[1] Original Person Object Created:");
        System.out.println("    Name:    " + originalPerson.getFullName());
        System.out.println("    Phone:   " + originalPerson.getPhoneNumber());
        System.out.println("    Aadhaar: " + originalPerson.getMaskedAadhaar());

        // 2. Serialize the Person object into a byte file
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filename))) {
            oos.writeObject(originalPerson);
            System.out.println("\n[2] Serialization Successful!");
            System.out.println("    Person object converted to bytes and saved to file: " + filename);
        } catch (Exception e) {
            System.err.println("Serialization failed: " + e.getMessage());
            e.printStackTrace();
            return;
        }

        // 3. Deserialize the byte file back into a new Person object
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filename))) {
            Person deserializedPerson = (Person) ois.readObject();
            System.out.println("\n[3] Deserialization Successful!");
            System.out.println("    Byte stream read from file and reconstructed into Person object:");
            System.out.println("    Name:    " + deserializedPerson.getFullName());
            System.out.println("    Phone:   " + deserializedPerson.getPhoneNumber());
            System.out.println("    Aadhaar: " + deserializedPerson.getMaskedAadhaar());
            System.out.println("    toString(): " + deserializedPerson);
        } catch (Exception e) {
            System.err.println("Deserialization failed: " + e.getMessage());
            e.printStackTrace();
        } finally {
            // Clean up the temporary serialized file
            File file = new File(filename);
            if (file.exists()) {
                file.delete();
                System.out.println("\n[4] Cleaned up temporary file: " + filename);
            }
        }

        System.out.println("\n==================================================");
        System.out.println("Demo completed successfully!");
        System.out.println("==================================================");
    }
}
