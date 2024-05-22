// Alex Miller
#include <iostream>
using namespace std;

class Dollars
{
  public:
	int dol;
	int cents;

	Dollars(int i)
	{
		dol = i;
		cents = 0;
	}

	Dollars(double f)
	{
		dol = (int)f;
		cents = ((int)(f*100))-dol*100;
	}
    void add(int d, int c) {
        dol += d;
        cents += c;
        CheckCents();
    }
    void CheckCents() {
        while (cents >= 100) {
            cents -= 100;
            dol++;
        }
    }
    void multiply(int m) {
        dol *= m;
        cents *= m;
        CheckCents();

    }
    void combine(Dollars d) {
        dol += d.dol;
        cents += d.cents;
        CheckCents();
    }
    friend std::ostream& operator<< (std::ostream& stream, Dollars &d) {
        stream << "$" << d.dol << "." << d.cents << endl;
        return stream;
    }

	//
	// The only changes you can make to the program are here

};


int main()
{
	// This code doesn't work.  Change the class 'Dollars'
	// to make this code work.
	// Don't change this code; change the Dollar class above!

	Dollars d(1.9);
	cout << "Should be $1.90: " << d.dol << "." << d.cents << endl;

	d.add(2,80);
	cout << "Should be $4.70: " << d.dol << "." << d.cents << endl;

	d.multiply(3);
	cout << "Should be $14.10: " << d.dol << "." << d.cents << endl;

	cout << "And I can print it using cout! " << d << endl;

	Dollars wallet(1);
	Dollars pocket(2);
	wallet.combine(pocket);
	cout << "Should be $3.00: " << wallet.dol << "." << wallet.cents << endl;
}