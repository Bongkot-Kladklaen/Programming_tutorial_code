function drawCanvas(){
	var canvas = document.getElementById('myCanvas');
	var context = canvas.getContext('2d');
	context.beginPath();  
	context.moveTo(50,50); 
	context.lineTo(70,70);
	context.arc(80,80,50,0,Math.PI,false);
	context.closePath();
	context.fillStyle = 'yellow';
	context.strokeStyle = 'red';
	context.lineWidth = 4;
	context.stroke();
	context.fill();
}
drawCanvas();
