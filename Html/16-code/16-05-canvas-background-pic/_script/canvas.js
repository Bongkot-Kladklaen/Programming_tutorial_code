function drawCanvas(){
	var context = document.getElementById('myCanvas').getContext('2d');
	var bgImage = new Image(); 			//สร้างออบเจ็กต์ที่เป็นรูปภาพ
	bgImage.src = '_images/bg.png';  	//เลือกภาพไปใส่ในออบเจ็กต์
	bgImage.onload = function (){    	//ฟังก์ชันเมื่อมีการโหลดภาพ
		var myBackground = context.createPattern(bgImage,'repeat');
	    context.fillStyle = myBackground; 
		context.fillRect(10,10,200,200);
	}
}
drawCanvas();