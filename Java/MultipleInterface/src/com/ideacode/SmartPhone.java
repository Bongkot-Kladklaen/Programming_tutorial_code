package com.ideacode;

public class SmartPhone implements IPhone, ICamera, IGps{

    @Override
    public void takePhoto() {

    }

    @Override
    public void changeAperture() {

    }

    @Override
    public void changeShutterSpeed() {

    }

    @Override
    public void deletePhoto() {

    }

    @Override
    public void call(String phoneNumber) {

    }

    @Override
    public void hangup() {

    }

    @Override
    public void sendSms(String phoneNumber, String message) {

    }

    @Override
    public float receiveLat() {
        return 0;
    }

    @Override
    public float receiveLon() {
        return 0;
    }

    @Override
    public boolean isGpsEnabled() {
        return false;
    }
}
