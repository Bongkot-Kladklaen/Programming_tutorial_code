//
//  textField.swift
//  SwitftUIDemo1
//
//  Created by Bongkot kladklaen on 30/6/2563 BE.
//  Copyright © 2563 ideacode. All rights reserved.
//

import SwiftUI

struct textField: View {
    @State var username:String = ""
    @State var password = ""
    
    var body: some View {
        VStack {
            TextField("Username", text: $username)
            .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding(.horizontal)
                .padding(.top)
            
            SecureField("Password", text: self.$password)
            .textFieldStyle(RoundedBorderTextFieldStyle())
                           .padding()
                       
            Text(username)
            Text(password)
            Spacer()
        }
    }
}

struct textField_Previews: PreviewProvider {
    static var previews: some View {
        textField()
    }
}
