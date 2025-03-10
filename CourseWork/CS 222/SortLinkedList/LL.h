//Alex Miller
//Methods for linked list
#ifndef _LL_
#define _LL_
#include <iostream>
#include <cstdlib>
#include <string>
#include "LLN.h"
using namespace std;

class LLN;
class LL { //what the list has

private:
	LLN* head; //first node in the list

public:
	LL(); //creating the list
	~LL(); //deallocating
	void Sort(); //sorting the list
	void Sethead(LLN* n); //setting n as the new head of the list
	LLN* Gethead(); //returns the head of the list
	void Add(string s); //adding a node to the list
	void Print(); //printing the whole list
	void PrintSorted(); //print all the sorting booleans of all nodes (debugging)
};

#endif

