package com.ideacode;

public class Main {

    public static void main(String[] args) {
	    // Call method
        myMethod();
        myMethod2("John");
        myMethod3("Jay",25);

        int sum = myMethodReturnValue(5,5);
        System.out.println(sum);
    }

    // Method
    static void myMethod(){
        System.out.println("I just got executed!");
    }

    // Method and arguments
    static void myMethod2(String name){
        System.out.println("Hello " + name);
    }

    // Multiple Parameters
    static void myMethod3(String name, int age){
        System.out.println("Hello " + name + " age " + age);
    }

    // Return values
    static int myMethodReturnValue(int x, int y){
        return x + y;
    }
}
