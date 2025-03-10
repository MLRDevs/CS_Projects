// Alex Miller
// Singleton Pattern Example
import java.io.*;
import java.util.*;

public class Singleton { // main class
	public static void main(String[] args) { // main metho
		SingletonObj a = SingletonObj.getInstance(); // create SingletonObj a
		a.setName("Alex"); // set the name of a to "Alex"
		a.Print(); // print a

		SingletonObj b = SingletonObj.getInstance(); // create SingletonObj b
		b.Print(); // print b, also prints "Alex"

		// both of the memory locations are the same since they are the same object
		System.out.println("Memory location of a: " + a);
		System.out.println("Memory location of b: " + b);
	}
}
class SingletonObj { // Singleton Object class
	private static SingletonObj Inst = null; // initialize to null
	private String name; // data

	public static SingletonObj getInstance() { // get the instance of the Singleton Object
		if (Inst == null) { // if Inst is null then make a new SingletonObj, if not return the one already created
			Inst = new SingletonObj();
			return Inst;
		}
		else return Inst;
	}
	public void setName(String n) { // set the name data of the SingletonObj
		name = n;
	}
	public void Print() { // print the name of the SingletonObj
		System.out.println(name);
	}
}

