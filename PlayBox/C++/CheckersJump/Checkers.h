//Alex Miller
#ifndef _CHECKERS_
#define _CHECKERS_

#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main(int argc, char** argv);
bool InBounds(int rlen, int clen, int rc, int cc);
bool CheckJump(char** Board, int rlen, int clen, int rc, int cc);

#endif