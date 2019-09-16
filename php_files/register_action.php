<?php

if(isset($_POST['register']))

{



   $firstname=$_POST['firstname'];
   
   $lastname=$_POST['lastname'];
   
   $interests=$_POST['interests'];

   $email=$_POST['email'];

   $password=$_POST['password_1'];

   $password_confirm=$_POST['password_2'];
   

   if($password_confirm==$password)

   {
			$con=mysqli_connect("localhost","root","","db");
			$sql="SELECT * FROM users WHERE email='$email';";
			$result=mysqli_query($con,$sql);
			$resultcheck =mysqli_num_rows($result);
			if($resultcheck>0){
				header("Location:register.php?signup=usertaken");
				exit();
			}
   
else{
      mysqli_query($con,"insert into users values('$firstname','$lastname','$email','$interests','$password')");
	  
	   session_start();

        $_SESSION['uname']=$email;

      header('Location:userhome.php');

   }}

   else

   {

    header('Location:register.php?signup=passwordandconfirmpasswordmismatch');

   }



}

?>