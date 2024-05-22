# Template Method

*Forces*: You want to use the same pieces of code, but with slight differences

*Solution*: The Template Pattern allows us to use a template of a piece of code, and change what we need to do

### The following example will use C++
```
#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class Sport { // Template method
    private: // methods that are specific to each sport
        virtual void PrintSport() = 0;
        virtual void PrintPlayers() = 0;
    public: // methods that are used by everything that inherits the template
        void Play() {
            Template();
            PrintSport();
            PrintPlayers();
        }
        void Template() {
            cout << "This is a sport." << endl;
        }
};
class Hockey: public Sport { // Hockey class that inherits Sport
    private: // private data specific to Hockey
        int players = 6;
        string sport = "Hockey";
    public: // methods to override
        void PrintSport() {
            cout << sport << endl;
        }
        void PrintPlayers() {
            cout << sport << " has " << players << " players." << endl; 
        }
};
class Basketball: public Sport { // Basketball class that inherits Sport
    private: // private data specific to Basketball
        int players = 5;
        string sport = "Basketball";
    public: // methods to override
        void PrintSport() {
            cout << sport << endl;
        }
        void PrintPlayers() {
            cout << sport << " has " << players << " players." << endl; 
        }
};

int main() { // main method
    Hockey hockey; // create Hockey
    hockey.Play(); // do the template method

    cout << endl;

    Basketball basketball; // create Basketball
    basketball.Play(); // do the template method
}
```
### Output:
```
This is a sport.
Hockey
Hockey has 6 players.

This is a sport.
Basketball
Basketball has 5 players.
```

***

<br>

### Breakdown
```
private:
    virtual void PrintSport() = 0;
    virtual void PrintPlayers() = 0;
```
These are the methods inside of the template class that are going to change from one object to another. They are virtual methods so they can be inherited and change

<br>

```
public:
    void Play() {
        Template();
        PrintSport();
        PrintPlayers();
    }
    void Template() {
        cout << "This is a sport." << endl;
    }
```
When we create a Hockey or Basketball object, we call the ```Play()``` method. This method then calls the methods that the sports override. It also calls the method ```Template()``` to show that it calls the methods inside the class and the ones defined by the classes inheriting this one.

<br>

```
class Hockey: public Sport { // Hockey class that inherits Sport
    private: // private data specific to Hockey
        int players = 6;
        string sport = "Hockey";
    public: // methods to override
        void PrintSport() {
            cout << sport << endl;
        }
        void PrintPlayers() {
            cout << sport << " has " << players << " players." << endl; 
        }
};
```
This is the class for a Hockey object. This class has its own private data that differs from the Sport template class. The only difference is this class has the methods that the Sport class doesn't. these are the differences between the things you want to change and what the template class has. We also do the same thing with the Basketball class

<br>

```
int main() {
    Hockey hockey; // create Hockey
    hockey.Play(); // do the template method

    cout << endl;

    Basketball basketball; // create Basketball
    basketball.Play(); // do the template method
}
```
This is the main method working in action. We create each type of sport and use the ```Play()``` method in the Sport class. This method then uses each sports methods after using its own ```Template()``` method. that is how we get the following output.

```
This is a sport.
Hockey
Hockey has 6 players.

This is a sport.
Basketball
Basketball has 5 players.
```

<br>

*Preceding Pattern*

[Singleton](/Singleton.md)

*Following Pattern*

[Observer](/ObserverPattern.md)