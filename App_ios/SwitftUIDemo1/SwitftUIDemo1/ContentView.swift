//
//  ContentView.swift
//  SwitftUIDemo1
//
//  Created by Bongkot kladklaen on 29/6/2563 BE.
//  Copyright © 2563 ideacode. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    
    let message1 = "I am Lek CodeMobiles"
    let myName = "Lek"
    let today = Date()
    
    static let dateFormatter:DateFormatter = {
        let formatter = DateFormatter()
//        formatter.dateStyle = .short
        formatter.dateFormat = "dd/MM/YY"
        return formatter
    }()
    
    static let numberFormatter:NumberFormatter={
        let formatter = NumberFormatter()
        formatter.numberStyle = .decimal
        return formatter
    }()
    
    var body: some View {
//        Text("Hello, World!")
//            .border(Color.yellow)
//            //.frame(width: 300, height: 80, alignment: .center)
//            .frame(minWidth: 0,maxWidth: .infinity, minHeight: 0, maxHeight: .infinity, alignment: .center)
//            .border(Color.green, width:2)
//            .foregroundColor(.red)
//            .background(Color.black)
//            .font(.title)
        
        VStack(spacing: 20){
            Text(message1)
            Text("My name is \(self.myName)")
            Text("Today: \(today,formatter: Self.dateFormatter)")
            Text("My Money: \(Self.numberFormatter.string(from: 10000)!)")
            
            
        }
//        .frame(minWidth: 0, maxWidth: .infinity, minHeight: 0,maxHeight: .infinity)
//        .background(Color.green)
//        .edgesIgnoringSafeArea(.all)
        
//        VStack(spacing:0){
//            GeometryReader{ g in
//                Image("codemobiles_logo")
//                    .resizable()
//                    .aspectRatio(contentMode: .fill)
//                    .frame(width: g.size.width, height: g.size.height)
//                    .clipped()
//            }
//            .background(Color.green)
//            .frame(height:70)
//
//            VStack{
//                Spacer()
//                Row()
//                Spacer()
//                Row()
//                Spacer()
//                Row()
//                Spacer()
//            }
//            .background(Color.yellow)
//            .edgesIgnoringSafeArea(.all)
//        }
        
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

struct Row: View {
    var body: some View {
        HStack {
            Spacer()
            Text("Col1").background(Color.red)
            Spacer()
            Text("Col2").background(Color.red)
            Spacer()
            Text("Col3").background(Color.red)
            Spacer()
            
        }
    }
}
