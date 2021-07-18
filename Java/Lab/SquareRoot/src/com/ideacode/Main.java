package com.ideacode;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a number");
        int num = input.nextInt();
        float numRoot = (float)Math.sqrt(num);
        System.out.println("Square root of a number " + num +" = " + numRoot);
    }
}
