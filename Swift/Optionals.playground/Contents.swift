import UIKit

class Person {
    var name = ""
}
class BlogPost {
    
    var title:String?
    var body = "hey"
    var author:Person?
    var numberOfcomments = 0
   
}

let post = BlogPost()

print(post.body + " Hello!")

post.title = "yo"

// Optional Binding
if let actualTitle = post.title {
    // Optional contains value
    print(actualTitle + " salut")
}

// Test for nil
if post.title != nil{
    // Optional contains value
    print(post.title! + " Salut")
}
if post.title == nil{
    // Optional contains no value
}
