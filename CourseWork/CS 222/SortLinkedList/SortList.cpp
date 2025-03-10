//Alex Miller
//Asks user for items for a linked list, adds those items in the list, sorts the list, then prints the whole list
#include<iostream>
#include <cstdlib>
#include <string>
#include "SortList.h"
#include "LL.h"
using namespace std;

int main(int argc, char** argv) { //Asks user for items for a linked list, adds those items in the list, sorts the list, then prints the whole list

	LL* List = new LL(); //creating the list
	string s = "a";
	while (s != "") { //while there isn't a black line entered
		cout << "Enter a list item: ";
		getline(cin, s);
		if (s != "") {
			List->Add(s); //adds to the list
		}
	}
	if (List->Gethead()) { //if the list is not empty, sort it
		List->Sort();
	}
	List->Print(); //print the list
	//List->PrintSorted();
	
	delete List; //deleting the list

	return 0;
}
