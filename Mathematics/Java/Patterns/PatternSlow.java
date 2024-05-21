//Alex Miller
import java.io.*;
import java.util.*;
import java.math.*;

public class PatternSlow { //takes an int by the user, then gives the output based on the sequence

	public static Scanner in;

	public static void main (String[] args) {

		in = new Scanner(System.in);
		System.out.print("Enter a value: ");
		int n = Integer.parseInt(in.nextLine());


		System.out.println("f("+n+")  =  "+Fib(n)); //printing result
	}

	public static BigInteger Fib (int n) { //takes input int from user, runs output back through this same method for a final output

		if (n == 0) {
			return new BigInteger ("0");
		}
		if (n == 1) {
			return new BigInteger ("1"); //base cases
		}
		if (n == 2) {
			return new BigInteger ("1");
		}
		return ((Fib(n-1)).multiply(new BigInteger("3"))).add((Fib(n-2)).multiply(new BigInteger("2"))).add(Fib(n-3)); //return the output for the math of the sequence
	}
}