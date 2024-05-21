// Alex Miller
// get the sum of all the ints together, also with their squares and cubes
import java.io.*;
import java.util.*;

public class SSC {

	private static Scanner in;

	public static void main (String[] args) { // main

		in = new Scanner (System.in);

		// integers
		System.out.print ("Enter a positive integer: ");
		int integer = Integer.parseInt (in.nextLine());
		int sum = integer*(integer+1)/2;
		System.out.println ("Sum of Integers is: "+sum);

		// squares
		int sum2 = integer*(integer+1)*(2*integer+1)/6;
		System.out.println ("Sum of Squares is: "+sum2);

		// cubes
		int sum3 = (integer*integer)*(integer+1)*(integer+1)/4;
		System.out.println ("Sum of Cubes is: "+sum3);
}
}