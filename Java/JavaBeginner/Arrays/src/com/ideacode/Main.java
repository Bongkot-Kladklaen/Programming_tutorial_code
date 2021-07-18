package com.ideacode;

public class Main {

    public static void main(String[] args) {
	// write your code here
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        System.out.println(cars[0]);

        // Change an array element
        cars[0] = "Opel";
        System.out.println(cars[0]);

        // Array Length
        System.out.println(cars.length);

        // Loop array
        String[] cars2 = {"Volvo", "BMW", "Ford", "Mazda"};
        for (int i = 0; i < cars2.length; i++) {
            System.out.println(cars2[i]);
        }

        for (String i : cars2) {
            System.out.println(i);
        }

        // Multidimensional Arrays
        int[][] myNumbers = { {1,2,3,4}, {5,6,7} };
        for (int i = 0; i < myNumbers.length; i++) {
            for (int j = 0; j < myNumbers[i].length; j++) {
                System.out.println(myNumbers[i][j]);
            }
        }
        System.out.println("------");
        for (int[] i: myNumbers) {
            for (int j: i){
                System.out.println(j);
            }
        }


    }
}
