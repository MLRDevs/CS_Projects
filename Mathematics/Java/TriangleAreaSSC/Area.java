// Alex Miller
// get the area of a triangle
import java.io.*;
import java.util.*;

	public class Area {

		private static Scanner in;

		public static void main (String[] args) {

		in = new Scanner (System.in);

		// first side
		System.out.print ("Enter the first side of the triangle:  ");
		double a = Double.parseDouble (in.nextLine());
		System.out.print (a);

		// second side
		System.out.print ("Enter the second side of the triangle:  ");
		double b = Double.parseDouble (in.nextLine());
		System.out.print (b);

		// third side
		System.out.print ("Enter the third side of the triangle:  ");
		double c = Double.parseDouble (in.nextLine());
		System.out.print (c);

		// print result
		System.out.print ("You're area for the triangle is:  ");
		double s = (a+b+c)/2;
		double area = Math.sqrt(s*(s-a)*(s-b)*(s-c));
		System.out.println (area);



}
}