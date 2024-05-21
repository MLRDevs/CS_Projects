//Alex Miller
//takes a number of cards in a deck from a user, askes for the value of each card, picks five at random in the deck and says
#ifndef _POKER_
#define _POKER_

#include <iostream>
#include <string>
#include <cstdlib>
#include "Deck.h" //include deck.h so I can pass the d pointer to the RandomCard method
using namespace std;

int main(int argc, char** argv); //asks the user for the amount of cards and the cards themselves
void RandomCard(Deck* d,Card* cards[]); //picks a random card the deck, before picking a new card, makes sure the card it picks hasn't been picked yet (no duplicates get printed)
void PokerHands(int arr[],Deck* d,Card* cards[]); //checks what poker hand you have and prints it

#endif 
