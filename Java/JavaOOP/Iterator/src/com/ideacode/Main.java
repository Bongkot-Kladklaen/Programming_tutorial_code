package com.ideacode;

import java.util.ArrayList;
import java.util.Iterator;

public class Main {

    public static void main(String[] args) {
        // Make a collection
        ArrayList<String> cars = new ArrayList<String>();
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");
        cars.add("Mazda");

        Iterator<String> it = cars.iterator();
        System.out.println(it.next());
        System.out.println(it.next());

        System.out.println("-----------");

        // Loop
        while (it.hasNext()){
            System.out.println(it.next());
        }

        // Remove
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        numbers.add(12);
        numbers.add(8);
        numbers.add(2);
        numbers.add(23);

        Iterator<Integer> it2 = numbers.iterator();
        while(it2.hasNext()){
            int i = it2.next();
            if (i < 10){
                it2.remove();
            }
        }
        System.out.println(numbers);
    }
}
