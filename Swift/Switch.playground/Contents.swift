import UIKit

var someCharacter:Character = "c"

switch someCharacter {
case "a":
    print("is an A")
case "b","c":
    print("is an B or C ")
default:
    print("some fallback")
}
