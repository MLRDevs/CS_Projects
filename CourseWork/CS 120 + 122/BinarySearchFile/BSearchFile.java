//Alex Miller
import java.io.*;
import java.util.*;

public class BSearchFile { //takes in a file and a student ID number and searches the file for the ID number, if that ID number is in the file, then it prints what school it belongs to, if not then it prints where the ID number would be

	public static Scanner in, keyboard;

	private static RandomAccessFile words;

	public static void main(String[] args) throws Exception {

		keyboard = new Scanner(System.in);

		System.out.print("Enter a school database: ");
		String DataBase = keyboard.nextLine();
		in = new Scanner(new File(DataBase));
		words = new RandomAccessFile(DataBase, "r");

		while (true) { //loop to keep asking for a school ID until there is an empty string
			if (in.hasNextLine()) {
				System.out.print("Enter a school ID: ");
				String id = keyboard.nextLine();
				if (id == "") {
					break;
				}
				else {
					FindSchoolID(id);
				}
			}
			else { //if database is empty
				System.out.println("That database is empty");
				break;
			}
		}
		in.close();
		words.close();
	}
	public static String SearchFile(int recnum) throws Exception { //Searches the file 55 bytes at a time, which is the length of the ID numbers

		words.seek(55*recnum);

		byte[] ba = new byte[55];
		words.readFully (ba);
		return new String (ba);
	}

	public static void FindSchoolID (String id) throws Exception { //searches the database for the school ID given and prints whether it is in the database or not and where it is/could be

		int low = 0;
		int high = (int)(words.length() / 55)-1;
		int start = 0;
		int end = (int)(words.length() / 55);
		int av = (int)((low+high)/2);
		String RecordID = "";
		boolean found = false;
		while (high >= low && !found) { //Binary search code
			av = (high + low) / 2;
			String ba = SearchFile(av);
			RecordID = "";
			for (int i=0; i < 5; i++) { //taking the first five bytes from the 55 byte string
				char newba = ba.charAt(i);
				RecordID += newba;
			}
			if (RecordID.equals(id)) { //if the id was found
				found = true;
			}
			else if (RecordID.compareTo(id) > 0) {
				high = av-1;
			}
			else if (RecordID.compareTo(id) < 0) {
				low = av+1;
			}
		}

		if (found == true) { //printing the answer if it's equal to the id given
			System.out.println(SearchFile(av));
		}
		else if (high < start) { //printing if the id is before the first record
			System.out.println(id+" does not exist but would be before");
			high = start;
			System.out.println(SearchFile(start));
		}
		else if (low >= end) { //printing if the id is after the last record
			System.out.println(id+" does not exist but would be after");
			low = end;
			System.out.println(SearchFile(end - 1));
		}
		else { //printing if the id is in between the records but doesn't exist
			System.out.println(id+" does not exist but would fall between");
			System.out.println(SearchFile(high));
			System.out.println("and");
			System.out.println(SearchFile(low));
		}
	}
}