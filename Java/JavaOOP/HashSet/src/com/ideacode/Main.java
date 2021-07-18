package com.ideacode;

import java.util.HashSet;

public class Main {

    public static void main(String[] args) {
	    // HashSet เก็บข้อมูลไม่ซ้ำกัน
        HashSet<String> cars = new HashSet<String>();
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");
        cars.add("BMW");
        cars.add("Mazda");
        System.out.println(cars);

        // Check if an item exists
        System.out.println(cars.contains("Mazda"));

        // Remove an item
        cars.remove("Volvo");
        System.out.println(cars);

//        cars.clear();
//        System.out.println(cars);

        // HashSet size
        System.out.println(cars.size());

        // Loop HashSet
        for (String i :
                cars) {
            System.out.println(i);
        }
    }
}
