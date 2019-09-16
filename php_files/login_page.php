<!DOCTYPE html>
<html>
<head>
	<title>Login Here!!!</title>
	
	<link rel="stylesheet" type="text/css" href="log.css">
	
	<link href="https://fonts.googleapis.com/css?family=Comfortaa" rel="stylesheet">
</head>
<body>

	<div class="bgimage">
		<div class="menu">
				<div class="leftmenu">
					<h4>COURSEGEN</h4>
				</div>

				<div class="rightmenu">
					<ul>
						<li class="list"></li>
						<li class="firstlist"></li>
					</ul>
				</div>
			</div>
		</div>

		<div class="box">
	        <h1>Login</h1>
			<br><br>
			
	        <form name="f2" method="POST" action="loginaction.php">
	            <div class="inputbox">
	                <input type="text" name="email_id" required="">
	                <label>Enter Email address</label>
	            </div>
	             <div class="inputbox">
	                <input type="password" name="password" required="">
	                <label>Enter Password</label> 
	            </div>
	            <input type="submit" name="login" value="submit">
	            <br>
				<?php
    if(isset($_GET['login']))
     {
      $loginCheck = $_GET['login'];
      if($loginCheck== 'emptyfield'){
        echo "<h3 id='sname'>Enter all the fields</h3>";
      }
      elseif ($loginCheck=='Notfound') {
        echo "<h3 id='sname'>WRONG PASSWORD ENTERED</h3>";
      }
      elseif($loginCheck=='errorpwd'){
        echo "<h3 id='sname'>WRONG PASSWORD ENTERED</h3>";
      }
     }
?>

                <br>
                
    			<a href="register.php"><h3>Register here</h3></a>
    			<a href="resetpassword.php"><h4>Forgot Password?</h3></a>

	        </form>
			
	    </div>
	</div>

</body>
</html>
