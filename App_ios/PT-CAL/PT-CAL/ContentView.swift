//
//  ContentView.swift
//  PT-CAL
//
//  Created by Bongkot kladklaen on 26/6/2563 BE.
//  Copyright © 2563 ideacode. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    
    @State var pipsWin:String = ""
    @State var pipsLoss:String = ""
    @State var proFit:String = ""
    @State var usd:String = ""
    
    @State var text_loteSize:String = ""
    @State var text_balanceHave:String = ""
    @State var text_balanceWaste:String = ""
    
    @State var GrowthRate:Double = 0
    @State var LoteSize:Double = 0
    @State var BalanceHave:Double = 0
    @State var BalanceWeste:Double = 0
    @State var count:Int = 0
    
    var body: some View {
        VStack {
            Text("PT-Calculator")
                .font(.title)
                .padding(.bottom,20)
            VStack {
                VStack {
                    HStack {
                        VStack {
                            Text("Pips Win")
                            TextField("\(pipsWin)", text: $pipsWin)
                                .padding(10)
                                .font(Font.system(size: 15, weight: .medium, design: .serif))
                                .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                                .keyboardType(.decimalPad)
                        }
                        Spacer()
                        VStack {
                            Text("Pips loss")
                            TextField("\(pipsLoss)", text: $pipsLoss)
                                .padding(10)
                                .font(Font.system(size: 15, weight: .medium, design: .serif))
                                .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                                .background(Color.gray.opacity(0.2))
                                .disabled(true)
                        }
                    }
                    HStack {
                        VStack {
                            Text("Profit")
                            TextField("\(proFit)", text: $proFit)
                               .padding(10)
                               .font(Font.system(size: 15, weight: .medium, design: .serif))
                               .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                                .keyboardType(.numberPad)
                        }
                        Spacer()
                        VStack {
                            Text("USD")
                            TextField("\(usd)", text: $usd)
                              .padding(10)
                                .font(Font.system(size: 15, weight: .medium, design: .serif))
                                .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                                .keyboardType(.numberPad)
                        }
                    }
                    .padding(.bottom,30)
                    Button(action: {
                        let usd = Double(self.usd)!
                        let profit = Double(self.proFit)!
                        let pipswin = Double(self.pipsWin)!
                        let PipLoss = Double(self.pipsWin)! * 0.75
                    
                        self.GrowthRate = usd/(usd+(usd*(profit/100.0)))
                        self.LoteSize = ((usd+(usd*(profit/100.0)))-usd)/pipswin
                        self.BalanceHave = usd/self.GrowthRate
                        self.BalanceWeste = (usd * 0.75)/self.GrowthRate
                        
                        self.LoteSize = (self.LoteSize * 1000).rounded()/1000
                        self.BalanceHave = (self.BalanceHave * 100).rounded()/100
                        self.BalanceWeste = (self.BalanceWeste * 100).rounded()/100
                        
                        self.text_loteSize = String(format: "%.3f",self.LoteSize)
                        self.text_balanceHave = String(format: "%.2f", self.BalanceHave)
                        self.text_balanceWaste = String(format: "%.2f", self.BalanceWeste)
                        
                        self.pipsLoss = String(PipLoss)
                    }) {
                        Text("Calculate")
                            .fontWeight(.regular)
                            .foregroundColor(.white)
                            .font(.title)
                    }
                    .frame(width:250,height:55)
                    .background(Color.blue).cornerRadius(50)
                    .padding(.bottom,40)
                }
                VStack {
                    HStack{
                        Text("Lote size : " + text_loteSize)
                            .fontWeight(.bold)
                            .frame(width: 390, height: 60)
                            .background(Color.blue.opacity(0.9))
                            .cornerRadius(15)
                            .foregroundColor(.white)
                    }
                    .padding(.bottom,10)
                    HStack{
                        Text("Balance Win : " + text_balanceHave)
                            .fontWeight(.bold)
                            .frame(width: 390, height: 60)
                            .background(Color.blue.opacity(0.9))
                            .cornerRadius(15)
                            .foregroundColor(.white)
                    }
                    .padding(.bottom,10)
                    HStack{
                        Text("Balance Loss : " + text_balanceWaste)
                            .fontWeight(.bold)
                            .frame(width: 390, height: 60)
                            .background(Color.blue.opacity(0.9))
                            .cornerRadius(15)
                            .foregroundColor(.white)
                    }
                    .padding(.bottom,40)
                }
                VStack {
                    HStack{
                        Button(action: {
                            self.text_loteSize = ""
                            self.text_balanceHave = ""
                            self.text_balanceWaste = ""
                            self.pipsLoss = ""
                            self.pipsWin = ""
                            self.usd = ""
                            self.proFit = ""
                            self.count = 0
                        }) {
                            Text("Reset")
                                .fontWeight(.regular)
                                .foregroundColor(.white)
                                .font(.title)
                        }
                        .frame(width:150,height:50)
                        .background(Color.blue).cornerRadius(50)
                        .padding(.bottom,40)
                        
                        Button(action: {
                            self.LoteSize = self.LoteSize/self.GrowthRate
                            self.BalanceHave = self.BalanceHave/self.GrowthRate
                            self.BalanceWeste = (self.BalanceWeste/self.GrowthRate)
                
                            self.LoteSize = (self.LoteSize * 1000).rounded()/1000
                            self.BalanceHave = (self.BalanceHave * 100).rounded()/100
                            self.BalanceWeste = (self.BalanceWeste * 100).rounded()/100
                          
                            self.text_loteSize = String(format:"%.3f", self.LoteSize)
                            self.text_balanceHave = String(format: "%.2f", self.BalanceHave)
                            self.text_balanceWaste = String(format: "%.2f", self.BalanceWeste)
                        
                            self.count += 1
                        }) {
                            Text("Next")
                                .fontWeight(.regular)
                                .foregroundColor(.white)
                                .font(.title)
                        }
                        .frame(width:150,height:50)
                        .background(Color.blue).cornerRadius(50)
                        .padding(.bottom,40)
                    }
                }
                Text("Next Count : " + String(count))
                
            }
            .padding()
        }
        
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
