import UIKit

//Basic function
func addTwoNumbers() {
    
    let a = 1
    let b = 2
    let c = a + b
    
    print(c)
}
func substractTwoNumers(){
    let a = 1
    let d = 1
    let e = a - d
    
    print(e)
}

//Function return value
func addTwoNumbers_return() -> Int {
    
    let a = 1
    let b = 2
    let c = a + b
    
    return c
}

//Function parameter and return
func addTwoNumbers_parameter(number1 para1:Int, number2 para2:Int) -> Int {
    return para1 + para2
}
let sum = addTwoNumbers_parameter(number1: 2, number2: 4)
print(sum)
