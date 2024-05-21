//Alex Miller
import java.io.*;
import java.util.*;

public class TreeNode { //each node on the tree

	private char op = ' ';
	private TreeNode left = null;
	private TreeNode right = null;

	public TreeNode (char c) { //sets the op char to a node

		op = c;
	}

	public char getop() { //get the op char

		return op;
	}

	public TreeNode getleft() { //gets the left node

		return left;
	}

	public TreeNode getright() { //gets the right node

		return right;
	}

	public void setop (char c) { //set the op value to a char

		op = c;
	}

	public void setleft (TreeNode n) { //sets the left node

		left = n;
	}

	public void setright (TreeNode n) { //sets the right node

		right = n;
	}

	public String build (String input) { //builds the left and right nodes

		if (op >= '0' && op <= '9') {
			return input;
		}
		right = new TreeNode(input.charAt(input.length()-1));
		input = right.build(input.substring(0,input.length()-1));
		//System.out.println(input);
		left = new TreeNode(input.charAt(input.length()-1));
		input = left.build(input.substring(0,input.length()-1));
		//System.out.println(input);
		return input;
	}

	public void PrintPrefix () { //prints the prefix expression

		System.out.print(op);
		if (left != null) {
			left.PrintPrefix();
		}
		if (right != null) {
			right.PrintPrefix();
		}
	}

	public void PrintInfix() { //prints the infix expression

		if (!(op >= '0' && op <= '9')) {
			System.out.print("(");
		}
		if (left != null) {
			left.PrintInfix();
		}
		System.out.print(op);
		if (right != null) {
			right.PrintInfix();
		}
		if (!(op >= '0' && op <= '9')) {
			System.out.print(")");
		}
	}

	public int Calculate() { //calculates the answer to the expression

		if (op >= '0' && op <= '9') {
			return op-48;
		}
		if (op == '+') {
			return (left.Calculate() + right.Calculate());
		}
		if (op == '*') {
			return (left.Calculate() * right.Calculate());
		}
		if (op == '/') {
			return (left.Calculate() / right.Calculate());
		}
		if (op == '-') {
			return (left.Calculate() - right.Calculate());
		}
		return 0;
	}
}