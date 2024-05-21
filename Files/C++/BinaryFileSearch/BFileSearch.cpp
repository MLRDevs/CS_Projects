//Alex Miller
//takes in a file and searches for the specific record
#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include "BFileSearch.h"
using namespace std;

int main(int argc, char** argv) { //asks user for a file name, then asks for a record and reports if that record is in the file or not 
	string fname;
	cout << "Enter a file: ";
	cin >> fname;

	fstream in(fname, ios::in);
	string word = "";
	for (int i = 0; i < 4; i++) { //getting the four numbers at the start of the file 
		char c;
		in.get(c);
		word += c;
	}

	int n = atoi(word.c_str()); //amount of letters per word
	in.seekg(0, ios::end); //skip to the end of the file
	int fsize = in.tellg(); //file size
	int wct = (fsize - 4) / n; //amount of words

	//entering the record the user wants to search for 
	string record;
	cout << "Enter the record you want to search: ";
	cin >> record;

	Search(n, wct, record, in);

	in.close(); //closing the file
	return 0;
}
void Search(int n, int wct, string record, fstream& in) { //searches the file for the specific record the user wants

	int low = 0;
	int high = wct - 1;
	string RecordTwo = record; //record in all lower case
	for (int i = 0; i < n; i++) { //setting recordtwo to record but all lower case
		RecordTwo.at(i) = tolower(record.at(i));
	}
	string WordTwo = "";
	int B = 4; //byte to start at
	int ct = 0; //counter for words
	int av = (high + low) / 2;
	string word = ""; //string to hold the record we are comparing to the user record
	bool found = false;
	while (low <= high && found == false) {
		B = 4;
		ct = 0;
		av = (low + high) / 2;
		while (ct != av) { //while the counter of the word we are on is not equal to the word we are about to search
			B += n;
			ct++;
		}
		//cout << low << " " << high << " " << av << " " << B << " " << ct  << " " << record << " " << word << endl;
		in.seekg(B);
		word = "";
		for (int i = 0; i < n; i++) { //gets the letters from the word we are searching and adds it to the string
			char p;
			in.get(p);
			word += p;
		}
		WordTwo = word; //setting wordtwo to word
		for (int i = 0; i < n; i++) { //changing wordtwo to all lower case
			WordTwo.at(i) = tolower(word.at(i));
		}
		//cout << record << " " << word << endl;
		if (WordTwo == RecordTwo) { //if the word and record are equal
			found = true;
			//cout << found << endl;
		}
		else if (WordTwo < RecordTwo) { //if the word is less than the record
			low = av + 1;
		}
		else if (WordTwo > RecordTwo) { //if the word is greater than the record
			high = av - 1;
		}
		//cout << low << " " << high  << " " << av << " " << B << " " << ct  << " " << record  << " " << word << endl;
	}

	//outcome if the record was found or not
	if (found == true) {
		cout << record << " was in the file";
	}
	else if (found == false) {
		cout << record << " was not in the file";
	}
	
}