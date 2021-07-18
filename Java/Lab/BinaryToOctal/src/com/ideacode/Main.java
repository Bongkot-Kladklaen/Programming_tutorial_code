package com.ideacode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
	// write your code here

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter binary number: ");
        String num = input.readLine();

        int dec = Integer.parseInt("101010",2);
        String oct = Integer.toOctalString(dec);

        System.out.println("Binary " + num + " in Octal is " + oct );
    }
}
