<?php
$a = $_GET['a'] ?? '';
$b = $_GET['b'] ?? '';
$c = $_GET['c'] ?? '';
$d = $_GET['d'] ?? '';
$e = $_GET['e'] ?? '';

$command = escapeshellcmd("python3 data_management.py $a $b $c $d $e");
$output = shell_exec($command);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Processing Results</title>
</head>
<body>
    <h2>Results</h2>
    <?php
    echo $output;
    ?>
</body>
</html>
