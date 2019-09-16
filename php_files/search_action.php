<!DOCTYPE html>
<?php

         session_start();

?>
<html>
<head>
	 <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

body {
  font-family: Arial, Helvetica, sans-serif;
}

/* Float four columns side by side */
.column {
	margin-top: 30px;
  float: left;
  width: 50%;
  padding: 10px 100px ;

}

/* Remove extra left and right margins, due to padding */
.row {margin: 0 -5px;}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
p
{
	text-align: center;
}
img
{
	background-size: cover;
	width:200px;
	height:100px;
	float:left;
}

/* Responsive columns */
@media screen and (max-width: 600px) {
  .column {
    width: 10%;
    display: block;
    margin-bottom: 20px;

  }
}

/* Style the counter cards */
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  padding: 16px;
  text-align: center;
  background-color: #f1f1f1;
}



</style>
</head>
<body>
	<nav class="navbar navbar-light bg-light">
  <a class="navbar-bran" href="userhome.php">HOME</a>
</nav>


 <div class="row">
  <div class="column">
    <div class="card" style="height:250px; background-image: url ("pq2.jpg") ;">
      <h3>ARTIFICIAL INTELLIGENCE</h3>
      
      <p><img src="pq2.jpg">Combine the power of Data Science, Machine Learning to create powerful AI for Real-World applications!.</p><br>
      <a href="ai1.php" ><button class="btn btn-primary" type="button" style="margin-left: 100px ;">Explore Courses</button> </a>
</button>
    </div>
  </div>

  <div class="column">
    <div class="card" style="height: 250px;">
      <h3>PYTHON</h3>
     
      <p> <img src="pq1.jpg" >Learn to use Python professionally, learning both Python 2 and Python 3!</p><br>
    <a href="python1.php" ><button class="btn btn-primary" type="button" style="margin-left: 100px ;">Explore Courses</button> </a>
</button>
    </div>
  </div>
  <br><br><br><br><br>
  <div class="row">
  <div class="column">
    <div class="card" style="height: 250px;">
      <h3>CLOUD COMPUTING</h3>
		
      <p><img src="dq4.jpg">Fundamental understanding of what is cloud computing.The evolution from traditional IT to cloud services</p><br>
           <a href="cc1.php" ><button class="btn btn-primary" type="button" style="margin-left: 100px ;">Explore Courses</button> </a>
</button>
    </div>
  </div>

  <div class="column">
    <div class="card" style="height: 250px;">
      <h3>INTERNET OF THINGS</h3>
      
      <p><img src="p2.jpg">Learn how to Independently Design, Code and Build IOT products.</p><br>
    <a href="iot1.php" ><button class="btn btn-primary" type="button" style="margin-left: 100px ;">Explore Courses</button> </a>
</button>
    </div>
  </div>
 

</body>
</html>
