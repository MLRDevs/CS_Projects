//Alex Miller
//takes a number of cards in a deck from a user, askes for the value of each card, picks five at random in the deck and says what poker hand you have
#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include "Poker.h"
#include "Deck.h"
#include "Card.h"
using namespace std;

int main(int argc, char** argv) { //asks the user for the amount of cards and the cards themselves
	srand(time(NULL)); //random

	//getting deck amount 
	cout << "How many cards are there? ";
	int n;
	cin >> n;

	int arr[52];
	Card** cards = new Card * [5];
	int c;
	
	//asking for each card and entering it into the array
	for (int i = 0; i < n; i++) {
		cout << "Enter card " << i+1 << ": ";
		cin >> c;
		arr[i] = c;
	}
	cout << endl;

	Deck* d = new Deck(n, arr); //deck pointer to the deck

	d->PokerHand(arr);

	delete[] cards;
	delete d;
	return 0;
}
