//Alex Miller
//takes in a value to square root and a value to how many decimal places to square root, prints that value
#ifndef _LONGSQUAREROOTS_
#define _LONGSQUAREROOTS_

#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main(int argc, char** argv); //main method
void SquareRoot(string sqrt, string dec); //square roots the given number to the specified decimal places
void Trim(string& sqrt); //trims the string to get rid of the first char
string Add(string a, string b); //adds two strings together and returns sum
string Multiply(string a, string b); //multiplies the two strings together and returns the product
string Subtract(string a, string b); //subtracts the two strings and returns the difference
string AddZeros(string sqrt, string dec); //adding the zeros before taking the square root for the decimal places
string Cmp(string a, string b); //compares the two strings, returns the biggest one
void Answer(string ans, string dec, string sqrt, string oldsqrt); //puts the decimal place in the right spot and prints the answer

#endif
