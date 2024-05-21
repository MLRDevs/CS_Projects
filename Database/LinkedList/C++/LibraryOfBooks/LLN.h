//Alex Miller
//Each node inside of the linked list
#ifndef _LLN_
#define _LLN_

#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class LL;
class LLN {

private:
	string title; //title of the book
	LLN* next; //the next node 
	LLN* Temp; //temporary node

public:
	LLN(string t, LLN* n); //create a new node
	~LLN(); //deallocate data
	void Add(string t, LLN* prev); //adding a new node
	void Print(); //printing all the nodes
	void Remove(string s, LLN* prev); //remove the nodes with the specific substring

	string getTitle(); //getting the title of the node
	string getLower(string s); //changing the string so lowercase and returning it
	bool hasNext(); //returns true if there is a next
	void setNext(LLN* n); //setting the next node
	LLN* getNext(); //returns the next node
	bool Repeat(string t); //returns true if the title of the entered book is already in the list, false if not
};

#endif

