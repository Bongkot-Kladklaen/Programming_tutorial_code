import UIKit

class Car{
    
    var topSpeed = 200
    func drive() {
        print("Driving at \(topSpeed)")
    }
}

// inheritance
class FutureCar: Car {
    override func drive() {
        super.drive()
        print("and rockets boostring at 50")
    }
    func fly() {
        print("Flying")
    }
}

let myRide = Car()
myRide.topSpeed
myRide.drive()

let myNewRide = FutureCar()
myNewRide.topSpeed
myNewRide.drive()
myNewRide.fly()
