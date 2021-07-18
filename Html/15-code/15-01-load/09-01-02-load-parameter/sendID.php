<?php
$id = $_REQUEST['myID'];
if ($id==1) {
	$name = 'jeerawuth';
} else {
	$name = 'Other';
}
?>
<html>
<head></head>
<body>
	<div><?php echo 'Student name is : '.$name;?></div>
</body>
</html>