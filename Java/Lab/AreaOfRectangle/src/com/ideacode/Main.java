package com.ideacode;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the length of Rectangle: ");
        float l = input.nextFloat();
        System.out.print("Enter the width of Rectangle: ");
        float w = input.nextFloat();

        System.out.println("Area of Rectangle is: " + (l*w));

    }
}
