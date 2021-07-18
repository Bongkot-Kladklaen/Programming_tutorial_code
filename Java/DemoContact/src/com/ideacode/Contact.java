package com.ideacode;

import java.util.Locale;

public class Contact {
    private String firstname, lastName;
    private String phoneNumber;

    public Contact(String firstname, String lastName, String phoneNumber) {
        setFirstname(firstname);
        setLastName(lastName);
        setPhoneNumber(phoneNumber);
    }
    public Contact(){}

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {

        this.firstname = Utils.capitalizedFirstCharOfString(firstname);
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = Utils.capitalizedFirstCharOfString(lastName);
    }

//    private String capitalizedFirstCharOfString(String s){
//        return s.substring(0,1).toUpperCase() + s.substring(1).toLowerCase();
//    }

    public String getPhoneNumber() {
        return prettyFormatPhoneNumber();
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber.replaceAll("[\\D]","");
    }

    public String prettyFormatPhoneNumber(){
        return phoneNumber.replaceAll("(\\d{3})(\\d{3})(\\d{4})","$1-$2-$3");
    }
    @Override
    public String toString() {
        return "Contact{" +
                "firstname='" + firstname + '\'' +
                ", lastName='" + lastName + '\'' +
                ", phoneNumber='" + prettyFormatPhoneNumber() + '\'' +
                '}';
    }
}
