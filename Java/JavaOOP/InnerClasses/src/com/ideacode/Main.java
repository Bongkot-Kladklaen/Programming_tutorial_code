package com.ideacode;

public class Main {

    public static void main(String[] args) {
	// write your code here
        OuterClass myOuter = new OuterClass();
//        OuterClass.InnerClass myInner = myOuter.new InnerClass();
        OuterClass.InnerClass myInner = new OuterClass.InnerClass();
        System.out.println(myInner.y + myOuter.x);
    }
}

class OuterClass{
    int x = 10;

    // Class ภายนอกไม่สามารถเข้าถึงได้
//    private class InnerClass{
//        int y = 5;
//    }

    // เข้าถึง class ได้โดยไม่ต้องสร้าง object
    static class InnerClass{
        int y = 5;
    }
}
