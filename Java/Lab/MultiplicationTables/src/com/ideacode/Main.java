package com.ideacode;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        int start,stop,mul;
        System.out.println("Enter range of numbers to print their multiplication table");
        Scanner input = new Scanner(System.in);
        start = input.nextInt();
        stop = input.nextInt();
        for (mul = start;mul <= stop;mul++){
            System.out.println("Multiplication table of " + mul);
            for (int i=1;i<=10;i++){
                System.out.println(mul + "*" + i + " = " + (mul * i));
            }
        }
    }
}
