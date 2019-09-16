<?php

  if(isset($_POST["login"]))

  {
	session_start();
    $email=$_POST['email_id'];
	$password=$_POST['password'];
	
	if (empty($email)||empty($password)) 
	{
		header("Location:login.php?login=emptyfield");
    	exit();
	} 
	else
	{
		$con=mysqli_connect("localhost","root","","db");
		$result=mysqli_query($con,"select * from users where email='$email' and password='$password'");
	
		if(mysqli_num_rows($result)==0)
		{
			header("Location:login.php?login=Notfound");
    		 exit();	
    	}
        else
		{
			$_SESSION['uname']=$email;
			header('Location:userhome.php');
			exit();
		}

  }}
else{
    	header("Location:login.php.php?login=error");
    	exit();
    }
?>