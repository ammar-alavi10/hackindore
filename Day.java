package com.ammar.restapitry;

public class Day {

    private String outlook;
    private String temp;
    private String humidity;
    private String windy ;
    private String play;

    public Day(String outlook, String temp, String humidity, String windy, String play) {
        this.outlook = outlook;
        this.temp = temp;
        this.humidity = humidity;
        this.windy = windy;
        this.play = play;
    }

    public String getPlay() {
        return play;
    }
}
