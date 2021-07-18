package com.ideacode;

public class Main {

    public static void main(String[] args) {
	// write your code here
        int num1 = sumNumber(5,5);
        double num2 = sumNumber(5.5,2.0);

        System.out.println("int: "+num1);
        System.out.println("double: "+num2);
    }

    static int sumNumber(int x, int y){
        return x + y;
    }

    static double sumNumber(double x, double y){
        return x + y;
    }
}
