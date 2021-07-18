package com.ideacode;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Scanner input = new Scanner(System.in);
        System.out.println("Enter first number to find GCD : ");
        int num1 = input.nextInt();
        System.out.println("Enter second number to find GCD : ");
        int num2 = input.nextInt();

        System.out.println("GCD of two numbers 80 and 50 is : " + findGCD(num1,num2));

    }

    public static int findGCD(int a, int b){
        if (b == 0){
            return a;
        }
        return findGCD(b, a % b);
    }
}
