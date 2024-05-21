//Alex Miller
//ask the user for a string then changes all the vowels to capitals
import java.io.*;
import java.util.*;

public class CapitalizeVowels {

	private static Scanner in;

	public static void main (String [] args) {

	in = new Scanner (System.in);

	// get word from user
	System.out.print ("Please enter a string:  ");
	String words= "";
	words = in.nextLine();
	String newword = "";

	// build new string with each vowel being uppercase
	for (int i=0; i < words.length(); i++) {
		if (words.charAt(i) == 'a') newword += 'A';
		else if (words.charAt(i) == 'e') newword += 'E';
		else if (words.charAt(i) == 'i') newword += 'I';
		else if (words.charAt(i) == 'o') newword += 'O';
		else if (words.charAt(i) == 'u') newword += 'U';
		else newword += words.charAt(i);
	}
	System.out.println(newword);

	}
}