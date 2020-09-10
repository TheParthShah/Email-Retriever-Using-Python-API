<?php 

ini_set('max_execution_time', 30000);
$code = $_GET['code'];


$result = exec("pythonFullURL emailAPI.py $code",$output);

$msg = htmlspecialchars_decode(str_replace('\r\n' , ' ', $output['0']));
$msg  = htmlspecialchars_decode(str_replace('["' , '', $msg));
$msg  = htmlspecialchars_decode(str_replace('"]' , '', $msg));
print_r($msg);

?>