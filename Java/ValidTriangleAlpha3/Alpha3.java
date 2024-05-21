//Alex Miller
//takes three words from user and prints the first word alphabetically
import java.io.*;
import java.util.*;

	public class Alpha3 {

	private static Scanner in;

	public static void main (String [] args) {

		in = new Scanner (System.in);

		// get first word
		String First = "";
		System.out.print ("Enter a word:  ");
		First = in.nextLine();

		// get second word
		String Second = "";
		System.out.print ("Enter another word:  ");
		Second = in.nextLine();

		// get third word
		String Third = "";
		System.out.print ("Enter a third word:  ");
		Third = in.nextLine();

		// test each word and print the first one alphabetically
		if (First.compareTo(Second) <= 0 && First.compareTo(Third) <0)
			System.out.println ("The first word is:  "+First);
		else
			if (Second.compareTo(First) <= 0 && Second.compareTo(Third) < 0)
				System.out.println ("The first word is:  "+Second);
			else
				System.out.println ("The first word is:  "+Third);

	}
}