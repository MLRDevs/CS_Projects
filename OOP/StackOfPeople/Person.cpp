// Alex Miller
// Person methods

#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include "Person.h"
using namespace std;

Person::Person(string n, int a) {
    name = n;
    age = a;
}
std::ostream& operator<< (std::ostream& stream, Person &p) {
    stream << p.name << " " << p.age << endl;
    return stream;
}