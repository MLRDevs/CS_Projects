// Alex Miller
// Using a stack to hold data on people
#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include "HW4.h"
//#include "PersonStack.h"
//#include "Person.h"
#include "PersonStack.cpp"
#include "Person.cpp"
using namespace std;

string getName(string cmd) { // gets the name of the person
    string name;
    for (int i=1; i < cmd.length()-1; i++) {
        if (cmd[i] > '9') {
            name += cmd[i];
        }
    }
    return name;
}
int getAge(string cmd, string name) { // gets the age of the person
    string agestring;
    for (int i=name.length()+1; i < cmd.length(); i++) { // get the age from the string
        agestring += cmd[i];
    }
    int age = stoi(agestring); // make it an integer (used this code before in previous C++ class)
    return age;

}
int main(int argc, char** argv) { // main method

    fstream in("Input.txt");
    if (in.fail()) { // input file failed
        cout << "Input file failed" << endl;
        exit(1);
    }

    int n = 0;
    string s;
    while(!in.eof()) { // find out how many lines
        in >> s;
        if (s == "+") {
            in >> s;
            in >> s;
        }
        n++;
    }
    in.seekg(0); // go back to beginning of file
    string* arr = new string[n]; // create array

    int count = 0;
    while(!in.eof()) { // enter lines from the file into the array
        in >> s;
        if (s == "+") { // in >> s --> stops at a space, so if there was "+ Alex 23", "in >> s" would return "+" only
            string t;
            in >> t;
            s += t;
            in >> t;
            s += t;
        }
        arr[count] = s;
        count++;
    }
    in.close();
    Stack* stack = new Stack();
    string name;
    int age;
    for (int i=0; i < n; i++) { // for loop that runs each command (i.e how many lines in the file)
        string command = arr[i];
        if (command[0] == '+') { // push
            name = getName(command);
            age = getAge(command, name);
            Person* newHuman = new Person(name, age);
            stack->Push(newHuman);
            cout << newHuman << endl;
        }
        else if (command[0] == '-') { // pop and print
            //stack->Pop();
        }
        else if (command[0] == '?') { // print stack
            //cout << stack << endl;
        }
        else {
            cout << "Error with command" << endl;
        }
    }
    //delete stack;
    delete[] arr;
    return 0;
}