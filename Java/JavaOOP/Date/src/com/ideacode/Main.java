package com.ideacode;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class Main {

    public static void main(String[] args) {
	// write your code here
        LocalDate myObj1 = LocalDate.now();
        System.out.println(myObj1);

        LocalTime myObj2 = LocalTime.now();
        System.out.println(myObj2);

        LocalDateTime myObj3 = LocalDateTime.now();
        System.out.println(myObj3);

        DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
        String formattedDate = myObj3.format(myFormatObj);
        System.out.println(formattedDate);
    }
}
