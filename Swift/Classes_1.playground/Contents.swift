import UIKit

class BlogPost {
    
    var title = ""
    var body = ""
    var author = ""
    var numberOfComments = 0
    
    func addComment() {
        numberOfComments += 1
    }
    
}

let myPost = BlogPost()
myPost.title = "Hello Playground"
myPost.author = "Chris Ching"
myPost.body = "Hello"
myPost.addComment()
print(myPost.numberOfComments)

let mySecounPost = BlogPost()
mySecounPost.title = "Goodbye Playground"
mySecounPost.author = "John Travolta"
mySecounPost.body = "Hello"
myPost.addComment()
print(myPost.numberOfComments)



