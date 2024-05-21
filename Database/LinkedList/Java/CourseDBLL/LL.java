//Alex Miller
import java.io.*;
import java.util.*;

public class LL { //Linked List comprising of Course ID's and Course Names

	private LLN head = null;
	private LLN Temp = null;

	public LLN gethead() {

		return head;

	}

	public void AddCourse(String CourseID, String CourseName) { //adding new courses

			if (head == null) { //if list is empty
				head = new LLN (CourseID, CourseName, head);
			}
			else { //if list is not empty
				if (head.getCourse().compareTo(CourseID) > 0){ //if the course goes before the first course in the list
					head = new LLN (CourseID, CourseName, head);
				}
				else { //if the course goes sometime after the first course in the list
					head.AddCourse(CourseID, CourseName, head);
				}
			}
	}

	public void DeleteCourse(String CourseID) { //deleting courses

		if (head == null) { //if list is empty
			return;
		}
		else { //if list is not empty
			if (head.getCourse().equals(CourseID)) { //if the CourseID given is equal to the course at the top of the list
			head = head.getnext();
			}
			else {
				head.DeleteCourse(CourseID, null); //if the CourseID given is somewhere in the list and not at the start
			}
		}
	}

	public boolean SearchCourse(String CourseID) { //searching for a specific course

		if (head == null) { //if list is empty
			return false;
		}
		else { //if list is not empty
			return head.SearchCourse(CourseID);
		}
	}

/*
	public void print() {
		if (head != null) {
			head.print();
		}
	}
*/
}