//Alex Miller
//Linked list
#include <iostream>
#include <cstdlib>
#include <string>
#include "LL.h"
using namespace std;

LL::LL() { //what the list has
	head = nullptr;
}
LL::~LL() { //deallocating
	delete head;
}
void LL::Sort() { //sorting the list
	if (head->Getnext()) { //if there is more than one item in the list
		if (head->Getsorted() == false) { //if the list still needs to be sorted
			head->Sort(this, head);
		}
	}
}
void LL::Sethead(LLN* n) { //setting n as the new head of the list
	head = n;
}
void LL::PrintSorted() { //print all the sorting booleans of all nodes (debugging)
	head->PrintSorted();
}
LLN* LL::Gethead() { //returns the head of the list
	return head;
}
void LL::Add(string s) { //adding a node to the list
	if (!head) {
		head = new LLN(s, nullptr, false);
	}
	else {
		head->Add(s);
	}
}
void LL::Print() { //printing the whole list
	if (head) {
		head->Print();
	}
	else {
		cout << "The list is empty!";
	}
}