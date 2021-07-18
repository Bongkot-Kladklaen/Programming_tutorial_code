//
//  button.swift
//  SwitftUIDemo1
//
//  Created by Bongkot kladklaen on 30/6/2563 BE.
//  Copyright © 2563 ideacode. All rights reserved.
//

import SwiftUI

struct button: View {
    @State var isShowMessage = false
    var body: some View {
        VStack{
//            Button(action: {
//                print("running.")
//                self.isShowMessage.toggle()
//            }){
//                Text("Run")
//            }
//            if isShowMessage{
//                Text("I am lek")
//            }
            
            Button(action: {
               self.isShowMessage = true
            }){
                Text("Run")
            }
        }.alert(isPresented: self.$isShowMessage){() -> Alert in
            Alert(title: Text("Rusult"), message: Text("It is just alert"), dismissButton: .cancel())
        }
    
    }
}

struct button_Previews: PreviewProvider {
    static var previews: some View {
        button()
    }
}
