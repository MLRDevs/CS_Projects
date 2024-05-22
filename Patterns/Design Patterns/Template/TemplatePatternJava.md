# Template Method

*Forces*: You want to use the same pieces of code, but with slight differences

*Solution*: The Template Pattern allows us to use a template of a piece of code, and change what we need to do

### The following example will use Java
```
import java.io.*;
import java.util.*;

public class Template { // Template Class
	public static void main(String[] args) { // main method
		Hockey hockey = new Hockey(); // create a new Hockey instance
		hockey.Play(); // play hockey

		System.out.println();

		Basketball basketball = new Basketball(); // create a new Basketball instance
		basketball.Play(); // play basketball
	}
}
class Sport { // Sport class, most methods get overriden by Hockey and Basketball
	public void PrintSport() { // print the sport
		System.out.println("Sport");
	}
	public void PrintPlayers() { // print the amount of players
		System.out.println("0");
	}
	public void Play() { // play method, calls other methods in this class
		TemplateSport();
		PrintSport();
		PrintPlayers();
	}
	public void TemplateSport() { // just to show that not every method needs to be overriden
		System.out.println("This is a sport");
	}
}
class Hockey extends Sport { // Hockey class, inherits from Sport
	private int players = 6;
	private String sport = "Hockey";

	@Override
	public void PrintSport() { // print "Hockey" instead of "Sport" from the Sport class
		System.out.println(sport);
	}
	@Override
	public void PrintPlayers() { // prints something different than the Sport class
		System.out.println(sport + " has " + players + " players");
	}
}
class Basketball extends Sport { // Basketball class that inherits from the Sport class
	private int players = 5;
	private String sport = "Basketball";

	@Override
	public void PrintSport() { // print "Basketball" instead of "Sport" from the Sport class
		System.out.println(sport);
	}
	@Override
	public void PrintPlayers() { // prints something different than the sport class
		System.out.println(sport + " has " + players + " players");
	}
}
```
### Output:
```
This is a sport
Hockey
Hockey has 6 players

This is a sport
Basketball
Basketball has 5 players
```

*Preceding Pattern*

[Singleton](/SingletonJava.md)

*Following Pattern*

[Observer](/ObserverPattern.md)