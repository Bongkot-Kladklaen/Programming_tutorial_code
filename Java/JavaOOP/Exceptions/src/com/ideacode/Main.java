package com.ideacode;

public class Main {

    public static void main(String[] args) {

        // try and catch and finally
//        int[] myNumber = {1,2,3};
//        try {
//            System.out.println(myNumber[10]);
//        }
//        catch (Exception e){
//            System.out.println("Something went wrong.");
//        }
//        finally {
//            System.out.println("The 'try catch' is finished.");
//        }

        // throw กำหนดข้อผิดพลาดเอง
        int age = 20;
        if (age < 18){
            throw new ArithmeticException("Access denied - you must be at least 10 years old.");
        } else {
            System.out.println("Access granted - You are old enough!");
        }

    }
}
