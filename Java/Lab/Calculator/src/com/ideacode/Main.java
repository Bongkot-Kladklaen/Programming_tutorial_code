package com.ideacode;

import java.util.Scanner;

public class Main {
    static Scanner input = new Scanner(System.in);
    static int[] nums = new int[2];
    static int choice;

    public static void main(String[] args) {
	// write your code here
        calculator();
    }

    public static void calculator(){
        listChoice();
        while (choice != 99){
            if (choice == 1) {
                int[] nums = inputNumber();
                System.out.println("The answer is " + add(nums[0], nums[1]) + "\n");
            } else if (choice == 2) {
                int[] nums = inputNumber();
                System.out.println("The answer is " +  subtract(nums[0], nums[1]) + "\n");
            } else if (choice == 3) {
                int[] nums = inputNumber();
                System.out.println("The answer is " + multiply(nums[0], nums[1]) + "\n");
            } else if (choice == 4) {
                int[] nums = inputNumber();
                System.out.println("The answer is " + divide(nums[0], nums[1]) + "\n");
            } else if (choice == 5) {
                int[] nums = inputNumber();
                System.out.println("The answer is " +  mod(nums[0], nums[1]) + "\n");
            } else if (choice == 6) {
                int[] nums = inputNumber();
                System.out.println("The answer is " + power(nums[0], nums[1]) + "\n");
            }
            listChoice();
        }
        System.out.println("Ending Program...." );
    }

    public static void listChoice(){
        System.out.println("Calculator Program");
        System.out.println("------------------");
        System.out.println("\n1. Add \n"
                + "2. Subtract \n"
                + "3. Multiply \n"
                + "4. Divide \n"
                + "5. Mod \n"
                + "6. Power \n"
                + "99. End program"
        );
        System.out.println("Enter Choice:");
        choice = input.nextInt();
    }

    public static int[] inputNumber(){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter enter 2 numbers only:");
        nums[0] = input.nextInt();
        nums[1] = input.nextInt();
        return nums;
    }

    public static int add(int x, int y){
        return x + y;
    }
    public static int subtract(int x, int y){
        return x - y;
    }
    public static int multiply(int x, int y){
        return x * y;
    }
    public static int divide(int x, int y){
        return x / y;
    }
    public static int mod(int x, int y){
        return x % y;
    }
    public static int power(int x, int y){
        return (int)Math.pow(x,y);
    }

}
