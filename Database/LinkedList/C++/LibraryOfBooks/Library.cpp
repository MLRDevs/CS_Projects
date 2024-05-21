//Alex Miller
//library of book titles, asks user for specific commands regarding the list
#include <iostream>
#include <cstdlib>
#include <string>
#include "Library.h"
#include "LL.h"
using namespace std;

int main(int argc, char** argv) { //asks user for a command and runs that command

	string command; //command string
	string t; //string without quotes
	LL* list = new LL(); //creating list

	while (true) { //keeps asking for commands
		cout << "Enter a command: ";
		cin >> command;
		for (int i = 0; i < command.length(); i++) { //change the command to lower case
			command.at(i) = tolower(command.at(i));
		}
		if (command == "add") { //adds a node to the list
			string title;
			cout << "Enter title of book: ";
			cin.ignore();
			getline(cin, title);
			for (int i = 1; i < title.length()-1; i++) { //removing the quotations in the string
				t += title.at(i);
			}
			title = t;
			list->Add(title);
		}
		else if (command == "print") { //prints the whole list in alphabetical order
			list->Print();
		}
		else if (command == "remove") { //removes nodes with the particular substring
			string sub;
			cout << "Enter a substring: ";
			cin >> sub;
			list->Remove(sub);
		}
		else if (command == "exit") {
			exit(1);
		}
		command = ""; //resetting the command to nothing to be entered again
		t = "";
	}
	delete list;

	return 0;
}