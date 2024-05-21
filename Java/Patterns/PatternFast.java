//Alex Miller
import java.io.*;
import java.util.*;
import java.math.*;

public class PatternFast { //take an int from user and give an output based on a sequence

	public static Scanner in;

	public static void main (String[] args) {

		in = new Scanner(System.in);
		System.out.print("Enter a value: ");
		int n = Integer.parseInt(in.nextLine());

		System.out.println("f("+n+") = "+Fib(n)); //printing the results
	}

	public static BigInteger Fib (int n) { //taking user inputed int then returning the output

		if (n == 0) {
			return new BigInteger("0");
		}
		if (n == 1) {
			return new BigInteger("1"); //base cases
		}
		if (n == 2) {
			return new BigInteger("1");
		}

		BigInteger Triple = new BigInteger("0"); //n-3
		BigInteger Duce = new BigInteger("1"); //n-2
		BigInteger Single = new BigInteger("1"); //n-1
		BigInteger Final = null;
		for (int i=3; i <= n; i++) {
			Final = (Single.multiply(new BigInteger("3"))).add(Duce.multiply(new BigInteger("2"))).add(Triple); //math for final output
			Triple = Duce;
			Duce = Single; //moving the values down the line
			Single = Final;
		}
		return Final; //returning the final value computed
	}
}