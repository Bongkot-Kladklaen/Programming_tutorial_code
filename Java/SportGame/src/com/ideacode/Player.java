package com.ideacode;

import java.time.LocalDate;

public class Player {
    private String firstname, lastName, position;
    private LocalDate dob;

    public Player(String firstname, String lastName, String position, LocalDate dob) {
        this.firstname = firstname;
        this.lastName = lastName;
        this.position = position;
        this.dob = dob;
    }

    public Player() {
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public LocalDate getDob() {
        return dob;
    }

    public void setDob(LocalDate dob) {
        this.dob = dob;
    }

    @Override
    public String toString() {
        return "Player{" +
                "firstname='" + firstname + '\'' +
                ", lastName='" + lastName + '\'' +
                ", position='" + position + '\'' +
                ", dob=" + dob +
                '}';
    }
}
