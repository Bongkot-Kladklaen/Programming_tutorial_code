package com.ideacode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
	// write your code here
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter Binary no. to convert in Decimal : ");
        String num = input.readLine();

        int dec = Integer.parseInt(num,2);
        System.out.println("Binary number converted to decimal number\n" +
                "Decimal number is : " + dec);
    }
}
