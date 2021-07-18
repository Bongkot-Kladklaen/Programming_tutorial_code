function drawCanvas(){
	var canvas = document.getElementById('myCanvas');
	var context = canvas.getContext('2d');
	var degrees = 270;  	//กำหนดมุมเป็น 270 องศา
	var radians = (Math.PI/180)*degrees;  	//คำนวณค่ามุมในหน่วยเรเดียน
	context.beginPath();  
	context.arc(90,90,60,0,radians,false); 	//วาดรูปโดยเริ่มจาก 0 องศา ไปจบที่									//270 องศา แบบตามเข็ม
	context.fillStyle = 'transparent';
	context.strokeStyle = 'green';
	context.stroke();
	context.fill();
}
drawCanvas();