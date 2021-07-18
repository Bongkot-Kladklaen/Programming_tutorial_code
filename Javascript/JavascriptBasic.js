// var number1 = 35;
// var number2 = 40;

// var color = ['red','yellow','blue']
// color.push('black')
// color.push('blow')

// for(var i = 0; i <= color.length;i++) {
//     console.log(color[i])
// }

// var i = 0
// while (i < 10 ) {
//     console.log(i)
//     i++
// }

// color.forEach(function(color){
//     console.log(color)
// })

// color.forEach(color => {
//     console.log(color) 
// });

// if (condition) {
    
// }

// switch (key) {
//     case value:
        
//         break;

//     default:
//         break;
// }

asyncFunc(cb, cb);

function asyncFunc (running, done) {
  for (var i = 0;i<10;i++) {
    running('i = ' + i);
  }
  done('done');
}

function cb (str) {
  console.log(str);
}