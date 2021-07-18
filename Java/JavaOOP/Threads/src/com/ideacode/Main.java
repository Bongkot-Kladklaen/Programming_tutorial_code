package com.ideacode;

public class Main extends Thread{

    public static int amount = 0;

    public static void main(String[] args) {
	// write your code here
        Main thread = new Main();
        thread.start();
        while (thread.isAlive()){
            System.out.println("Waiting....");
        }
//        System.out.println("This code id outside of the thread");
        System.out.println(amount);
        amount++;
        System.out.println(amount);
    }

    public void run(){
//        System.out.println("This code is running in a thread");
        amount++;

    }

}
