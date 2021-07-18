function drawCanvas(){
	var canvas = document.getElementById("myCanvas");  //สร้าง Canvas
	var context = canvas.getContext("2d"); 		//กำหนด Context ซึ่ง												//ก็คือการเตรียมพื้นที่
	context.fillStyle = "red";  	//กำหนดสีให้กับพื้นเป็นสีแดง
	context.fillRect(10,10,90,90); 	//กำหนดว่าจะเทสีพื้นทึบรูปสี่เหลี่ยมตรงไหน
	context.clearRect(40,40,60,60); //กำหนดว่าจะลบพื้นที่ตรงไหนออกไป
}
drawCanvas();