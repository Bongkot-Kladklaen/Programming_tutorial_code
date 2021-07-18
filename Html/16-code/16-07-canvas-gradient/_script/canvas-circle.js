function drawCanvas(){
	var canvas = document.getElementById('myCanvas');
	var context = canvas.getContext('2d');
	var myGradient = context.createRadialGradient(80,80,30,70,70,60);  
  	myGradient.addColorStop(0, 'orange');  
  	myGradient.addColorStop(0.8, 'rgb(0,125,0)');  
  	myGradient.addColorStop(1, 'rgba(1,159,98,0)');
  	context.fillStyle = myGradient;
	context.fillRect(0,0,400,400);
}
drawCanvas();