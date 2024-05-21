//Alex Miller
//what each specific card has itself
#include <iostream>
#include <cstdlib>
#include <string>
#include "Card.h"
using namespace std;

Card::Card(int v) {
	value = v; //specific card (0-51)
	suit = value / 13; //suit of card
	rank = value % 13; //number on card

	switch (rank) { //adds the rank to the card name from the given rank
		case 0: name = "ACE"; break;
		case 1: name = "TWO"; break;
		case 2: name = "THREE"; break;
		case 3: name = "FOUR"; break;
		case 4: name = "FIVE"; break;
		case 5: name = "SIX"; break;
		case 6: name = "SEVEN"; break;
		case 7: name = "EIGHT"; break;
		case 8: name = "NINE"; break;
		case 9: name = "TEN"; break;
		case 10: name = "JACK"; break;
		case 11: name = "QUEEN"; break;
		case 12: name = "KING"; break;
	}
	name += " OF ";
	switch (suit) { //adds the suit to the card name from the given suit
		case 0: name += "CLUBS"; break;
		case 1: name += "DIAMONDS"; break;
		case 2: name += "HEARTS"; break;
		case 3: name += "SPADES"; break;
	}
}

Card::~Card() { //deallocates data
	
}

void Card::print() { //prints the name of the card
	cout << name << endl;
}

//gets the specific thing from each card (value,rank,suit,name)
int Card::getrank() {
	return rank;
}
int Card::getsuit() {
	return suit;
}
int Card::getvalue() {
	return value;
}
string Card::getname() {
	return name;
}