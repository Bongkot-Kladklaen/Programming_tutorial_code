package com.ideacode;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class Main {

    public static void main(String[] args) {
        ArrayList<String> cars = new ArrayList<String>();  // Create an ArrayList object
        cars.add("Volvo");
        cars.add("Mazda");
        cars.add("BMW");
        cars.add("Ford");

        System.out.println(cars);

        // Access an item
        System.out.println(cars.get(0));

        // Change an item
        cars.set(0,"Opel");
        System.out.println(cars.get(0));

        // Remove an item
        cars.remove(0);
        System.out.println(cars);

//        cars.clear();
//        System.out.println(cars);

        // ArrayList size
        System.out.println(cars.size());

        // Loop ArrayList
        for (int i = 0; i < cars.size(); i++) {
            System.out.println(cars.get(i));
        }

        for (String myCar :
                cars) {
            System.out.println(myCar);
        }

        // Sort ArrayList
        Collections.sort(cars);
        for (String i : cars) {
            System.out.println(i);
        }
    }
}
