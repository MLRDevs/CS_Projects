//Alex Miller
//takes three sides of a triangle form user and determines if it's a valid  triangle
import java.io.*;
import java.util.*;

	public class ValidTriangle {

	private static Scanner in;

	public static void main (String [] args) {

		in = new Scanner (System.in);

		// get the sides from the user
		System.out.print ("Enter the first side:  ");
		double a = Double.parseDouble (in.nextLine());
		System.out.print ("Enter the second side:  ");
		double b = Double.parseDouble (in.nextLine());
		System.out.print ("Enter the third side:  ");
		Double c = Double.parseDouble (in.nextLine());

		// print whether the sides inputed result in a valid triangle or not
		if (a+b < c || a+c < b || b+c < a) System.out.println ("This is NOT a valid triangle.");
		else System.out.println ("This IS a valid triangle.");

	}
}