function keepEventScript() {
	var myImage = document.getElementById("mainImage");
	myImage.onclick = function() {
		alert("คุณคลิกรูปภาพเหรอ.."); 	
	};
}
window.onload = function() {
	keepEventScript();  	// เรียกใช้ฟังก์ชันเมื่อมีการโหลดเว็บเพจเรียบร้อยแล้ว
};