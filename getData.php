<?php 

//ini_set('max_execution_time', 30000);

$proccess = 0;

$code = $_GET['code'];

// print('Please wait while we fetch the email thread for the claim number : '.$code.'.');

?>
<!doctype html>
<html lang="en">

<head>
  
</head>

<body>
    <font>It will take a few seconds while we fetch the email thread for the Subject Containing : <?php echo $code; ?> </font>&nbsp;&nbsp;&nbsp;
<input type="button" value="I Understand" onclick="window.open('printData.php?code=<?php echo $code; ?>','_self','width=600,height=400')"> 
</body>

</html>