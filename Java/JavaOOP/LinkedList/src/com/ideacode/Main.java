package com.ideacode;

import java.util.LinkedList;

public class Main {

    public static void main(String[] args) {
	// write your code here
        LinkedList<String> cars = new LinkedList<String>();
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");
        cars.add("Mazda");
        System.out.println(cars);

        cars.addFirst("AddFirst");
        cars.addLast("AddLast");
        System.out.println(cars);

        System.out.println(cars.getFirst());
        System.out.println(cars.getLast());
    }
}
