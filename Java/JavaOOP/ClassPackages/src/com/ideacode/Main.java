package com.ideacode;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	    // Scanner is Build-in class package
        Scanner input = new Scanner(System.in);
        System.out.println("Enter username");

        String userName = input.nextLine();
        System.out.println("Username is: " + userName);
    }
}
