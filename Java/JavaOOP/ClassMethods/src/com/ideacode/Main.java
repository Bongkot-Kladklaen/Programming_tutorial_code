package com.ideacode;

public class Main {
    // Static method
    static void myStaticMethod(){
        System.out.println("Static method can be called without crating objects");
    }

    // Public method
    public void myPublicMethod(){
        System.out.println("Public methods must be called by creating objects");
    }

    public static void main(String[] args) {
        myStaticMethod();
//        myPublicMethod();  // Error

        Main obj1 = new Main();
        obj1.myPublicMethod();


    }
}
