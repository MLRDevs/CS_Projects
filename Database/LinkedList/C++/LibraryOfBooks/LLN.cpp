//Alex Miller
//each node inside the linked list
#include <iostream>
#include <cstdlib>
#include <string>
#include "LLN.h"
using namespace std;

LLN::LLN(string t, LLN* n) { //what every node has
	title = t;
	next = n;
}
LLN::~LLN() { //deallocates data
	delete next;
}
string LLN::getTitle() { //gets the title 
	return title;
}
void LLN::setNext(LLN* n) { //sets the next node
	next = n;
}
LLN* LLN::getNext() { //returns the next node
	return next;
}
string LLN::getLower(string s) { //changes the given string to all lower case and returns the result
	for (int i = 0; i < s.length(); i++) {
		s.at(i) = tolower(s.at(i));
	}
	return s;
}
bool LLN::hasNext() {
	if (next) {
		return true;
	}
	return false;
}
bool LLN::Repeat(string t) { //checks if there is a repeat node 
	if (getLower(t) == getLower(title)) {
		return true;
	}
	if (next) {
		return next->Repeat(t);
	}
}
void LLN::Add(string t, LLN* prev) { //adds a new node to the list in alphabetical order
	if (next == nullptr) { //if there is no next
		next = new LLN(t, next);
		prev->setNext(next); //sets the previous node's next to the new next
	}
	else { //if there is a next
		if (prev->getLower(prev->getTitle()) < getLower(t) && next->getLower(next->getTitle()) > getLower(t)) { //if the new node resides somewhere inside the list and is not a repeat
			Temp = new LLN(t, next);
			prev->setNext(Temp);
		}
		else {
			next->Add(t, next);
		}
	}
}
void LLN::Print() { //prints the whole list
	cout << title << endl;
	if (next != nullptr) {
		next->Print();
	}
}
void LLN::Remove(string s, LLN* prev) { //removes the nodes with the particular substring
	string t = getLower(title);
	string p = getLower(s);
	int n = s.length();
	for (int i = 0; i < t.length(); i++) {
		string r = t.substr(i, n);
		if (r == p) {
			if (next) {
				prev->setNext(next);
				next->Remove(p, prev);
			}
			else {
				prev->setNext(nullptr);
			}
		}
	}
	if (next) {
		next->Remove(p, this);
	}
	else {
		this->setNext(nullptr);
	}
}