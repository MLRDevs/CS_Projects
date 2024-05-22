// Alex Miller
// prints prime number up to a given value
#include <iostream>
#include <cstdlib>
#include <string>
#include "SOE.h"
using namespace std;


int GetNextT(bool* arr, int t, int arrlen) { // getting the next item in the array that is not crossed off (true)
    for (int i=t; i < arrlen; i++) { // loop through starting at the last t value until a new one is found
        if (arr[t] == true) {
            return t;
        }
    }
    return t; // return t if there is no next t
}

void Sieve (bool* arr, int t, int arrlen) { // crossing off the items in the list (making them false)
    while(t*t < arrlen) { // while we are not at the end of the list
        for (int i=t; i < arrlen-t; i += t) { // start at t and make every tth value false, ex: t=2, i=2, 4 is false, i += 2, and so on the so forth. stops at arrlen-t to avoid out of bounds
            arr[i+t] = false; // change the value to false
        }
        t = GetNextT(arr, t+1, arrlen); // get the next available number next
    }

}
void PrintPrimeNums(bool* arr, int n) { // printing the array, only the ones that are true starting at 2
    for (int i=2; i < n; i++) {
        if (arr[i] == true) {
            cout << i << endl;
        }
    }
}

int main(int argc, char** argv) { // main method

    int n;
    cout << "Enter the amount: "; // get the array length
    cin >> n;
    bool* arr = new bool[n];

    for (int i=0; i < n; i++) { // make every item true
        arr[i] = true;
    }

    Sieve(arr, 2, n); // do the crossing off
    cout << endl;
    PrintPrimeNums(arr, n); // print the result
    delete[] arr; // deallocating the memory

    return 0;
}