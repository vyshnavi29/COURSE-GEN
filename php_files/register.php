<!DOCTYPE html>
<html>
<head>
	<title>Register Here!!!</title>
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
    		<h1>Register</h1>
			<br>
    		
    		<form name="f1" method="post" action="registeraction.php">
                

                <div class="inputbox">
    			<input type="text" name="firstname" required="">
                <label>Enter First Name</label>
                </div>

                <div class="inputbox">
                <input type="text" name="lastName" required="">
                <label>Enter Last Name</label>
                </div>

                <div class="inputbox">
    			<input type="text" name="interests" required="">
                <label>Enter interests</label>
                </div>

                <div class="inputbox">
    			<input type="text" name="email" required="">
                <label>Enter Email Address</label>
                </div>

                <div class="inputbox">
    			<input type="password" name="password_1" required="">
                <label>Enter Password</label>
                </div>

                <div class="inputbox">
                <input type="password" name="password_2" required="">
                <label>Enter Confirm Password</label>
                </div>

    			<input type="submit" name="register" value="submit">
                <br>
                <?php
     if(isset($_GET['signup']))
     {
      $signupCheck = $_GET['signup'];
      if ($signupCheck=='usertaken') {
        echo "<h3 id='sname'>Username already exists</h3>";
      }
	  else
		  echo "<h3 id='sname'>password and confirm password mismatch</h3>";
     }
    ?>
                <h2>Already have an account?</h2>
                <br>

    			<a href="login.php"><h3>Login here</h3></a>
    		</form>
    	</div>
    </div>
</body>
</html>
