function drawCanvas(){
	var canvas = document.getElementById('myCanvas');
	var context = canvas.getContext('2d');
	var myGradient = context.createLinearGradient(45,45,200,200);  
  	myGradient.addColorStop(0, 'green');  
	myGradient.addColorStop(1, 'rgba(1,159,98,0)'); 
	context.fillStyle = myGradient;
	context.fillRect(0,0,400,400);
}
drawCanvas();