//Alex Miller
import java.io.*;
import java.util.*;

public class DB {

	public static Scanner in;

	public static void main (String[] args) { //takes a user command and does the right command with the courses in a linked list

		in = new Scanner(System.in);

		LL Courses = new LL(); //creating the linked list
		//Courses.AddCourse ("CS 122", "Computer Science II");
		//Courses.AddCourse ("CS 201", "Programming in C++");

		while (true) {
			String CourseID = "";
			String CourseName = "";
			System.out.print("Enter command: ");
			String com = in.nextLine();
			if (com.equals("ADD")) { //adding a course, takes the courseID and the name and adds it to the linked list in order
				System.out.print("What course do you wish to add? ");
				CourseID = in.nextLine();
				System.out.print("What is the course name? ");
				CourseName = in.nextLine();
				Courses.AddCourse(CourseID, CourseName);
				System.out.println("This course has been added");
				//Courses.print();
			}
			else if (com.equals("DELETE")) { //deletes the right course the user wants in the list
				System.out.print("What course do you wish to delete? ");
				CourseID = in.nextLine();
				Courses.DeleteCourse(CourseID);
				System.out.println("This course has been deleted");
				//Courses.print();
			}
			else if (com.equals("SEARCH")) { //searches for a specific course in the list, tells the user what the name and courseID of the course they entered, if it is not there then it tells the user where in the list that course would be
				System.out.print("What course are you looking for? ");
				CourseID = in.nextLine();
				Courses.SearchCourse(CourseID);
			}
			else if (com.equals("QUIT")) { //quits the program
				System.exit(0);
			}
		}
	}
}