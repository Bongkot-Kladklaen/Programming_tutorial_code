function drawCanvas(){
	var canvas = document.getElementById("myCanvas");  //สร้าง Canvas
	var context = canvas.getContext("2d"); 	//กำหนด Context ซึ่งก็คือ													//การเตรียมพื้นที่
	context.strokeStyle = "red";  		//กำหนดสีให้กับเส้นเป็นสีแดง
	context.fillStyle = "blue";   		//กำหนดสีให้กับพื้นเป็นสีน้ำเงิน
	context.fillRect(10,10,90,90); 	//กำหนดว่าจะเทสีพื้นทึบรูปสี่เหลี่ยมตรงไหน
	context.strokeRect(20,20,100,100); //กำหนดว่าจะตีเส้นกรอบสี่เหลี่ยมตรงไหน
}
drawCanvas(); //คำสั่งในการเรียกใช้ฟังก์ชัน