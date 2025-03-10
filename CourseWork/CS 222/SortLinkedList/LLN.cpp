//Alex Miller
//nodes for linked list
#include<iostream>
#include <cstdlib>
#include <string>
#include "LLN.h"
#include "LL.h"
using namespace std;

LLN::LLN(string w, LLN* n, bool s) { //what every node has
	word = w;
	next = n;
	sort = s;
}
LLN::~LLN() { //deallocating
	delete next;
}
void LLN::Sort(LL* L, LLN* B) { //gets to the next unsorted node and then calls the sort method
	if (next) {
		if (next->Getsorted() == false && next->Getnext()) { //gets to the next unsorted node and calls the method to sort it
			next->Sort(L,this);
		}
		else {
			SortThis(L, B); //sort the node
		}
	}
}
void LLN::SortThis(LL* L, LLN* B) { //sorts this into the right place in the list
	if (next) {
		if (next->Getsorted() == true && this == L->Gethead()) { //special case if this is the head node
			LLN* n = next;
			if (n->Getnext()) { //if there is a node that this can point to
				this->Setnext(n->Getnext());
			}
			else {
				this->Setnext(nullptr);
			}
			n->Setnext(this);
			L->Sethead(n); //setting the new head
			this->SortThis(L, n); //sorting the list again
		}
		if (this->Getword() >= next->Getword()) { //if this needs to be swapped
			LLN* n = next;
			LLN* t = this;
			if (n->Getnext()) { //if the node after next is null
				this->Setnext(n->Getnext());
			}
			else {
				this->Setnext(nullptr);
			}
			B->Setnext(n);
			n->Setnext(this);
			n->Changesorted(); //changing the boolean value to true
			if (this->Getnext()) { //if this is not the last node, try sorting it again
				if (this->Getword() >= this->Getnext()->Getword()) {
					this->SortThis(L, n);
				}
				else { //if this is not the last node but cannot move anymore down the list
					this->Changesorted();
					L->Sort();
				}
			}
			else { //if this is the last node then it is sorted
				this->Changesorted();
				L->Sort();
			}
		}
		else { //if this is the last node then it is sorted
			this->Changesorted();
			L->Sort();
		}
	}
}
void LLN::Setnext(LLN* n) { //setting next to n
	next = n;
}
LLN* LLN::Getnext() { //getting next
	return next;
}
void LLN::PrintSorted() { //print all the sorting booleans of all nodes (debugging)
	cout << this->Getsorted() << endl;
	if (next) {
		next->PrintSorted();
	}
}
string LLN::Getword() { //getting the word
	return word;
}
bool LLN::Getsorted() { //returns true if the node is in the right spot, false if it is not
	return sort;
}
void LLN::Changesorted() { //changes the boolean value to true, call if the node is where it needs to be
	sort = true;
}
void LLN::Add(string s) { //adding a node to the list
	if (!next) {
		next = new LLN(s, nullptr, false);
	}
	else {
		next->Add(s);
	}
}
void LLN::Print() { //printing the whole list
	cout << this->Getword() << endl;
	if (next) {
		next->Print();
	}
}