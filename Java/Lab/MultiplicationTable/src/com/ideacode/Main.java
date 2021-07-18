package com.ideacode;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        int sum;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter an integer to print it's multiplication table");
        int num = input.nextInt();
        System.out.println("Multiplication table of " + num +" is :-");
        for (int i = 1; i <= 10 ; i++) {
            sum = num * i;
            System.out.println(num + "*" + i + " = " + sum);
        }
    }
}
