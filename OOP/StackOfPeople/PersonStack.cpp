// Alex Miller
// Stack methods

#include <iostream>
#include <cstdlib>
#include <string>
#include "Person.h"
#include "PersonStack.h"
using namespace std;

Stack::Stack() {
    pos = data[0];
}
Stack::~Stack() {
    for (int i=0; i < 100; i++) {
        delete data[i];
    }
    delete[] data;
}
void Stack::Push(Person* newHuman) {
    *pos = *newHuman;
    cout << "HERE" << endl;
}
void Stack::Pop() {

}
bool Stack::IsEmpty() {
    if (pos == data[0]) {
        return true;
    }
    return false;
}
bool Stack::IsFull() {
    if (pos == data[99]) {
        return true;
    }
    return false;
}
std::ostream& operator<< (std::ostream& stream, Stack &s) {
    return stream;
}