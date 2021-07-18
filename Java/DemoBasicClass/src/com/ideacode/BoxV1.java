package com.ideacode;

public class BoxV1 {
    public double w, h, d; // access modifier

    public double volume(){
        return w * h * d;
    }

    public double surfaceArea(){
        return (2.0 * w * h) + (2.0 * w * d) + (2.0 * d * h);
    }
}
