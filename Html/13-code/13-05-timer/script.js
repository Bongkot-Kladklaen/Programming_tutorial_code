window.onload = function () { 
	var myImage = document.getElementById("mainImage");
	imageArray= ["images/1.png","images/2.png","images/3.png","images/4.png","images/5.png","images/6.png"];
	imageIndex= 0;

	function changeMyImage(){
		myImage.setAttribute("src",imageArray[imageIndex]);
		imageIndex++;
		if (imageIndex >= imageArray.length) {
			imageIndex = 0;
		}
	}

	var mySetChange = setInterval(changeMyImage,3000); 
	//เก็บ Interval ลงในตัวแปร ซึ่งเป็นการเก็บลงในหน่วยความจำ
	//ข้อดีคือ สามารถใช้ซ้ำในส่วนต่างๆ ของเว็บเพจได้

	myImage.onclick = function(){
		clearInterval(mySetChange); //ล้างค่า Interval ในหน่วยความจำ
		alert("Stop!");
	}
}