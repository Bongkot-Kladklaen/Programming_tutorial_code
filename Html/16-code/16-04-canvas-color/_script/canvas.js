function drawCanvas(){
	var canvas = document.getElementById("myCanvas");  //สร้าง Canvas
	var context = canvas.getContext("2d"); 	//กำหนด Context ซึ่งก็คือ													//การเตรียมพื้นที่
	context.fillStyle = "rgba(128,0,256,0.4)"; 
	context.fillRect(10,10,90,90); //กำหนดว่าจะเทสีพื้นทึบรูปสี่เหลี่ยมตรงไหน
}
drawCanvas();