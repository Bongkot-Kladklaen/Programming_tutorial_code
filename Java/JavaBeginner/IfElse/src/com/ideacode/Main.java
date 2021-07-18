package com.ideacode;

public class Main {

    public static void main(String[] args) {

        int x = 20;
        int y = 18;

        if (x > y){
            System.out.println("x is grater than y");
        } else {
            System.out.println("x is not grater than y");
        }

        // Short had if-else
        String a = (x > y) ? "x is grater than y" : "x is not grater than y";
        System.out.println(a);
    }
}
