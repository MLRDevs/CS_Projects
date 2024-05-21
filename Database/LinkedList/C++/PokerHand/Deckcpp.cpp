//Alex Miller
//creates the deck and shuffles the cards in the deck to then print out
#include <iostream>
#include <cstdlib>
#include <string>
#include "Deck.h"
#include "Card.h"
using namespace std;

Deck::Deck(int n, int arr[]) { //creates the deck

	mycards = new Card * [n];
	for (int i = 0; i < n; i++) {
		Card* c = new Card(arr[i]);
		mycards[i] = c;
	}
	Shuffle(n); 
	for (int i = 0; i < 5; i++) {
		print(i);
		cout << endl;
	}
	cout << endl;
	DeckSize = n; //assigns the amount of cards to DeckSize
}

Deck::~Deck() { //deallocates data
	for (int i = 0; i < DeckSize; i++) {
		delete mycards[i];
	}
	delete [] mycards;
}

void Deck::Shuffle(int n) { //shuffles all the cards together in the deck so they are in a random order

	for (int i = 0; i < n; i++) {
		int r = rand() % (i + 1);
		Card* t = mycards[i];
		mycards[i] = mycards[r];
		mycards[r] = t;
	}
}
void Deck::print(int r) { //prints the name of the card with the specific value
	cout << mycards[r]->getname(); 
}

//get methods for getting the specific item in the card
int Deck::getsuit(int r) {
	return mycards[r]->getsuit();
}
int Deck::getrank(int r) {
	return mycards[r]->getrank();
}
int Deck::getvalue(int r) {
	return mycards[r]->getvalue();
}

void Deck::PokerHand(int arr[]) { //determines what poker hand you have and prints it

	//ints for each card rank
	int ace = 0;
	int two = 0;
	int three = 0;
	int four = 0;
	int five = 0;
	int six = 0;
	int seven = 0;
	int eight = 0;
	int nine = 0;
	int ten = 0;
	int jack = 0;
	int queen = 0;
	int king = 0;

	int spades = 0;
	int hearts = 0;
	int diamonds = 0;
	int clubs = 0;

	bool Flush = false;

	int zero = 0;
	int onescards = 0;
	int twoscards = 0;
	int threescards = 0;
	int fourscards = 0;

	for (int i = 0; i < 5; i++) { //coutning each time a certain rank shows up in the five cards
		if (mycards[i]->getrank() == 0) {
			ace++;
		}
		else if (mycards[i]->getrank() == 1) {
			two++;
		}
		else if (mycards[i]->getrank() == 2) {
			three++;
		}
		else if (mycards[i]->getrank() == 3) {
			four++;
		}
		else if (mycards[i]->getrank() == 4) {
			five++;
		}
		else if (mycards[i]->getrank() == 5) {
			six++;
		}
		else if (mycards[i]->getrank() == 6) {
			seven++;
		}
		else if (mycards[i]->getrank() == 7) {
			eight++;
		}
		else if (mycards[i]->getrank() == 8) {
			nine++;
		}
		else if (mycards[i]->getrank() == 9) {
			ten++;
		}
		else if (mycards[i]->getrank() == 10) {
			jack++;
		}
		else if (mycards[i]->getrank() == 11) {
			queen++;
		}
		else if (mycards[i]->getrank() == 12) {
			king++;
		}
	}
	for (int i = 0; i < 5; i++) { //counting each suit 
		if (mycards[i]->getsuit() == 0) {
			clubs++;
		}
		else if (mycards[i]->getsuit() == 1) {
			diamonds++;
		}
		else if (mycards[i]->getsuit() == 2) {
			hearts++;
		}
		else if (mycards[i]->getsuit() == 3) {
			spades++;
		}
	}
	if (clubs == 5 || diamonds == 5 || hearts == 5 || spades == 5) { //if there are five cards of the same suit then there is a flush
		Flush = true;
	}

	int fivecardsranks[13] = { ace,two,three,four,five,six,seven,eight,nine,ten,jack,queen,king }; //putting all the rank counters into an array
	for (int i = 0; i < 13; i++) { //counting each time a rank counter is inside the array
		if (fivecardsranks[i] == 0) {
			zero++;
		}
		else if (fivecardsranks[i] == 1) {
			onescards++;
		}
		else if (fivecardsranks[i] == 2) {
			twoscards++;
		}
		else if (fivecardsranks[i] == 3) {
			threescards++;
		}
		else {
			fourscards++;
		}
	}

	//if statements for each possible hand
	if (onescards == 1 && twoscards == 0 && threescards == 0 && fourscards == 1) { //four of a kind
		cout << "you have a Four of a Kind" << endl;
	}
	else if (onescards == 0 && twoscards == 1 && threescards == 1 && fourscards == 0) { //full house
		cout << "you have a Full House" << endl;
	}
	else if (onescards == 2 && twoscards == 0 && threescards == 1 && fourscards == 0) { //three of a kind
		cout << "you have a Three of a Kind" << endl;
	}
	else if (onescards == 1 && twoscards == 2 && threescards == 0 && fourscards == 0) { //two pair
		cout << "you have a Two Pair" << endl;
	}
	else if (onescards == 3 && twoscards == 1 && threescards == 0 && fourscards == 0) { //pair
		cout << "you have a Pair" << endl;
	}
	else if (onescards == 5) { //everything else (royal flush, flush, straight, straight flush, highs)

		//checks for an Ace,King,Queen,Jack,Ten normal straight and royal flush
		if (fivecardsranks[0] == fivecardsranks[9] &&
			fivecardsranks[0] == fivecardsranks[10] &&
			fivecardsranks[0] == fivecardsranks[11] &&
			fivecardsranks[0] == fivecardsranks[12] &&
			fivecardsranks[0] == 1) {

			if (Flush == true) {

				cout << "you have a Royal Flush" << endl; exit(1); //exits stopping the program when the correct outcome is found, otherwise you will get more than one outcome, ie: royal flush and then flush
			}
			else {
				cout << "you have a Straight" << endl; exit(1);
			}

		}
		//checking for normal straight and straight flush
		for (int i = 0; i < 10; i++) {
			if (fivecardsranks[i] == fivecardsranks[i + 1] &&
				fivecardsranks[i] == fivecardsranks[i + 2] &&
				fivecardsranks[i] == fivecardsranks[i + 3] &&
				fivecardsranks[i] == fivecardsranks[i + 4] &&
				fivecardsranks[i] == 1) {

				if (Flush == true) {

					cout << "you have a Straight Flush" << endl; exit(1);
				}
				else {
					cout << "you have a Straight" << endl; exit(1);
				}
			}
		}

		//checks for normal flush
		for (int i = 0; i < 10; i++) {
			if (Flush == true) {

				cout << "you have a Flush" << endl; exit(1);
			}
		}
		int high = mycards[0]->getrank(); //initialize the highest value to the first one in the array
		bool acehigh = false; //bool to see if ace is the highest card, won't work in the noraml for loop since the rank of ace is 0 and king is 12, ace > king
		for (int i = 0; i < 5; i++) { //for loop to go through the cards and see if there is an ace
			if (mycards[i]->getrank() == 0) {
				acehigh = true; //switching the bool to true if there is an ace, if there is an ace then there is no need to see a higher card than that
				high = mycards[i]->getrank();
			}
		}
		if (acehigh == false) { //if there is no ace in the array
			for (int i = 1; i < 5; i++) { //getting the largest ranked card in the array and setting it to the high value
				if (high < mycards[i]->getrank()) {
					high = mycards[i]->getrank();

				}
			}
		}

		//printing the respective high value card of the highest values card in the five cards
		if (high == 0) {
			cout << "you have Ace high";
		}
		else if (high == 12) {
			cout << "you have King high";
		}
		else if (high == 11) {
			cout << "you have Queen high";
		}
		else if (high == 10) {
			cout << "you have Jack high";
		}
		else if (high == 9) {
			cout << "you have Ten high";
		}
		else if (high == 8) {
			cout << "you have Nine high";
		}
		else if (high == 7) {
			cout << "you have Eight high";
		}
		else if (high == 6) {
			cout << "you have Seven high";
		}
	}
	else {
		cout << "hit end"; //debug
	}
}