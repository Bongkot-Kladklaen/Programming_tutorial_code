function drawCanvas(){
	var canvas = document.getElementById('myCanvas');
	var context = canvas.getContext('2d');
	context.beginPath();  
	context.arc(95,95,50,0,Math.PI*2,true); 
	context.fillStyle = 'blue';
	context.strokeStyle = 'red';
	context.stroke();
	context.fill();
}
drawCanvas();