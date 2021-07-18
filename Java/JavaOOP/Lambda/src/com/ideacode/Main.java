package com.ideacode;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
	// write your code here
//        ArrayList<Integer> numbers = new ArrayList<Integer>();
//        numbers.add(5);
//        numbers.add(2);
//        numbers.add(8);
//        numbers.add(1);
//        numbers.forEach( n -> System.out.println(n) );

        StringFunction exclaim = s -> s + "!";
        StringFunction ask = s -> s + "?";
        printFormatted("Hello", exclaim);
        printFormatted("Hello", ask);

    }

    public static void printFormatted(String str, StringFunction format){
        String result = format.runLambda(str);
        System.out.println(result);
    }
}

interface StringFunction{
    String runLambda(String str);
}