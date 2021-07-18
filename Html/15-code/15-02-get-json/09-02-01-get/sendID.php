<?php
$xName = $_GET['name'];
$xLast = $_GET['lastname'];
myShow($xName,$xLast);

function myShow($myname, $mylast){
	$full = $myname.' '.$mylast;
	echo $full;
}
?>