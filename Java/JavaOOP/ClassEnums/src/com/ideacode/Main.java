package com.ideacode;

public class Main {

    public static void main(String[] args) {

        // Enum มักใช้กับ switch
//        Level myVar = Level.MEDIUM;
//        switch (myVar){
//            case LOW : System.out.println("Low level"); break;
//            case MEDIUM: System.out.println("Medium level"); break;
//            case HIGH: System.out.println("High level"); break;
//
//        }

        for (Level myVar: Level.values()) {
            System.out.println(myVar);
        }

    }
}
