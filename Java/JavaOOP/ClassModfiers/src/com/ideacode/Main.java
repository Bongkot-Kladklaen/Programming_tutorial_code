package com.ideacode;

public class Main {
    final int X = 10;
    final double PI = 3.14;

    public static void main(String[] args) {

//        Main obj = new Main();
//        obj.X = 50; Error: cannot change value
//        System.out.println(obj.X);

        Student obj2 = new Student();
        System.out.println(obj2.firstName);
        System.out.println(obj2.age);
        System.out.println(obj2.graduationYear);
        obj2.study();


    }
}

// Abstract class
abstract class People{
    public String firstName = "John";
    public int age = 24;
    // Abstract method
    public abstract void study();
}

class Student extends People{
    public int graduationYear = 2018;
    public void study(){
        System.out.println("Studying all day long");
    }
}
