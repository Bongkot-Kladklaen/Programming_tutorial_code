package com.ideacode;

public class Main {
    public static void demoDice1(){
        long start = System.currentTimeMillis();
        Dice aDice = new Dice();
        for (int i = 0; i < 10000; i++){
            System.out.println(aDice.roll());
        }
        for (int i = 0; i < aDice.getFreqs().length; i++){
            System.out.printf("face %d occurs %d times\n",i+1,aDice.getFreqs()[i]);
        }
        long stop = System.currentTimeMillis();
        System.out.println("Time = " + (stop-start));
    }
    public static void demoDice2(){
        long start = System.currentTimeMillis();
        DiceV2 aDice = new DiceV2();
        for (int i = 0; i < 20; i++){
            aDice.roll();
            System.out.println(aDice.getDiceFace());
        }
        aDice.showFreqs();
        long stop = System.currentTimeMillis();
        System.out.println("Time = " + (stop-start));
    }

    public static void main(String[] args) {
	// write your code here
        demoDice2();

    }
}
