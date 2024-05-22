// Alex Miller
// Quiz 1

#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
using namespace std;

int main(int argc, char** argv) {

    // 7 a's into a file
    ofstream out("output.txt");
    if (out.fail()) {
        cout << "Error with file";
        exit(1);
    }

    for (int i=0; i < 7; i++) {
        out << 'a';
    }

    // Wipes out a file
    ofstream out2("output2.txt");
    if (out2.fail()) {
        cout << "Error with file";
        exit(1);
    }

    ifstream in("Quiz1.cpp");
    if (in.fail()) {
        cout << "Error with file";
        exit(1);
    }

    // prints 12th line of source code
    string text;
    for (int i=0; !in.eof(); i++) {
        getline(in, text);
        if (i == 11) {
            cout << text << endl;
            exit(1);
        }
    }

    out.close();
    out2.close();
    in.close();
    
    return 0;
}