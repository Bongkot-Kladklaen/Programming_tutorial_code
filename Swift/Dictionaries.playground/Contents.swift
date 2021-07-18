import UIKit

//Declaring a new Dictionary
var carDB = Dictionary<String,String>()

// Adding key value pairs
carDB["JSD 238"] = "Blue Ferrari"
carDB["SID 482"] = "Green Lamborghini"

// Retrieving data
carDB["JSD 238"]

// Update a vlaue for a key
carDB["JSD 238"] = "Red Perrari"

// Remove a key-value pair
//carDB["JSD 238"] = nil

// iterate over it
for (license , car) in carDB{
    print("\(car) as a license: \(license)")
}
