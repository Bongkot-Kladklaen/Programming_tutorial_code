package com.ideacode;

public interface IPhone {
    void call(String phoneNumber);
    void hangup();
    void sendSms(String phoneNumber, String message);
}
