package com.ideacode;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        calMean();
    }
    public static void calMean(){
        int sum = 0, inputNum, count;
        float mean;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the total number of terms whose mean you wat to calculate: ");
        count = input.nextInt();

        System.out.println("Please enter " + count + " numbers:");
        for (int i = 0; i < count ; i++) {
            inputNum = input.nextInt();
            sum += inputNum;
            System.out.println();

        }
        mean = sum / count;
        System.out.println("The mean of the 3 numbers you entered is " + mean );
    }
}
