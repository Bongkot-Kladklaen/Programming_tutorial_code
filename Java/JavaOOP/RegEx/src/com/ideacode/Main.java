package com.ideacode;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Pattern pattern = Pattern.compile("w3schools", Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher("Visit W3Schools!");
        boolean matchFound = matcher.find();
        if (matchFound){
            System.out.println("Match found");
        } else {
            System.out.println("Match not found");
        }

        /*
            *** Metacharacter ***
            .   ตัวอักษรอะไรก็ได้
            []  ใช้เพื่อค้นหาช่วงของอักษร
            [^] ไม่เอาตัวอักษรที่อยู่ในนี้
            ^   ขึ้นต้นประโยคด้วยคำนี้
            $   ต้องจบประโยคด้วยคำนี้
            ()  จัดกลุ่มว่าเป็นกลุ่มเดียวกัน
            |   ใช้แทนหรือ or

            *** Character Classes *** short-hand
            \w  [A-Za-z0-9_]
            \W  [^A-za-z0-9_]
            \a  [A-za-z]
            \s  [ \t] (space กับ tap)
            \_s [ \t\r\n\v\f] (space กับ tap และ whitespace ทุกตัว
            \S  [^ \t\r\n\v\f]
            \d  [0-9] (digits ตัวเลข)
            \D  [^0-9]
            \l  [a-z] (lowercase character)
            \u  [A-Z] (uppercase character)
            \x  [A-Fa-f0-9] (Hexadecimal digits)

            *** Quantification ***
            ?           มี หรือ ไม่มี ก็ได้
            *           มี หรือ ไม่มี ก็ได้ แล้วจะมีกี่ตัวก็ได้
            +           มีกี่ตัวก็ได้ อย่างน้อยต้องมีหนึ่งตัว
            {min,max}   มีได้ตั้งแต่ min ถึง max
         */
    }
}
