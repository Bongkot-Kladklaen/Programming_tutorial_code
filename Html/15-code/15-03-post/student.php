<?php 
if(isset($_POST['id'])){
	$myInput = $_POST['id'];
	$selectStudent= getResult($myInput); 
	echo $selectStudent; 
}
function getResult($myId){ 
	switch ($myId) { 
		case '1': 
			$student['name']='Jeerawuth Varin'; 
			$student['studentClass']='1/1'; 
			break; 
		case '2': 
			$student['name']='Somchi Thongdee'; 
			$student['studentClass']='1/2'; 
			break; 
		case '12': 
			$student['name']='Eakarak Kaminthong'; 
			$student['studentClass']='2/1'; 
			break;
		default: 
			$student['name']='No student found'; 
			$student['studentClass']=''; 
			break;
	} 
	$strResult=json_encode($student); 
	return $strResult; 
} 
?>