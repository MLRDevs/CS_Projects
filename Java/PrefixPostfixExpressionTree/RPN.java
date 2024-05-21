//Alex Miller
import java.io.*;
import java.util.*;

public class RPN { //converts postfix expression into an expression tree and prints the infix expression, prefix expression, and the answer to the expression

	public static Scanner in;

	public static void main(String[] args) {

		in = new Scanner(System.in);
		Tree xp = new Tree();
		System.out.print("Enter a postfix notation: ");
		String input = in.nextLine();

		xp.build(input);
		xp.PrintPrefix();
		xp.PrintInfix();
		System.out.println ("Answer: "+xp.Calculate());
	}
}