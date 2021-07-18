package com.ideacode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {

        int dec;
        String bit;

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter a number: ");
        dec = Integer.parseInt(input.readLine());
        bit = Integer.toBinaryString(dec);
        System.out.println("The binary representation is "+bit);

    }
}
