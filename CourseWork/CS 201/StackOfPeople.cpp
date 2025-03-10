// Alex Miller
// Stack of People

#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include <assert.h>
using namespace std;

class Person { // person class 

    private:
        string name;
        int age;
    public:
        Person(string n, int a) { // constructor
            name = n;
            age = a;
        }
        friend std::ostream& operator<< (std::ostream& stream, Person &p) { // print method
            stream << p.name << " " << p.age << endl;
            return stream;
        }
};
class Stack { // stack class

    private:
        Person* data[100];
        int count;
        int countminus;
        Person* temp;
        Person* end;
    public:
        Stack() { // constructor
            count = 0;
            end = data[99];
        }
        void Push(Person* newHuman) { // put a pointer on the top of the stack
            if (IsFull()) {
                cout << "The stack is already full, cannot add anymore" << endl;
            }
            else {
                data[count] = newHuman;
                count++;
                countminus = count - 1;
            }
        }
        Person* Pop() { // take the top pointer off the stack
            if (IsEmpty()) {
                cout << "Stack is empty, cannot pop" << endl;
                return nullptr;
            }
            else {
                temp = data[count - 1];
                data[count - 1] = nullptr; // delete the pointer in the certain array index
                count--;
                countminus = count - 1;
                return temp;
            }
            return nullptr;
        }
        bool IsEmpty() { // check if the stack is empty
            if (count == 0) {
                return true;
            }
            return false;
        }
        bool IsFull() { // check if the stack is full
            if (count == 99) {
                return true;
            }
            return false;
        }
        friend std::ostream& operator<< (std::ostream& stream, Stack &s) { // print method
            if (s.IsEmpty()) { // check if it is empty
                stream << "The stack is empty" << endl;
            }
            else {
                while (s.countminus >= 0) { // start at top of stack and print down
                    stream << *s.data[s.countminus] << endl;
                    s.countminus--;
                }
            }
            return stream;
        }
};
int main(int argc, char** argv) { // take commands from a file and do the commands from the file to the stack

    Stack stack;
    ifstream in("Input.txt");
    if (in.fail()) {
        cout << "File error" << endl;
        exit(1);
    }
    while(!in.eof()) { // take each line in the file and do the command
        string s;
        getline(in, s);
        if (s[0] == '+') { // push a person to the stack
            string name;
            for (int i=2; i < s.length(); i++) { // get the name of the person
                if (s[i] > '9') {
                    name += s[i];
                }
            }
            string agestring;
            for (int i=name.length()+3; i < s.length(); i++) { // get the age of the person
                agestring += s[i];
            }
            int age = stoi(agestring); // change the string to an int, used in another C++ class before
            Person* newHuman = new Person(name, age);
            stack.Push(newHuman); // push the person onto the stack
            if (!stack.IsFull()) {
                cout << "Pushed: " << *newHuman << endl;
            }
        }
        else if (s[0] == '-') { // pop a person off of the stack
            Person* p = stack.Pop(); // pop the person off of the stack
            if (!stack.IsEmpty()) {
                cout << "Popped: " << *p << endl;
            }
            delete p;
        }
        else {
            cout << "Print Stack: " << endl;
            cout << stack << endl;
        }
    }
    
    return 0;
}