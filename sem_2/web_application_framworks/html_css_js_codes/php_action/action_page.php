<!DOCTYPE html>
<html>
<head>
<title>Form Result</title>
</head>

<body>

<h2>Browser Selection Result</h2>

<?php

if(isset($_GET["browser"])) {

    $browser = htmlspecialchars($_GET["browser"]);

    echo "<p>You selected browser: <b>$browser</b></p>";

}
else {

    echo "<p>No browser selected.</p>";

}

?>

<br>
<a href="index.html">Go Back</a>

</body>
</html>