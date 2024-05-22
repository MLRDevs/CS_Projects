// Alex Miller
// Person class
 #ifndef _PERSON_
 #define _PERSON_

 #include <iostream>
 #include <cstdlib>
 #include <string>
 using namespace std;

 class Person {

    private:
        string name;
        int age;
    public:
        Person(string n, int a);
        friend std::ostream& operator<< (std::ostream& stream, Person &p);
 };

 #endif