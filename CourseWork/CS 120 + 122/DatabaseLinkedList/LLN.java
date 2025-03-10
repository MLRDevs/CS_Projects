//Alex Miller
import java.io.*;
import java.util.*;

public class LLN { //Each node of the Linked List

	private String CourseID = "";
	private String CourseName = "";
	private LLN Next = null;
	private LLN Temp;


	public LLN (String courseid, String coursename, LLN next) { //what every node has

		CourseID = courseid;
		CourseName = coursename;
		Next = next;

	}

	public String getCourse() { //getting the CourseID

		return CourseID;
	}

	public LLN getnext() { //getting the next node

		return Next;
	}

	public void setCourse (String course) { //setting the course

		CourseID = course;
	}

	public void setnext (LLN C) { //setting the next node

		Next = C;
	}
/*	public void print() {

		System.out.println(CourseID+": "+CourseName);
		if (Next != null) {
			Next.print();
		}

	}
*/

	public void AddCourse (String CourseID, String CourseName, LLN Prev) { //adds a new course to the list in the right spot

		if (Next == null) { //if the course goes at the end of the list
			Next = new LLN (CourseID, CourseName, null);
		}
		else { //if the course goes somewhere in the list
			if (Prev.getCourse().compareTo(CourseID) < 0 && Next.getCourse().compareTo(CourseID) > 0) { //tests if the course is in between the list
				Temp = new LLN (CourseID, CourseName, Next);
				Prev.setnext(Temp);
			}
			else {
				Next.AddCourse(CourseID, CourseName, Next); //if the course is in between the list, but higher than next then next tries to add the course instead
			}
		}
	}
	public void DeleteCourse (String CourseID, LLN Prev) { //deleting a specific course node

		if (Next != null) {
			Next.DeleteCourse(CourseID, this);
		}
		if (CourseID.equals(this.getCourse())) {
			if (Prev != null) {
				Prev.setnext(Next);
			}
		}

	}

	public boolean SearchCourse(String CourseID) { //searches for course user enters and gives appropriate output

		if (this.getCourse().equals(CourseID)) { //if user entered course is the right course
			System.out.println(CourseID+": "+CourseName);
			return true;
		}
		else if (this.getCourse().compareTo(CourseID) > 0) { //if user entered course doesn't exist but would fall before the head of the list
			System.out.println("This course doesn't exist but would be before: ");
			System.out.println(this.getCourse());
			return false;
		}
		else if (Next != null) {
			if (this.getCourse().compareTo(CourseID) < 0 && Next.getCourse().compareTo(CourseID) > 0) { //if user entered course doesn't exist but would be in between two courses
				System.out.println("This course doesn't exist but would fall between: ");
				System.out.println(this.getCourse()+" and "+Next.getCourse());
				return false;
			}
		}
		else if (this.getCourse().compareTo(CourseID) < 0 && Next == null) { //if user entered course doesn't exist and would fall after last node in the list
			System.out.println("This course doesn't exist but would be after: ");
			System.out.println(this.getCourse());
			return false;
		}
		return Next.SearchCourse(CourseID);
	}
}