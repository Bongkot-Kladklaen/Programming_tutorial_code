package com.ideacode;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Person obj = new Person();
        obj.setName("John");
        System.out.println(obj.getName());
    }
}

class Person{
    // Encapsulation attribute
    private String name;

    // Getter
    public String getName(){
        return name;
    }

    // Setter
    public void setName(String name){
        this.name = name;
    }

}
