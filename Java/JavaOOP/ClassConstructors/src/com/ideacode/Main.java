package com.ideacode;

public class Main {
    // Create a class attribute
    int modelYear;
    String modelName;

    // Constructor for the main class
    public Main(int year, String name){
        modelYear = year;
        modelName = name;

    }

    public static void main(String[] args) {
	// write your code here
        Main obj = new Main(2021,"John");
        System.out.println(obj.modelYear +" "+ obj.modelName);
    }
}
