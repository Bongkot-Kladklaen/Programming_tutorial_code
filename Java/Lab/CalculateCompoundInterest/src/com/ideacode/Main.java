package com.ideacode;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        double amount,years,rate;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the amount: ");
        amount = input.nextDouble();
        System.out.println("Enter the No.of years: ");
        years = input.nextDouble();
        System.out.println("Enter the Rate of interest: ");
        rate = input.nextDouble();

        double simpleInt = (amount * rate * years)/100;
        double compoundInt = amount * Math.pow((1+(rate/100)),years)- amount;

        System.out.println("\nAmount : " + amount);
        System.out.println("No. of years : " + years);
        System.out.println("Rate of interest : " + rate);
        System.out.println("Simple Interest : " + simpleInt);
        System.out.println("Compound Interest : " + compoundInt);



    }
}
