//
//  ContentView.swift
//  BMI
//
//  Created by Bongkot kladklaen on 26/6/2563 BE.
//  Copyright © 2563 ideacode. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    @State var resultText:String = "BMI Calculator"
    @State var weight:String = ""
    @State var height:String = ""
    var body: some View {
        VStack {
            Text(resultText)
            HStack {
                Text("น้ำหนัก")
                TextField("Kg.", text: $weight).keyboardType(.numberPad)
            }.padding()
            
            HStack {
                Text("ส่วนสูง")
                TextField("Cm.", text: $height).keyboardType(.numberPad)
            }.padding()
            
            Button(action: {
                let result = Double(self.weight)! / pow(Double(self.height)!/100.0,2)
                self.resultText = String(result)
            }) {
                Text("เริ่มคำนวณ")
            }.padding()
        }.padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
