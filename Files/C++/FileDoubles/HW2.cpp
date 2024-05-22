// Alex Miller
// Sorting doubles in a file and printing min, max, median, and mean

#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include "HW2.h"
using namespace std;

int main(int argc, char** argv) { // main method

    ifstream in("Input.txt");
    if (in.fail()) { // if the file fails
        cout << "Error with file";
        exit(1);
    }
    int n = 0; // array size
    double tempn = 0; // temp number
    while (!in.eof()) { // getting the number of lines, only ints higher than 0
        in >> tempn;
        if (tempn >= 0) { // if the int is higher than 0
            n++;
        }
    }

    in.seekg(0); // going back to the start of the file

    double* arr = new double[n]; // initialize array
    double t = 0; // temp variable
    int count = 0; // keep track of where we are in the array
    while (!in.eof()) { // put ints in array
        in >> t;
        if (t >= 0) { // if temp is higher than 0, add to array
            arr[count] = t;
            count++;
        }
    }

    for (int i=0; i < n; i++) { // sort the array
        for (int j=i+1; j < n; j++) {
            if (arr[i] > arr[j]) { // if there is a swap needed
                double temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }

    double mean = 0;
    for (int i=0; i < n; i++) { // adding the ints together
        mean += arr[i];
    }
    mean /= n; // getting the mean

    cout << "List: "  << n  << " items in array" << endl;
    cout << endl;
    for (int i=0; i < n; i++) { // printing the whole list
        cout << arr[i] << endl;
    }
    cout << endl;

    // printing the min, max, median, and mean
    cout << "min: " << arr[0] << endl;
    cout << "max: " << arr[n-1] << endl;
    cout << "median: " << arr[(n/2)-1] << endl;
    cout << "mean: " << mean << endl;

    delete[] arr; // deallocating memory
    return 0;
}