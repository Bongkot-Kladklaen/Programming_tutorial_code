package com.ideacode;

import java.time.LocalDate;
import java.time.Month;
import java.time.temporal.ChronoUnit;

public class Main {

    public static void main(String[] args) {
	// write your code here
        LocalDate today = LocalDate.now();
        System.out.println(today);
        System.out.println(today.getDayOfWeek());
        System.out.println(today.getDayOfYear());

        LocalDate day199 = LocalDate.ofYearDay(2021,199);
        System.out.println(day199);

        LocalDate woldCup2021 = LocalDate.of(2021, Month.JUNE, 12);
        System.out.println("WoldCup จะถึงอีกใน " + today.until(woldCup2021, ChronoUnit.DAYS) + " วัน");

        LocalDate birthday = LocalDate.of(1995, Month.MARCH, 31);
        System.out.println("เกิดมาแล้ว "+ birthday.until(today, ChronoUnit.DAYS) + " วัน");

        System.out.printf("อายุ %d ปี %d เดือน %d วัน",
                birthday.until(today).getYears(),
                birthday.until(today).getMonths(),
                birthday.until(today).getDays());
    }
}
