package com.ideacode;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        areaCircle();
    }

    public static void areaCircle(){
        Scanner input = new Scanner(System.in);
        System.out.println("The radius of the circle is: ");

        double radius = input.nextDouble();
        double result = Math.PI * Math.pow(radius,2);
        System.out.println("Area of a circle is: " + result);
    }

}
