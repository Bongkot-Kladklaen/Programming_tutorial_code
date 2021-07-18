package com.ideacode;

import java.time.LocalDate;
import java.time.Month;
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
	// write your code here
        demo2();
    }

    public static void demo(){
        Person p1 = new Person("Mr.","Peter","Parker", LocalDate.of(1995, Month.MARCH,31));
        System.out.println(p1);
    }

    public static void demo2(){
        PersonV2 p1 = new PersonV2();
        PersonName th = new PersonName("นาย","ปีเตอร์","ปาร์คเกอร์");
        PersonName en = new PersonName("Mr.","Peter","Parker");
        p1.setNameTh(th);
        p1.setNameEn(en);
        p1.setDob(LocalDate.of(1995,Month.MARCH,31));

        Map<String, String> phone = new HashMap<String, String>();
        phone.put("mobile", "1234567890");
        phone.put("home", "0987654321");

        p1.setPhone(phone);

        System.out.println(p1);

    }
}
