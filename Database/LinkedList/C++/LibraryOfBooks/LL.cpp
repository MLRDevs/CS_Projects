//Alex Miller
//Linked list of book titles
#include <iostream>
#include <cstdlib>
#include <string>
#include "LL.h"
#include "LLN.h"
using namespace std;

LL::LL() { //what the list holds
	head = nullptr;
}
LL::~LL() { //deallocates data
	delete head;
}
string LL::getLower(string s) { //changes the given string to lower case and returns result
	for (int i = 0; i < s.length(); i++) {
		s.at(i) = tolower(s.at(i));
	}
	return s;
}
bool LL::Repeat(string t) {
	if (head) {
		if (head->getLower(head->getTitle()) == getLower(t)) {
			return true;
		}
		else {
			return head->Repeat(t);
		}
	}
}

void LL::Add(string t) { //adds a new node to the list in alphabetical order
	if (head != nullptr) {
		if (head->Repeat(t) == true) {
			cout << "that book title is already in the list!" << endl;
			return;
		}
		if (head->getLower(head->getTitle()) > getLower(t)) { //if the new node comes before the head
			head = new LLN(t, head);
		}
		else {
			head->Add(t, head); //if the new node comes after the head
		}
	}
	else { //if the list is empty
		head = new LLN(t,head);
	}
}
void LL::Print() { //prints the nodes in the list
	if (head) {
		head->Print();
	}
}
void LL::Remove(string sub) { //removes all nodes with the specific substring
	if (head) { //if list is not empty
		string s = getLower(sub);
		string t = getLower(head->getTitle());
		int n = sub.length();
		for (int i = 0; i < t.length()-1; i++) {
			string r = t.substr(i, n);
			if (r == s) {
				if (head->hasNext()) {
					head = head->getNext();
					Remove(s); 
				}
				else {
					cout << "List is empty" << endl;
					head = nullptr;
					return;
				}
			}
		}
		head->Remove(s, head);
	}
	else { //if the list is empty
		cout << "List is empty" << endl;
	}
}
