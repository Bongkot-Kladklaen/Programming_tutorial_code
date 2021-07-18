package com.ideacode;

public class Main {
    public static void demo1(){
        Contact p1 = new Contact();
        Contact p2 = new Contact("bongkot","kladklaen","0860354540");
        p1.setFirstname("peter");
        p1.setLastName("PARKER");
        p1.setPhoneNumber("063-4172-459");

        System.out.println(p1);
        System.out.println(p2);



    }
    public static void main(String[] args) {
	// write your code here
        demo1();
    }
}
