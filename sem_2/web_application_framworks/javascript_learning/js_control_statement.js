function runProgram() {
    let output = "";

    // While loop
    output += "<h3>While loop:</h3>";
    let i = 1;
    while (i <= 5) {
        output += "Number: " + i + "<br>";
        i++;
    }

    // For Loop
    output += "<h3>For Loop:</h3>";
    for (let j = 1; j <= 5; j++) {
        if (j === 3) {
            continue;
        }
        if (j === 5) {
            break;
        }
        output += "Value: " + j + "<br>";
    }

    // Do while
    output += "<h3>Do While loop:</h3>";
    let k = 1;
    do {
        output += "Count: " + k + "<br>";
        k++;
    } while (k <= 3);

    // Switch statement
    output += "<h3>Switch statement:</h3>";
    let day = new Date().getDay();

    switch (day) {
        case 0: 
        output += "Sunday"; 
        break;

        case 1: 
        output += "Monday"; 
        break;

        case 2: 
        output += "Tuesday";
         break;

        case 3: 
        output += "Wednesday"; 
        break;

        case 4: 
        output += "Thursday"; 
        break;

        case 5: 
        output += "Friday"; 
        break;

        case 6: 
        output += "Saturday"; 
        break;
        
        default:
             output += "Invalid day";
    }

    // Window Object Model
    output += "<h3>Window Object Model:</h3>";
    output += "Width: " + window.innerWidth + "<br>";
    output += "Height: " + window.innerHeight + "<br>";

    alert("Program executed successfully!");

    document.getElementById("output").innerHTML = output;
}