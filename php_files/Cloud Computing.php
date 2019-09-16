<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
@import url(https://fonts.googleapis.com/css?family=Open+Sans);

body{
  background: #f2f2f2;
  font-family: 'Open Sans', sans-serif;
}
.menu{
	width: 100%;
	height: 100px;
	background-color: rgba(0,0,0,0.5);
}

.leftmenu{
	width: 25%;
	line-height: 70px;
	float: left;
	
}

.leftmenu h4{
	padding-left: 70px;
	padding-top: 10px;
	font-weight: bold;
	font-size: 20px;
	font-family: 'Comfortaa', cursive;
	color: white;
}

.rightmenu{
	width: 75%;
	height: 100px;
	float: right;
}

.rightmenu .list a{
	color: orange;
	cursor: pointer;
}

.rightmenu ul{
	margin-left:  700px; 
}

.rightmenu ul li{
	font-family: 'Comfortaa', cursive;
	display:inline-block;
	list-style: none;
	font-size: 17px;
	color: #fff;
	font-weight: bold;
	line-height: 100px;
	margin-left: 40px;
	text-transform: uppercase;


}


.firstlist{
	text-decoration-color: orange;
	cursor: pointer;
	
}

.rightmenu ul li:hover{
	color: orange;
}
.search {
  width: 100%;
  margin-top:10%
  position: relative
}

.searchTerm {
  float: left;
  width: 100%;
  border: 3px solid orange;
  padding: 5px;
  height: 20px;
  border-radius: 5px;
  outline: none;
  color: black;
}

.searchTerm:focus{
  color: black;
}

.searchButton {
  position: absolute;  
  right: -50px;
  width: 40px;
  height: 36px;
  border: 1px solid #00B4CC;
  background: orange;
  text-align: center;
  color: #fff;
  border-radius: 5px;
  cursor: pointer;
  font-size: 20px;
}

/*Resize the wrap to see the search bar change!*/
.wrap{
  width: 40%;
  position: absolute;
  top: 10%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.floatLeft { width: 30%; float: left; }
.floatRight {width: 70%; float: right; }
.container { overflow: hidden; }
.border{
margin-left:200px;
border:1px solid black;
background-color:#d9d9d9	;
width:80%;
}


</style>
<body>
<div class="bgimage">
        <div class="menu">
                <div class="leftmenu">
                    <h4>COURSEGEN</h4>
                </div>

                <div class="rightmenu">
                    <ul>
                        <li class="list"><a href="register.php">SIGN UP</a></li>
						<li class="list"><a href="login.php">LOGIN</a></li>
                        <li class="firstlist"></li>
                    </ul>
                </div>
            </div>
        </div>
<div class="wrap">
   <div class="search">
      <input type="text" class="searchTerm" value="Cloud Computing">
      <button type="submit" class="searchButton">
        <i class="fa fa-search"></i>
     </button>
   </div>
</div>
<br><br><br><br><br>

<?php
 $con=mysqli_connect("localhost","root","","db");
 $sql="SELECT * FROM cc WHERE domain='cloud computing' ORDER BY positive;";
 $result=mysqli_query($con,$sql);
 $resultcheck =mysqli_num_rows($result);
 if ($resultcheck > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {?>
<div class="border">
<div class="container">

<table><tr><th  colspan="2">
<?php echo "<b>".$row["course_name"]."</b><br>"?></th></tr>
<tr><th colspan="2">&nbsp </th></tr>
<tr><td rowspan="6" width="50%">
<img src="<?php echo $row["course_image"];?>" alt="not found" width=300 height=250>
</td>
<td><?php echo "&nbsp&nbsp&nbsp <b>PROVIDER</b> -&nbsp  ".$row["provider"]?></td>
</tr>
<tr><td>
<?php echo "&nbsp&nbsp&nbsp <b>LEVEL</b> -&nbsp  ".$row["course_level"]?></td>
</tr>
<tr><td>
<?php echo "&nbsp&nbsp&nbsp <b>DURATION</b> - &nbsp ".$row["course_duration"];?></td>
</tr>
<tr><td>
<?php echo "&nbsp&nbsp&nbsp <b>PRICE</b> -&nbsp  ".$row["course_price"]?></td>
</tr>
<tr><td>
<?php echo "&nbsp&nbsp&nbsp <b>POSITIVE</b> - &nbsp ".$row["positive"]."%";?></td>
</tr>
<tr><td>
<?php echo "&nbsp&nbsp&nbsp <b>NEGATIVE</b> - &nbsp ".$row["negative"]."%";?></td>
</tr>
<tr>
<td colspan="2">
<a href="<?php echo $row['course_url'];?>" target="blank"><img src="download.png" alt="image not found" height="35px" width="100px" style="float:right"></a>
</td>
</tr>
</table>

</div></div><br><br>

    <?php    
    }echo "<br><br>";
} else {
    echo "<center>0 results</center>";
} ?>

</body>