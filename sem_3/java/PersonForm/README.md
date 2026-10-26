# Person Registration Web Application

A beginner-friendly Java Web Application built with **JSP**, **Java Servlet (javax.servlet)**, **HTML5**, **CSS3**, and **Apache Tomcat 9.0**.

## Project Features
- **Class & Object**: Object-oriented `Person` model.
- **Encapsulation**: Private fields, strict getters, and validation in setters.
- **Constructors**: Default constructor, parameterized constructors, and constructor chaining with `this()`.
- **Validation**:
  - Name presence & alpha validation.
  - 10-digit phone number validation (preserving leading zeros as String).
  - 12-digit Aadhaar number validation (preserving leading zeros as String).
  - Match validation between Aadhaar and Confirm Aadhaar.
- **Security**: Masks Aadhaar number (e.g., `XXXXXXXX1234`) on display.
- **Serialization**: Demonstrates `java.io.Serializable`, `serialVersionUID`, and object byte streaming.
- **MVC Architecture**:
  - **Model**: `Person.java`
  - **View**: `index.jsp` (form) and `result.jsp` (details)
  - **Controller**: `PersonServlet.java` (`javax.servlet.http.HttpServlet`)

## Directory Layout
```
PersonForm/
├── pom.xml
├── build_and_deploy.bat
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── Person.java
│   │   │           ├── PersonServlet.java
│   │   │           └── SerializationDemo.java
│   │   └── webapp/
│   │       ├── index.jsp
│   │       ├── result.jsp
│   │       ├── style.css
│   │       └── WEB-INF/
│   │           └── web.xml
```

## Running the Application
### Option A: Using the Automated Build Script
Run the `build_and_deploy.bat` file. It compiles all Java files with `javac`, packages `PersonForm.war`, and copies it to `C:\Program Files\Apache Software Foundation\Tomcat 9.0\webapps\`.

### Option B: Using Maven
```bash
mvn clean package
```
Copy `target/PersonForm.war` to Tomcat's `webapps/` folder.

### Accessing the Web App
1. Start Apache Tomcat 9.
2. Visit: `http://localhost:8050/PersonForm/`
