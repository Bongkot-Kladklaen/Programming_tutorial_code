<?php 
if(isset($_GET['branch'])){
	$myInput = $_GET['branch'];
	$selectShop= getResult($myInput); 
	echo $selectShop; 
}
function getResult($myCat){ 
	switch ($myCat) { 
	case 'jShop': 
		$shop['telephone']='024111111'; 
		$shop['address']='MK Tower'; 
		break; 
	case 'SiamShop': 
		$shop['telephone']='024222222'; 
		$shop['address']='Twin Tower'; 
		break; 
	case 'ByteMe': 
		$shop['telephone']='024333333'; 
		$shop['address']='Singha Place'; 
		break; 
	} 
	$strResult=json_encode($shop); 
	return $strResult; 
} 
?>