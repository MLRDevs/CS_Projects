// Alex Miller
// Stack class

#ifndef _PERSONSTACK_
#define _PERSONSTACK_

#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class Person;
class Stack {

    private:
        Person* data[100];
        Person* pos;
    public:
        Stack();
        ~Stack();
        void Push(Person* newHuman);
        void Pop();
        bool IsEmpty();
        bool IsFull();
        inline friend std::ostream& operator<< (std::ostream& stream, Stack &s);
};

#endif