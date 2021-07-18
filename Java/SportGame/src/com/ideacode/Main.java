package com.ideacode;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.Month;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
	// write your code here
        demo1();
    }

    public static void demo1(){
        Team teamA = new Team();
        teamA.setName("Cavaliers");
        teamA.setCity("Cleveland");
        List<Player> playersA = new ArrayList<Player>();
        playersA.add(new Player("LeBron","James","forward", LocalDate.of(1995, Month.MARCH,31)));
        playersA.add(new Player("Mike","Will","center", LocalDate.of(1994, Month.MARCH,2)));
        playersA.add(new Player("Jame","Jackson","guard", LocalDate.of(1992, Month.MARCH,29)));
        teamA.setPlayers(playersA);
        System.out.println(teamA);

        Team teamB = new Team();
        teamB.setName("Hawks");
        teamB.setCity("Atlanta");
        List<Player> playersB = new ArrayList<Player>();
        playersB.add(new Player("LeBron","James","forward", LocalDate.of(1995, Month.MARCH,31)));
        playersB.add(new Player("Mike","Will","center", LocalDate.of(1994, Month.MARCH,2)));
        playersB.add(new Player("Jame","Jackson","guard", LocalDate.of(1992, Month.MARCH,29)));
        teamB.setPlayers(playersB);
        System.out.println(teamB);

        Match m = new Match(teamA,teamB,"Cleveland", LocalDateTime.of(2014,Month.MARCH,12,16,0,0));
        System.out.println(m);


    }
}
