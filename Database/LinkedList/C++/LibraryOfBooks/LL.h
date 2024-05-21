//Alex Miller
//Linked list of book titles
#ifndef _LL_
#define _LL_

#include <iostream>
#include <cstdlib>
#include <string>
#include "LLN.h"
using namespace std;

class LLN;

class LL {

private:
	LLN* head; //first node in the list
	bool same = false; //boolean for remove method

public:
	LL(); //linked list
	~LL(); //deallocates data

	string getLower(string s); //changing the string so lowercase and returning it
	bool Repeat(string t); //checking if the title is a repeat in the list

	void Add(string t); //adding a new node 
	void Print(); //printing all nodes
	void Remove(string sub); //remove the nodes with specific substring

};

#endif

