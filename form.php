<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Input Form</title>
</head>
<body>
    <h1>Enter Five Numbers</h1>
    <form action="process.php" method="get">
        <label for="a">First:</label>
        <input type="number" name="a" id="a" required><br>
        
        <label for="b">Second:</label>
        <input type="number" name="b" id="b" required><br>
        
        <label for="c">Third :</label>
        <input type="number" name="c" id="c" required><br>
        
        <label for="d">Fourth:</label>
        <input type="number" name="d" id="d" required><br>
        
        <label for="e">fifth:</label>
        <input type="number" name="e" id="e" required><br>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>
