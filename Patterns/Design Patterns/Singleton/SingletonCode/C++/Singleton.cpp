#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class Singleton {

    private:
        static Singleton* instanceptr;
        string name;

        Singleton() {

        }

    public:

        static Singleton* getInstance() {
            if (instanceptr == NULL) {
                instanceptr = new Singleton();
                return instanceptr;
            }
            else {
                return instanceptr;
            }
        }
        void setvalues(string n) {
            name = n;
        }
        void print() {
            cout << name << endl;
        }
};

Singleton* Singleton::instanceptr = NULL;

int main() {
    Singleton* a = Singleton::getInstance();

    a->setvalues("Alex");
    a->print();

    Singleton* b = Singleton::getInstance();
    b->print();

    cout << "Memory location for a: " << a << endl;
    cout << "Memory location for b: " << b << endl;

    return 0;
}