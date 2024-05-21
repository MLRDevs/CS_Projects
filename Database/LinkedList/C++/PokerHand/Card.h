//Alex Miller
//what each specific card has itself
#ifndef _CARD_
#define _CARD_

#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

class Card { //what each card has

private: //each card has these 
	int rank;
	int suit;
	int value;
	string name;

public:
	Card(int v); //creates the card
	~Card(); //deallocates
	void print(); //prints the name of the card
	int getrank(); //gets the rank of the card
	int getsuit(); //gets the suit of the card
	int getvalue(); //gets the value of the card
	string getname(); //gets the name of the card
};

#endif 
