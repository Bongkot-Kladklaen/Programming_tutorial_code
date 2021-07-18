function drawCanvas(){
 	var context = document.getElementById('myCanvas').getContext('2d');  
	var img = new Image();
	img.src = '_images/logo.png';  
    	img.onload = function(){  
      		context.drawImage(img,5,0);    
    	};  
}
drawCanvas();