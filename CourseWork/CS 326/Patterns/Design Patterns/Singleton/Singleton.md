# Singleton

*Forces*: When creating an object, such as a database, it can be confusing when multiple of one object is being created and used.

*Solution*: The singleton pattern allows us to be able to create one instance of an object and only one instance of that object.

### The following example will use C++
```
#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class Singleton {
    private:
        static Singleton* Iptr; // the only pointer pointing to the object
        string name; // data the object holds

        Singleton() { // constructor

        }
    public:
        static Singleton* getInstance() { // getting the instance of the object
            if (Iptr == NULL) { // if there is no instance, create one
                Iptr = new Singleton();
                return Iptr;
            }
            else { // if there is an instance, return the instance
                return Iptr;
            }
        }

        // methods that you can add to manipulate the data 
        void setName(string n) {
            name = n
        }
        void print() {
            cout << name << endl;
        }
};
Singleton* Singleton::Iptr = NULL; // initializing the pointer to null

int main() { // main method
    Singleton* a = Singleton::getInstance(); // creating a singleton

    a->setName("Alex"); // assigning the name to "Alex"
    a->print();

    Singleton* b = Singleton::getInstance(); // creating another singleton
    b->print();

    cout << "Memory location of a: " << a << endl;
    cout << "Memory location of b: " << b << endl;

    return 0;
}
```
### Output:
```
Alex
Alex
Memory location of a: 013A82F8
Memory location of b: 013A82F8
```

***

<br>

### Breakdown:
The Singleton class is really dependant on it's private members
```
static Singleton* Iptr;
```
this creates the pointer that we will use to point to the instance of the object. This is declared private along with the Constructor so that another copy of a Singleton class cannot be created outside of the class.

<br>

```
static Singleton* getInstance() {
    if (Iptr == NULL) {
        Iptr = new Singleton();
        return Iptr;
    }
    else {
        return Iptr;
    }
}
```
these lines are what drives the pattern. If there is a pointer to a singleton object it returns the pointer, if there is no pointer pointing to a singleton object, it creates the singleton object and returns a pointer pointing to it. This way, there is only one singleton object that is being created regardless of how many times this method is invoked. Since the constructor for the singleton object is private, this is the only way to access that constructor.

<br>


```
void setName(string n) {
    name = n;
}
void print() {
    cout << name << endl;
}
```
these are used to show that you can still create methods and access them like any other object. It's just the creation of the object that only happens once

<br>

```
Singleton* a = Singleton::getInstance();

a->setName("Alex")
a->print();

Singleton* b = Singleton::getInstance();
b->print();
```
In this example we create two Singleton pointers, a and b. We use the public method ```setName(string n)``` to set the name member of the singleton object. after calling ```print()``` it prints the name of the object. We only use ```setName(string n)``` on pointer a. When calling ```getInstance()``` and assigning it to pointer b, it gets the same pointer so a and b are pointing at the same object. That's why, even though we dont set the name for pointer b, we can call ```print()``` on b and print the same name as a.

<br>

```
cout << "Memory location of a: << a << endl;
cout << "Memory location of b: << b << endl;
```
This just shows that they are indeed the same object. Both pointers point to the same memory location where the object is.

<br>

*Following Pattern*

[Observer](/ObserverPattern.md)


