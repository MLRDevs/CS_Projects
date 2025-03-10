//Alex Miller
//Node methods
#ifndef _LLN_
#define _LLN_

#include<iostream>
#include <cstdlib>
#include <string>
#include "LL.h"
using namespace std;

class LL;
class LLN { //what every node in the list has
	
private:
	LLN* next;
	string word;
	bool sort;

public:
	LLN(string w, LLN* n, bool s); //creating the node
	~LLN(); //deallocating
	void Sort(LL* L, LLN* B); //makes sure list is sorted, if not, sorts the next node to be sorted
	void SortThis(LL* L, LLN* B); //sorts this into the right place in the list
	bool Getsorted(); //returns true if the node is in the right spot, false if it is not
	void Setnext(LLN* n); //setting next to n
	LLN* Getnext(); //getting next
	string Getword(); //getting word
	void Changesorted(); //changes the boolean value to true, call if the node is where it needs to be
	void Add(string s); //adding a node to the list
	void Print(); //printing the list
	void PrintSorted(); //print all the sorting booleans of all nodes (debugging)
};

#endif
