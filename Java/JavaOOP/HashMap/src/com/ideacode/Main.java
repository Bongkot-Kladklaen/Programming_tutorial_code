package com.ideacode;

import java.util.HashMap;

public class Main {

    public static void main(String[] args) {
	    // HashMap store items in Key/Value
        HashMap<String, String> capitalCities = new HashMap<String, String >();

        capitalCities.put("England", "London");
        capitalCities.put("Germany", "Berlin");
        capitalCities.put("Norway", "Oslo");
        capitalCities.put("USA", "Washington DC");
        System.out.println(capitalCities);

        // Access an item
        System.out.println(capitalCities.get("USA"));

        // Remove an item
        capitalCities.remove("USA");
        System.out.println(capitalCities);

//        capitalCities.clear();
//        System.out.println(capitalCities);

        // HashMap size
        System.out.println(capitalCities.size());

        // Loop HashMap
        for(String i: capitalCities.keySet()){ // Print keys
            System.out.println(i);
        }

        for (String i: capitalCities.values()) { // Print values
            System.out.println(i);
        }

        for(String i: capitalCities.keySet()){ // Print keys and value
            System.out.println("key: " + i + " value: " + capitalCities.get(i));
        }


    }
}
