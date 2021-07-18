import UIKit

class Person{
    var name = ""
}
class BlogPost{
    
    var title:String
    var body = "hey"
    var author:Person
    var numberOfComments = 0
    
    init() {
        title = "My Title"
        author = Person()
    }
    convenience init(customTitle:String){
        self.init()
        title = customTitle
    }
 
}

let post = BlogPost(customTitle: "A Custom Title")

