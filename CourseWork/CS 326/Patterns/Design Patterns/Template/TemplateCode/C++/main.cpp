// Alex Miller
// Template Pattern example

#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class Sport { // Template
    private:
        // methods to override per sport
        virtual void PrintSport() = 0;
        virtual void PrintPlayers() = 0;
    
    public:
        void Play() { // method used for sport, has methods in template and methods specific per sport
            Print();
            PrintSport();
            PrintPlayers();
        }
        void Print() { // method in template used to show these methods work for each sport
            cout << "This is a sport" << endl;
        }
};
class Hockey: public Sport { // Hockey class that inherits the Sport class
    private: // data for Hockey
        string sport = "Hockey";
        int players = 6;
    
    public: // override methods
        void PrintSport() {
            cout << sport << endl;
        }
        void PrintPlayers() {
            cout << sport << " has " << players << " players." << endl;
        }
};
class Basketball: public Sport { // Basketball class that inherits the Sports class
    private: // data for Basketball
        string sport = "Basketball";
        int players = 5;
    
    public: // override methods
        void PrintSport() {
            cout << sport << endl;
        }
        void PrintPlayers() {
            cout << sport << " has " << players << " players." << endl;
        }
};
int main() { // main method

    Hockey hockey; // create Hockey
    hockey.Play(); // use the methods

    cout << endl;

    Basketball basketball; // create Basketball
    basketball.Play(); // use the methods

    return 0;
}