# Observer

*Forces*: When doing object design, it's a pain to manually change everything when one object changes.

*Solution*: The Observer Pattern lets you change the state of all dependencies of one object.

### The following example will use C++
```
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
        int amount; // data subject holds
        vector<Observer* observer> observers; // list of observers

    public:
        void AddObserver(Observer* observer) { // add an observer to list
            observers.push_back(observer);
        }
        void notify() {
            for (Observer* observer: observers) { // update each observer
                observer->update(amount);
            }
        }
        void setAmount(int n) { // set data and update observers
            amount = n;
            notify();
        }
};
class ConcreteObserver: public Observer { // concrete observer
    public:
        void update(int n) { // override update method for observer
            cout << "The amount is: " << n << endl;
        }
};
int main() { // main method
    Subject subject; // create the subject

    // create observer and add to subject's list, update the observer with the current data
    ConcreteObserver obs1;
    subject.AddObserver(&obs1);
    subject.setAmount(1);

    // create another observer and do the same, it also updates the first observer
    ConcreteObserver obs2;
    subject.AddObserver(&obs2);
    subject.setAmount(2);

    return 0;
}
```

<br>

### Output:
```
The amount is: 1
The amount is: 2
The amount is: 2
```

<br>

***

### Breakdown:
```
class Observer {
    public:
        virtual void update(int n) = 0;
};
```
This creates the Observer class and defines the method ```update(int n)``` as a virtual method, meaning it can be overrided. We need this method to be overrided in order to change what each observer does.

<br>

```
int amount;
vector<Observer*> observers;
```
This is what the Subject class knows. It knows the data that the observers know, along with a list of all the observers, which each observer doesn't know. We make these private since only the subject needs to know them.

<br>

```
void AddObserver(Observer* observer) {
    observers.push_back(observer);
}
void notify() {
    for (Observer* observer: observers) {
        observer->update(amount);
    }
}
void setAmount(int n) {
    amount = n;
    notify();
};
```
The ```AddObserver(Observer* observer)``` method adds an observer to the list of observers. The ```notify()``` method goes through each observers and lets them know the updated information. The ```setAmount(int n)``` method sets the information to the new information and then tells all the observers the new information.

<br>

```
class ConcreteObserver: public Observer {
    public:
        void update(int n) {
            cout << "The amount is: << n << endl;
        }
};
```
This is why we needed the ```update(int n)``` method in the Observer class to be a virtual method. Here, we are overriding what that method does since now we have new information from the Subject class. This class inherits the ```update(int n)``` method in order to override it. This method gets called everytime the Subject class gets new information with the ```notify()``` method.

<br>

```
int main() {
    Subject subject;

    ConcreteObserver obs1;
    subject.AddObserver(&obs1);
    subject.setAmount(1);

    ConcreteObserver obs2;
    subject.AddObserver(&obs2);
    subject.setAmount(2);

    return 0;
}
```
Here is where we get to test it all in action. First we create the Subject and then create the first ConcreteObserver. We add the observer to the Subject's list and update the observer to an amount of 1, which also prints it out. We then make a second ConcreteObserver, add it to the list, and set the amount to 2. Since setting the amount changes every observer, the first observer also gets a new amount, thus also prints it out. This is why we get the amount being 2 twice, each observer prints the current amount.

<br>

```
The amount is: 1
The amount is: 2
The amount is: 2
```

<br>

*Preceding Pattern*

[Singleton](/Singleton.md)

*Following Pattern*

[Model View Controller](/MVC.md)