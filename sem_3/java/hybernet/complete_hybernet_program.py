
# ============================================================
# COMPLETE HIBERNATE CRUD PROJECT
# All project files explained in one Python file
# ============================================================

'''
PROJECT STRUCTURE:

HibernateProject/
|
|-- pom.xml
|
|-- src/
    |
    |-- main/
        |
        |-- java/
        |   |
        |   |-- com/example/
        |       |
        |       |-- Student.java
        |       |-- HibernateUtil.java
        |       |-- Main.java
        |
        |-- resources/
            |
            |-- hibernate.cfg.xml


PROJECT REQUIREMENTS:
1. Java 17
2. Maven
3. MySQL
4. Hibernate ORM
5. MySQL Connector/J
'''

# ============================================================
# 1. DATABASE CREATION
# ============================================================

'''
Execute the following SQL in MySQL Workbench.

CREATE DATABASE college;

USE college;

-- Hibernate will automatically create the student table.
-- We do not need to create the table manually.

SELECT * FROM student;
'''


# ============================================================
# 2. pom.xml
# ============================================================

'''
LOCATION:
HibernateProject/pom.xml

PURPOSE:
- Manages project dependencies.
- Downloads Hibernate.
- Downloads MySQL Connector.
- Configures Java version.
'''

POM_XML = r"""
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         https://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>HibernateProject</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>

        <!-- Hibernate ORM -->
        <dependency>
            <groupId>org.hibernate.orm</groupId>
            <artifactId>hibernate-core</artifactId>
            <version>6.6.15.Final</version>
        </dependency>

        <!-- MySQL Connector -->
        <dependency>
            <groupId>com.mysql</groupId>
            <artifactId>mysql-connector-j</artifactId>
            <version>9.2.0</version>
        </dependency>

        <!-- Logging -->
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-simple</artifactId>
            <version>2.0.17</version>
        </dependency>

    </dependencies>

</project>
"""


# ============================================================
# 3. hibernate.cfg.xml
# ============================================================

'''
LOCATION:
src/main/resources/hibernate.cfg.xml

PURPOSE:
- Connects Java application to MySQL.
- Defines database username and password.
- Configures Hibernate.
- Registers the Student entity.
'''

HIBERNATE_CONFIG = r"""
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE hibernate-configuration PUBLIC
        "-//Hibernate/Hibernate Configuration DTD 3.0//EN"
        "http://hibernate.org/dtd/hibernate-configuration-3.0.dtd">

<hibernate-configuration>

    <session-factory>

        <!-- Database Driver -->
        <property name="hibernate.connection.driver_class">
            com.mysql.cj.jdbc.Driver
        </property>

        <!-- Database URL -->
        <property name="hibernate.connection.url">
            jdbc:mysql://localhost:3306/college
        </property>

        <!-- Username -->
        <property name="hibernate.connection.username">
            root
        </property>

        <!-- Password -->
        <property name="hibernate.connection.password">
            your_password
        </property>

        <!-- SQL Dialect -->
        <property name="hibernate.dialect">
            org.hibernate.dialect.MySQLDialect
        </property>

        <!-- Display SQL queries -->
        <property name="hibernate.show_sql">true</property>

        <property name="hibernate.format_sql">true</property>

        <!-- Automatically update table -->
        <property name="hibernate.hbm2ddl.auto">update</property>

        <!-- Entity Mapping -->
        <mapping class="com.example.Student"/>

    </session-factory>

</hibernate-configuration>
"""


# ============================================================
# 4. Student.java
# ============================================================

'''
LOCATION:
src/main/java/com/example/Student.java

PURPOSE:
- Entity class.
- Maps Java Student objects to the database student table.
- Contains fields, constructors, getters and setters.

ANNOTATIONS:

@Entity
    Marks the class as a Hibernate entity.

@Table
    Specifies the database table name.

@Id
    Defines the primary key.

@GeneratedValue
    Automatically generates the ID.

@Column
    Customizes the database column.

@Transient
    Excludes a field from database persistence.
'''

STUDENT_JAVA = r"""
package com.example;

import jakarta.persistence.*;

@Entity
@Table(name = "student")
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "student_name", length = 50)
    private String name;

    private int age;

    // Default constructor
    public Student() {
    }

    // Parameterized constructor
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getter for ID
    public int getId() {
        return id;
    }

    // Setter for ID
    public void setId(int id) {
        this.id = id;
    }

    // Getter for name
    public String getName() {
        return name;
    }

    // Setter for name
    public void setName(String name) {
        this.name = name;
    }

    // Getter for age
    public int getAge() {
        return age;
    }

    // Setter for age
    public void setAge(int age) {
        this.age = age;
    }

    // Display student details
    @Override
    public String toString() {

        return "Student{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
"""


# ============================================================
# 5. HibernateUtil.java
# ============================================================

'''
LOCATION:
src/main/java/com/example/HibernateUtil.java

PURPOSE:
- Creates SessionFactory.
- Loads hibernate.cfg.xml.
- Provides SessionFactory to Main.java.

IMPORTANT:

Configuration:
    Reads Hibernate configuration.

SessionFactory:
    Creates Session objects.

Session:
    Performs database operations.
'''

HIBERNATE_UTIL_JAVA = r"""
package com.example;

import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class HibernateUtil {

    // Create SessionFactory only once
    private static final SessionFactory factory =
            new Configuration()
                    .configure("hibernate.cfg.xml")
                    .buildSessionFactory();

    // Return SessionFactory
    public static SessionFactory getSessionFactory() {
        return factory;
    }

    // Close SessionFactory
    public static void shutdown() {
        factory.close();
    }
}
"""


# ============================================================
# 6. Main.java
# ============================================================

'''
LOCATION:
src/main/java/com/example/Main.java

PURPOSE:
Performs all four CRUD operations.

CRUD:

C = CREATE  -> INSERT
R = READ    -> SELECT
U = UPDATE  -> UPDATE
D = DELETE  -> DELETE

IMPORTANT METHODS:

session.persist()
    Inserts a new entity.

session.find()
    Finds an entity using its primary key.

session.remove()
    Deletes an entity.

tx.commit()
    Commits the transaction.

tx.rollback()
    Rolls back the transaction.
'''

MAIN_JAVA = r"""
package com.example;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import java.util.List;

public class Main {

    public static void main(String[] args) {

        // Get SessionFactory
        SessionFactory factory =
                HibernateUtil.getSessionFactory();

        // 1. CREATE
        insertStudents(factory);

        // 2. READ
        readStudents(factory);

        // 3. UPDATE
        updateStudent(factory, 1);

        // 4. DELETE
        deleteStudent(factory, 2);

        // Close SessionFactory
        HibernateUtil.shutdown();
    }


    // =================================
    // 1. INSERT / CREATE
    // =================================

    public static void insertStudents(SessionFactory factory) {

        Transaction tx = null;

        try (Session session = factory.openSession()) {

            // Begin transaction
            tx = session.beginTransaction();

            // Create objects
            Student s1 = new Student("Piyush", 23);
            Student s2 = new Student("Rahul", 24);
            Student s3 = new Student("Aman", 22);

            // Persist one object at a time
            session.persist(s1);
            session.persist(s2);
            session.persist(s3);

            // Commit transaction
            tx.commit();

            System.out.println("Students inserted successfully!");

        } catch (Exception e) {

            if (tx != null && tx.isActive()) {
                tx.rollback();
            }

            e.printStackTrace();
        }
    }


    // =================================
    // 2. READ / SELECT
    // =================================

    public static void readStudents(SessionFactory factory) {

        try (Session session = factory.openSession()) {

            // HQL query
            List<Student> students =
                    session.createQuery(
                            "FROM Student", Student.class
                    ).list();

            System.out.println("\nStudent Records:");

            // Display all students
            for (Student s : students) {
                System.out.println(s);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }


    // =================================
    // 3. UPDATE
    // =================================

    public static void updateStudent(
            SessionFactory factory, int id) {

        Transaction tx = null;

        try (Session session = factory.openSession()) {

            tx = session.beginTransaction();

            // Find student by ID
            Student s = session.find(Student.class, id);

            if (s != null) {

                // Update fields
                s.setName("Updated Piyush");
                s.setAge(25);

                // Hibernate automatically detects
                // changes to this managed entity.

                tx.commit();

                System.out.println("\nStudent updated successfully!");

            } else {

                System.out.println("Student not found!");

                tx.rollback();
            }

        } catch (Exception e) {

            if (tx != null && tx.isActive()) {
                tx.rollback();
            }

            e.printStackTrace();
        }
    }


    // =================================
    // 4. DELETE
    // =================================

    public static void deleteStudent(
            SessionFactory factory, int id) {

        Transaction tx = null;

        try (Session session = factory.openSession()) {

            tx = session.beginTransaction();

            // Find student
            Student s = session.find(Student.class, id);

            if (s != null) {

                // Delete student
                session.remove(s);

                tx.commit();

                System.out.println("\nStudent deleted successfully!");

            } else {

                System.out.println("Student not found!");

                tx.rollback();
            }

        } catch (Exception e) {

            if (tx != null && tx.isActive()) {
                tx.rollback();
            }

            e.printStackTrace();
        }
    }
}
"""


# ============================================================
# 7. EXPECTED OUTPUT
# ============================================================

'''
On the first run, assuming the table is empty:

Students inserted successfully!

Student Records:

Student{id=1, name='Piyush', age=23}
Student{id=2, name='Rahul', age=24}
Student{id=3, name='Aman', age=22}

Student updated successfully!

Student deleted successfully!

NOTE:
The generated IDs may differ if records already exist.
The example updates ID 1 and deletes ID 2.
'''


# ============================================================
# 8. HIBERNATE ARCHITECTURE
# ============================================================

'''
                 JAVA APPLICATION
                        |
                        v
                  Configuration
                        |
                        v
                  SessionFactory
                        |
                        v
                     Session
                        |
                        v
                   Transaction
                        |
                        v
                  Hibernate ORM
                        |
                        v
                       JDBC
                        |
                        v
                 MYSQL DATABASE


REMEMBER:

Configuration    = Reads configuration
SessionFactory   = Creates Sessions
Session          = Performs operations
Transaction      = Commit / Rollback
Hibernate        = ORM framework
JDBC             = Database communication
'''


# ============================================================
# 9. CRUD QUICK REVISION
# ============================================================

'''
CREATE:
    session.persist(s1);

READ:
    session.find(Student.class, 1);

UPDATE:
    Student s = session.find(Student.class, 1);
    s.setName("New Name");
    tx.commit();

DELETE:
    Student s = session.find(Student.class, 1);
    session.remove(s);
    tx.commit();


FINAL FLOW:

Java Object
    |
    v
Entity Mapping
    |
    v
Session
    |
    v
Transaction
    |
    v
Hibernate
    |
    v
JDBC
    |
    v
Database
'''


# ============================================================
# 10. IMPORTANT
# ============================================================

'''
THIS IS A PYTHON REFERENCE FILE, NOT A RUNNABLE HIBERNATE
APPLICATION.

Python stores the Java and XML source code as multiline strings.

To actually execute Hibernate:

1. Create the Maven project.
2. Copy POM_XML into pom.xml.
3. Copy HIBERNATE_CONFIG into hibernate.cfg.xml.
4. Copy STUDENT_JAVA into Student.java.
5. Copy HIBERNATE_UTIL_JAVA into HibernateUtil.java.
6. Copy MAIN_JAVA into Main.java.
7. Configure your MySQL password.
8. Run Main.java.

You cannot execute Hibernate Java code directly using Python.
'''
