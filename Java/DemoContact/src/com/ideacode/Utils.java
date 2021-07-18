package com.ideacode;

public class Utils {
    // static method -> class method
    public static String capitalizedFirstCharOfString(String s){
        return s.substring(0,1).toUpperCase() + s.substring(1).toLowerCase();
    }
}
