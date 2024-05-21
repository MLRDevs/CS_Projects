//Alex Miller
import java.io.*;
import java.util.*;

public class Tree { //expression tree

	private TreeNode root = null;

	public TreeNode getroot() { //gets the root of the tree

		return root;
	}

	public void setroot (TreeNode n) { //sets the root of the tree

		root = n;
	}

	public void build (String input) { //builds the tree

		if (input.equals("")) {
			return;
		}
		root = new TreeNode (input.charAt(input.length()-1));
		root.build (input.substring(0, input.length()-1));
	}

	public void PrintPrefix() { //prints the prefix expression

		if (root == null) {
			return;
		}
		System.out.print("Prefix: ");
		root.PrintPrefix();
		System.out.println();
	}

	public void PrintInfix() { //prints the infix expression

		if (root == null) {
			return;
		}
		System.out.print("Infix: ");
		root.PrintInfix();
		System.out.println();
	}

	public int Calculate() { //calculates the answer to the expression

		if (root == null) {
			return 0;
		}
		return root.Calculate();
	}

}