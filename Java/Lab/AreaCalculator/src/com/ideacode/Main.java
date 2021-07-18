package com.ideacode;

import java.awt.*;
import java.util.Scanner;

public class Main {
    static Scanner input = new Scanner(System.in);
    static int choice;
    static int currentChoice;
    public static void main(String[] args) {
	// write your code here
        listChoice();
        while (choice != 7){
            if (choice == 1 || (currentChoice == 1 && choice == 6)){
                System.out.println("The Area of Square is: "+squareArea());
            }else if(choice == 2 || currentChoice == 2 && choice == 6){
                System.out.println("The Area of Rectangle is: "+rectangleArea());
            }else if(choice == 3 || currentChoice == 3 && choice == 6){
                System.out.println("The Area of Triangle is: "+triangleArea());
            }else if(choice == 4 || currentChoice == 4 && choice == 6){
                System.out.println("The Area of Circle is: "+circleArea());
            }else if(choice == 5 || currentChoice == 5 && choice == 6) {
                System.out.println("The Area of Trapezoid is: " + trapezoidArea());
            }
            currentChoice = choice;
            listChoice();
        }
    }
    public static void listChoice(){
        System.out.println("Enter the Object of which Area is to be calculated\n" +
                "1:square\n" +
                "2:rectangle\n" +
                "3:Triangle\n" +
                "4:circle\n" +
                "5:Trapezoid\n" +
                "6:Repeat\n" +
                "7:Exit");
        choice = input.nextInt();
    }
    public static float squareArea(){
        System.out.print("Enter the A side of Square: ");
        float a = input.nextFloat();
        return a * a;
    }
    public static float rectangleArea(){
        System.out.print("Enter the A width of Rectangle: ");
        float a = input.nextFloat();
        System.out.print("Enter the B length of Rectangle: ");
        float b = input.nextFloat();
        return a * b;
    }
    public static float triangleArea(){
        System.out.print("Enter the A width of Triangle: ");
        float w = input.nextFloat();
        System.out.print("Enter the B length of Triangle: ");
        float l = input.nextFloat();
        return (float)(0.5 * w * l);
    }
    public static float circleArea(){
        System.out.print("Enter the A radius of Circle: ");
        float r = input.nextFloat();
        return (float)(3.14 * r * r);
    }
    public static float trapezoidArea(){
        System.out.print("Enter the A side of Trapezoid: ");
        float l1 = input.nextFloat();
        System.out.print("Enter the B side of Trapezoid: ");
        float l2 = input.nextFloat();
        System.out.print("Enter the C height of Trapezoid: ");
        float h = input.nextFloat();
        return (float)(0.5 * ((l1 + l2) * h));
    }


}
