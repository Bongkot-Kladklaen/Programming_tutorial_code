package com.ideacode;

import java.util.Random;

public class DiceV2 {
    private int[] freqs = new int[6];
    private int counts = 0;
    private char diceFace;

    public int[] getFreqs() {
        return freqs;
    }

    public char getDiceFace() {
        return diceFace;
    }

    public static Random R = new Random();
    public int roll(){
        counts++;
        int face =  R.nextInt(6) + 1;
        freqs[face-1] += 1;
        diceFace = (char)(face-1 + '\u2680');
        return face;
    }

    public void showFreqs(){
        for (int i = 0; i < freqs.length; i++){
            System.out.printf("face %d occurs %d times(%.2f%%)\n",i+1,freqs[i],(float)freqs[i]/(float) counts * 100);
        }
    }
}
