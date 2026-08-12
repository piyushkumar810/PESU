// Import Student component
import Student from "../components/Student";

// Import Layout component
import Layout from "../components/Layout";

// Import Product component
import Product from "../components/Product";

// Import Card component
import Card from "../components/Card";

import Button from "../components/Button";
import StudentInfo from "../components/StudentInfo";

export default function Home() {

    // =====================================================
    // 1. MULTIPLE TYPED PROPS - PRODUCT
    // =====================================================

    // Creating an object containing Product props
    const productProps = {
        name: "Laptop",
        price: 50000
    };

    // Calling Product function and printing the result
    console.log(Product(productProps));


    // =====================================================
    // 2. CHILDREN + ANOTHER PROP - CARD
    // =====================================================

    // Card with children as a string
    const card1 = Card({
        title: "Welcome",
        children: "to NextJS"
    });

    // Card with children as a string array
    const card2 = Card({
        title: "Topics",
        children: ["TypeScript", "React", "NextJS"]
    });

    // Printing Card results in the console
    console.log(card1);
    console.log(card2);


    const saveButton = {
    label: "Save",
    onClick: () => {
        console.log("Save button clicked.");
    }
    };
    
    console.log(Button(saveButton));
    
    
    const studentInfo = {
        name: "Akansha",
        age: 20,
        course: "MCA",
        subjects: ["Java", "Python", "DBMS"]
    };
    
    console.log(StudentInfo(studentInfo));


    // =====================================================
    // RETURN - DISPLAY CONTENT IN BROWSER
    // =====================================================

    return (
    <div>

        {/* 1. BASIC TYPED PROPS - STUDENT */}
        <h2>Executing Prop Types in NextJS</h2>

        <Student
            name="Akansha"
            age={20}
            course="MCA"
        />

        <hr />

        {/* 2. CHILDREN PROP - LAYOUT */}
        <h2>Children Props</h2>

        <Layout>
            Welcome to NextJS
        </Layout>

        <hr />

        {/* 3. MULTIPLE TYPED PROPS - PRODUCT */}
        <h2>Multiple Typed Props</h2>

        <p>
            Product: {productProps.name}
        </p>

        <p>
            Price: ₹{productProps.price}
        </p>

        <hr />

        {/* 4. CHILDREN + ANOTHER PROP - CARD */}
        <h2>Children with Another Prop</h2>

        <p>
            {card1}
        </p>

        <p>
            {card2}
        </p>

        <hr />

        {/* 5. FUNCTION PROP - BUTTON */}
        <h2>Function Prop</h2>

        <button onClick={saveButton.onClick}>
            {saveButton.label}
        </button>

        <hr />

        {/* 6. STUDENT INFORMATION CARD */}
        <h2>Student Information Card</h2>

        <p>Name: {studentInfo.name}</p>

        <p>Age: {studentInfo.age}</p>

        <p>Course: {studentInfo.course}</p>

        <p>
            Subjects: {studentInfo.subjects.join(", ")}
        </p>

    </div>
  );
}