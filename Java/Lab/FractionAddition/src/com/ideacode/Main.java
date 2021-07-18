package com.ideacode;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        float a,b,c,d;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a: ");
        a = input.nextInt();
        System.out.println("Enter b: ");
        b = input.nextInt();
        System.out.println("Enter c: ");
        c = input.nextInt();
        System.out.println("Enter d: ");
        d = input.nextInt();
        System.out.println("[("+a+" * "+d+")+("+b+" * "+c+")/("+b+" * "+d+")] + " + ((a*d)+(b*c))/(b*d));



    }
}
