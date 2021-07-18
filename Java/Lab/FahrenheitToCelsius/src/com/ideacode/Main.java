package com.ideacode;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here

        float temperature;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter temperature in Fahrenheit : ");
        temperature = input.nextInt();
        temperature = (temperature - 32) * 5/9;
        System.out.println("Temperature in Celsius = " + temperature);

    }
}
