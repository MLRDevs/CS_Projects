//Alex Miller
//all the methods that deals with the deck of cards themselves
#ifndef _DECK_
#define _DECK_

#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

class Card;
class Deck { //holds the methods for the entire deck of cards

	private: 
		Card** mycards; //holds all the cards
		int DeckSize; //size of the deck

	public: 
		Deck(int n, int arr[]); //creates the deck
		~Deck(); //deallocates
		void Shuffle(int n); //shuffle the deck
		void print(int r); //prints the name of the cards
		int getvalue(int r); //gets the value of the card
		int getsuit(int r); //gets the suit of the card
		int getrank(int r); //gets the rank of the card
		void PokerHand(int arr[]); //figures out what the hand is and prints it
};


#endif 
