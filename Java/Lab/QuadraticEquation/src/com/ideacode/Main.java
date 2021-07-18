package com.ideacode;

public class Main {

    public static void main(String[] args) {
	// write your code here
        quadraticEquation();
    }
    public static void quadraticEquation(){
        // ax^2 + bx + c = 0

        int a = 2;
        int b = 6;
        int c = 4;

        double sRoot = Math.sqrt(b * b - 4 * a * c);
        double x1 = (-b + sRoot) / (2*a);
        double x2 = (-b - sRoot) / (2*a);

        System.out.println("The roots of the Quadratic Equation \"2x2 + 6x +4 = 0 are "+ x1 + " and " + x2);
    }
}
