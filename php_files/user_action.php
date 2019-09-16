<!DOCTYPE html>
<?php

         session_start();

?>
<html>
<head>
<style>
table {
    width: 100%;
    border-collapse: collapse;
}

table, td, th {
    border: 1px solid black;
    padding: 5px;
}

th {text-align: left;}
</style>
</head>
<body>

<?php
$q = $_GET['q'];
$r = $_SESSION["uname"];
echo "$r";
$con = mysqli_connect('localhost','root','','db');
if (!$con) {
    die('Could not connect: ' . mysqli_error($con));
}
$sql="insert into recommend(`user_mail`,`course_name`) values('".$q."','".$r."');";
$result = mysqli_query($con,$sql) or die("error: ".mysqli_error($con));

mysqli_close($con);
?>
</body>
</html>