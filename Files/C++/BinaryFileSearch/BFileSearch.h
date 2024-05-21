//Alex Miller
//takes in a file and searches for the specific record
#ifndef _BFILESEARCH_
#define _BFILESEARCH_

#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main(int argc, char** argv); //asks user for a file and what record to search in the file
void Search(int n, int wct, string record, fstream& in); //searching the file for the specific record the user inputs

#endif
