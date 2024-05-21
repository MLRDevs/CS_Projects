//Alex Miller
//takes a user inputed string and prints all the longest nondecreasing runs
import java.io.*;
import java.util.*;

public class Run {

	public static Scanner in;
	public static int n;

	public static void main(String[] args) {

		in = new Scanner(System.in);
		System.out.print("Enter a string: ");
		String Text = in.nextLine();
		Print(Text,n);
	}

	public static boolean run (String Text) { //tests if the whole string is a nondecreasing run

		int ct = 0;
		for (int i=0; i < Text.length()-1; i++) {
			if (Text.charAt(i) <= Text.charAt(i+1)) {
				ct++;
			}
		}
		if (ct+1 == Text.length()) {
			return true;
		}
		else {
			return false;
		}
	}

	public static boolean RunLength (String Text, int n) { //tests if each substring of the Text is a run

		for (int i=0; i < Text.length()-n+1; i++) {
			if (run(Text.substring(i,i+n)) == true) {
				return true;
			}
		}
		return false;

	}

	public static int LongRun (String Text) { //returns the length of the longest run

		for (int i=Text.length(); i >= 1; i--) {
			if (RunLength(Text,i)) {
				return i;
			}
		}
		return 0;
	}

	public static void Print (String Text, int n) { //prints all the longest runs

		System.out.println("The maximum runs are: ");

		for (int i=0; i < Text.length()-LongRun(Text)+1; i++) {
			if (run(Text.substring(i,i+LongRun(Text))) == true) {
				System.out.println(Text.substring(i,i+LongRun(Text)));
			}
		}
	}
}