package com.ideacode;

public class Main {

    public static void main(String[] args) {
	// write your code here
//        int result = sum(10);
//        System.out.println(result);

        System.out.println(fac(5));
    }

    // Recursion sum
    static int sum(int k){
        if(k > 0){
            return k + sum(k-1);
        } else {
            return 0;
        }
    }

    static int fac(int factorial){
        if(factorial == 0){
            return 1;
        } else {
            return (factorial * fac(factorial-1));
        }
    }
}
