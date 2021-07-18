package com.ideacode;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        harmonicSeries();
    }

    public static void harmonicSeries(){
        double sum = 0.0;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number for length of series");
        int numbers = input.nextInt();

        for (int i = 1; i <= numbers; i++){
            System.out.print("1/"+i+" + ");
            sum += (double)1/i;
        }
        System.out.println("\n\nSum of Harmonic Series is " + sum);

    }
}
