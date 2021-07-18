package com.ideacode;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Scanner input = new Scanner(System.in);
        System.out.print("Enter Radius: ");
        int r = input.nextInt();
        System.out.print("Enter Height: ");
        int h = input.nextInt();

        double area = 2* 3.14 * r * (r+h);
        double volume = (3.14 * r * r) * h;

        System.out.println("Volume of Cylinder: " + volume);
        System.out.println("Area of Cylinder: " + area);

    }
}
