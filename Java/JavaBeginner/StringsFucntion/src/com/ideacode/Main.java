package com.ideacode;

public class Main {

    public static void main(String[] args) {
        // length()
        // toUpperCase()
        // toLowerCase()
        // indexOf()
        // concat()

        String txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        System.out.println(txt.length());

        txt = txt.toLowerCase();
        System.out.println(txt);

        txt = txt.toUpperCase();
        System.out.println(txt);

        System.out.println(txt.indexOf("B"));

        String firstName = "Jone";
        String lastName = "Doe";
        System.out.println(firstName.concat(lastName));
    }
}
