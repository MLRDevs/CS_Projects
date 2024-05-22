// Alex Miller
// code example for observer pattern

#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
using namespace std;

class Observer { // observer class
    public:
        virtual void update(int n) = 0; // virtual method to be overrided 
};

class Subject { // subject class
    private:
        int amount; // data the subject holds
        vector<Observer*> observers; // list of observers
        
    public:
        void AddObserver(Observer* observer) { // add an observer to the list
            observers.push_back(observer);
        }
        void notify() { // update all observers
            for (Observer* observer: observers) { // for every observer
                observer->update(amount);
            }
        }
        void setAmount(int n) { // set the amount
            amount = n;
            notify();
        }
};

class ConcreteObserver: public Observer { // concrete observer
    public:
        void update(int n) { // override the update method
            cout << "The amount is: " << n << endl;
        }
};

int main() { // main method

    Subject subject; // create the subject

    // create the first Derive object and add it to subject's list and notify it's observers
    ConcreteObserver obs1;
    subject.AddObserver(&obs1);
    subject.setAmount(1);

    // create the second Derive object and do the same thing
    ConcreteObserver obs2;
    subject.AddObserver(&obs2);
    subject.setAmount(2);

    return 0;
}