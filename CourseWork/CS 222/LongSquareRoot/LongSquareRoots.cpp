//Alex Miller
//takes in a value to square root and a value to how many decimal places to square root, prints that value
#include <iostream>
#include <cstdlib>
#include <string>
#include "LongSquareRoots.h"
using namespace std;

int main(int argc, char** argv) { //asks for a non negative number to square root, how many decimal places, and then square roots it.

	cout << "Enter a non-negative number: ";
	string sqrt; //number to square root
	getline(cin, sqrt);
	while (sqrt < "0") { //making sure its a positive number
		cout << "That is negative, try again." << endl;
		cout << "Enter a non-negative number: ";
		getline(cin, sqrt);
	}
	cout << "How many decimal places? ";
	string dec; //amount of decimal places to square root
	getline(cin, dec);

	if (sqrt == "0") { //squre root of zero
		string s;
		string r = dec;
		while (stoi(dec) > 0) { //adding the right amount of zeros after the decimal point
			s += "0";
			dec = Subtract(dec, "1");
		}
		cout << sqrt << " to " << r << " decimal places is: 0." << s << endl; //printing the answer
	}
	else { //if square root is a positive
		SquareRoot(sqrt, dec);
	}

	return 0;
}
void SquareRoot(string sqrt, string dec) { //takes the square root of "sqrt" and to "dec" number of decimal places
	string oldsqrt = sqrt; 
	sqrt = AddZeros(sqrt,dec); //adding the zeros to the initial square root value
	int len = sqrt.length() * 2; //making the length of the array double the length of the square root value
	string* fours = new string[len]; //initializing array

	string g = "1"; //strings that will be multiplied to make the fours array
	string m = "4";
	int ct = 1; //counter to keep track of where the last fours is
	fours[0] = "1"; //intitializing the first value in the array to be 1
	for (int i = 1; i < len; i++) { //for loop to add the fours to the array
		string s = Multiply(g, m);
		if (Cmp(sqrt, s) == sqrt) { //if the square root value is still bigger than the next four then add it to the array
			fours[i] = s;
			g = s;
			ct++;
		}
		else { //continue to the next iteration
			continue;
		}
	}
	/*
	for (int i = 0; i < len; i++) { //testing the fours array to make sure it works as intended
		cout << fours[i] << endl;
	}
	*/

	string ans = "0";
	string n = sqrt; //initial value
	for (int i = ct-1; i >= 0; i--) { //for loop will start at the last four in the fours array and go until it reaches the start of the array
		string p = Multiply(fours[i], Add("1", Multiply("4", ans))); //after multiplying the fours array item by 4*ans+1
		if (Cmp(p, n) == n) { //if the subtraction will work
			n = Subtract(n, p);
			ans = Add("1", Multiply("2", ans)); //2*ans+1
		}
		else { 
			ans = Multiply("2", ans); //2*ans
		}
	}

	//cout << sqrt << " = " << ans << "^2 " << "+ " << n << endl; //testing to see if the algorithm is working
	Answer(ans, dec, sqrt, oldsqrt);
	delete[]fours; //deallocating

}
void Answer(string ans, string dec, string sqrt, string oldsqrt) { //puts the decimal place in the right spot and prints the answer
	string s = "";
	int j = ans.length() - stoi(dec); //getting the position of the first number to be behind the decimal
	for (int i = 0; i < stoi(dec); i++) { //runs until the end of how many decimal places value
		s += ans[j+i]; //adding the number in the position to s
	}
	string y;
	for (int i = 0; i < j; i++) { //adds all the numbers before the decimal point to a new string to print
		y += ans[i]; 
	}
	cout << "the square root of " << oldsqrt << " to " << dec << " decimal place(s) is: " << y << "." << s << endl;
}
string AddZeros(string sqrt, string dec) { //adding zeros to the original value to be square rooted
	dec = Multiply(dec, "2");
	for (int i = 0; i < stoi(dec); i++) {
		sqrt += "0";
	}
	return sqrt;
}
string Cmp(string a, string b) { //compares two strings, returns whichever one is bigger
	if (a.length() > b.length()) { //return a if a is a longer string
		return a;
	}
	else if (b.length() > a.length()) { //return b if b is a longer string
		return b;
	}
	else {
		for (int i = 0; i < a.length(); i++) { //for loop to check one char at a time which one is larger
			if (a.at(i) > b.at(i)) {
				return a;
			}
			else if (b.at(i) > a.at(i)) {
				return b;
			}
		}
	}
	return a;
}
void Trim(string& sqrt) { //takes the first char of the string off the string
	while (sqrt.length() > 1 && sqrt[0] == '0') {
		sqrt = sqrt.substr(1);
	}
}
string Add(string a, string b) { //adds the two strings together and returns the sum
	Trim(a);
	Trim(b);
	while (a.length() < b.length()) a = "0" + a;
	while (b.length() < a.length()) b = "0" + b;
	a = "0" + a; 
	b = "0" + b; 
	string ans = "";
	int carry = 0;
	for (int i = a.length() - 1; i >= 0; i--) {
		int sum = (a[i] - '0') + (b[i] - '0') + carry;
		ans = (char)(sum % 10 + '0') + ans;
		carry = sum / 10;
	}
	Trim(ans);
	return ans;
}
string Multiply(string a, string b) { //Multiplies the two strings and returns the product
	Trim(a);
	Trim(b);
	string sum = "0";
	for (int i = 0; i < a.length(); i++)
		for (int j = 0; j < b.length(); j++) {
			int prod = (a[i] - '0') * (b[j] - '0');
			string addend = to_string(prod);
			for (int k = 0; k < a.length() - 1 - i + b.length() - 1 - j; k++)
				addend += "0";
			sum = Add(sum, addend);
		}
	return sum;
}
string Subtract(string a, string b) { //subtracts the two strings and returns difference

	Trim(a);
	Trim(b);
	while (a.length() < b.length()) a = "0" + a;
	while (b.length() < a.length()) b = "0" + b;
	for (int i = 0; i < b.length(); i++)
		b[i] = (char)('9' - b[i] + '0');
	string diff = Add(Add(a, b), "1").substr(1);
	Trim(diff);
	return diff;
}