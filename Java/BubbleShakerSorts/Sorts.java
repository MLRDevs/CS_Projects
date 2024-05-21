//Alex Miller
import java.io.*;
import java.util.*;

public class Sorts { //takes an array of strings and uses bubble and shaker sorts to sort them and prints whichever one had the fewest comparisons

	public static Scanner in;

	public static void main(String[] args) {

		in = new Scanner(System.in);
		System.out.print("Enter amount of strings: ");
		int amount = Integer.parseInt(in.nextLine());
		String[] words = new String[amount];
		for(int i=0; i < amount; i++) { //taking users strings and inserting them into array
			System.out.print("Enter string "+(i+1)+": ");
			words[i] = in.nextLine();
		}
		String[] Bubble = words.clone();//cloning the array
		String[] Shaker = words.clone();

		int Bct = BubbleSort(Bubble);//setting the cloned arrays to an int for each sorting method
		int Sct = ShakerSort(Shaker);


		System.out.println();

		System.out.println("Bubble sort sorted with "+Bct+" comparisons"); //printing comparison counts
		System.out.println("Shaker sort sorted with "+Sct+" comparisons");
		System.out.println();


		if (Bct > Sct) { //if else blocks printing which one had fewer comparisons
			System.out.println("ShakerSort had fewer comparisons with "+Sct+" comparisons");
		}
		else if (Sct > Bct) {
			System.out.println("BubbleSort had fewer comparisons with "+Bct+" comparisons");
		}
		else {
			System.out.println("BubbleSort and ShakerSort had the same comparisons with "+Bct+" comparisons");
		}
		System.out.println();
		System.out.println("Bubble Sort:");
		for (int i=0; i < amount; i++) {
			System.out.println(Bubble[i]);
		}
		System.out.println();
		System.out.println("Shaker Sort:");
		for (int i=0; i < amount; i++) {
			System.out.println(Shaker[i]);
		}

	}
	public static int BubbleSort(String[] A){ //Bubble sorts the array that the user inputed

		int ct = 0;
		int nct = 0;
		for (int i=A.length-1; i > 0; i-=(1+nct)) {
			nct = 0;
		    for (int j=0; j < i; j++) {
		    	ct++;
		    	if (A[j].compareTo(A[j+1]) > 0) {
		     		String t = A[j];
		     		A[j] = A[j+1];
		     		A[j+1] = t;
		     		nct = 0;
		    	}
		    	else {
					nct++;
				}
		   }
		}
  		return ct; //Returning the comparison count
	}
	public static int ShakerSort(String[] A) { //Shaker sorts the array the user inputed

		int nct = 0;//counter for non swapping
		int ct = 0;//counter for comparisons
		int first = 0;//setting the first unlocked position
		int last = A.length-1;//setting the last unlocked position
		while (first < last) {
			for (int i=last; i > first; i--) {//sorting from the back to the front
				ct++;
				if (A[i].compareTo(A[i-1]) < 0) {//comparing strings then swapping when needed
					String temp = A[i];
					A[i] = A[i-1];
					A[i-1] = temp;
					nct = 0;
				}
				else {
					nct++;
				}
			}
			first+=(1+nct);
			for (int j=first; j < last; j++) {//sorting from the front to the back
				ct++;
				if (A[j].compareTo(A[j+1]) > 0) {//comparing strings then swapping if needed
					String temp = A[j];
					A[j] = A[j+1];
					A[j+1] = temp;
					nct = 0;
				}
				else {
					nct++;
				}
			}
			last-=(1+nct);
		}
		return ct; //returning the comparison count
	}
}