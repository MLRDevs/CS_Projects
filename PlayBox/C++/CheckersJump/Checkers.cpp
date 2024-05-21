//Alex Miller
//user enters a checker board and enters a specific coordinate, user is then told if the checker at that specific square can make a valid jump or not
#include <iostream>
#include <cstdlib>
#include <string>
#include "Checkers.h"
using namespace std;

int main(int argc, char** argv) {
	//asking user for rows and columns
	cout << "How many rows? ";
	int r;
	cin >> r;
	cout << "How many columns? ";
	int c;
	cin >> c;
	cout << endl;
	cout << "Enter board below: " << endl;

	//taking row inputs and assigning it to a string
	string e;
	string s;
	for (int i = 0; i < r + 1; i++) {
		getline(cin, s);
		e += s;
	}

	//creating the board
	char** Board;
	Board = new char* [r];
	for (int i = 0; i < r; i++) {
		Board[i] = new char[c];
	}

	//assigning the board values
	int k = 0;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			Board[i][j] = e.at(k);
			k++;
		}
	}

	//asking the user for the specific coordinate to be checked
	cout << endl;
	cout << "Enter row to be checked: ";
	int rc;
	cin >> rc;
	cout << "Enter column to be checked: ";
	int cc;
	cin >> cc;

	//checking the coordinate and printing the result
	if (CheckJump(Board, c, r, rc, cc) == true) {
		cout << "the checker at this square can make a valid jump";
	}
	else {
		cout << "the checker at this square cannot make a valid jump";
	}

	//deallocating memory for Board
	for (int i = 0; i < r; i++) {
		delete[] Board[i];
	}
	delete[] Board;

	return 0;
}
bool InBounds(int rlen, int clen, int rc, int cc) { //checks if the coordinate is in bounds of the board
	if (rc < 0) return false;
	if (rc > clen) return false;
	if (cc < 0) return false;
	if (cc > rlen) return false;
	return true;
}
bool CheckJump(char** Board, int rlen, int clen, int rc, int cc) { //checks if the checker at the given square can make a valid jump or not 

	//checks every diagonal jumping oppertunity, long way to do it, could possibly be done by loops

	cout << endl;
	int nr; //new row coord
	int nc; //new column coord
	
	//for NorthWest jump
	if (InBounds(rlen, clen, rc, cc)) { //checks if the coordinate is in bounds of the board
		nr = rc - 1; //new row coord
		nc = cc - 1; //new column coord
		if (InBounds(rlen, clen, nr, nc)) { //checks if the new coordinate is in bounds of the board
			if (Board[nr][nc] != Board[rc][cc] && Board[nr][nc] != ' ') { //checks if the new coordinate is not a space and different from user coordinate
				nr -= 1; //new row coord
				nc -= 1; //new column coord
				if (Board[nr][nc] == ' ' && InBounds(rlen,clen,nr,nc)) { //checks if the new coordinate is a space and in bounds of the baord 
					return true; 
				}
			}
		}

	}
	//for SouthEast jump
	if (InBounds(rlen, clen, rc, cc)) { //checks if the coordinate is in bounds of the board
		nr = rc + 1; //new row coord
		nc = cc + 1; //new column coord
		if (InBounds(rlen, clen, nr, nc)) { //checks if the new coordinate is in bounds of the board
			if (Board[nr][nc] != Board[rc][cc] && Board[nr][nc] != ' ') { //checks if the new coordinate is not a space and different from user coordinate
				nr += 1; //new row coord
				nc += 1; //new column coord
				if (Board[nr][nc] == ' ' && InBounds(rlen, clen, nr, nc)) { //checks if the new coordinate is a space and in bounds of the baord 
					return true;
				}
			}
		}

	}
	//for SouthWest jump
	if (InBounds(rlen, clen, rc, cc)) { //checks if the coordinate is in bounds of the board
		nr = rc + 1; //new row coord
		nc = cc - 1; //new column coord
		if (InBounds(rlen, clen, nr, nc)) { //checks if the new coordinate is in bounds of the board
			if (Board[nr][nc] != Board[rc][cc] && Board[nr][nc] != ' ') { //checks if the new coordinate is not a space and different from user coordinate
				nr += 1; //new row coord
				nc -= 1; //new column coord
				if (Board[nr][nc] == ' ' && InBounds(rlen, clen, nr, nc)) { //checks if the new coordinate is a space and in bounds of the baord 
					return true;
				}
			}
		}

	}
	//for NorthEast jump
	if (InBounds(rlen, clen, rc, cc)) { //checks if the coordinate is in bounds of the board
		nr = rc - 1; //new row coord
		nc = cc + 1; //new column coord
		if (InBounds(rlen, clen, nr, nc)) { //checks if the new coordinate is in bounds of the board
			if (Board[nr][nc] != Board[rc][cc] && Board[nr][nc] != ' ') { //checks if the new coordinate is not a space and different from user coordinate
				nr -= 1; //new row coord
				nc += 1; //new column coord
				if (Board[nr][nc] == ' ' && InBounds(rlen, clen, nr, nc)) { //checks if the new coordinate is a space and in bounds of the baord 
					return true;
				}
			}
		}

	}
	return false;
}