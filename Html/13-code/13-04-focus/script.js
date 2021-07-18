var myName = document.getElementById("myName");
myName.onfocus = function() {
	if (myName.value == "กรุณากรอกชื่อ"){
		myName.value = "";
	}
};
myName.onblur = function() {
	if (myName.value == ""){
		myName.value = "กรุณากรอกชื่อ";
	}
};