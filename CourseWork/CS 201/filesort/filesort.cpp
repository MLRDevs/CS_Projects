// Alex Miller
// take lines from file and sort them

#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
using namespace std;

bool CheckSort(double* arr, int n) { // return true if the list is already sorted
    for (int i=0; i < n-2; i++) {
        if (arr[i+1] < arr[i]) {
            return false;
        }
    }
    return true;
}

void PrintList(double* arr, int n) { // printing the list
    for (int i=0; i < n; i++) {
        cout << arr[i] << endl;
    }
}

double* SortList(double* arr, int n) { // sorts the list
    for (int i=0; i < n-1; i++) {
        for (int j=i+1; j < n; j++) {
            if (arr[j] < arr[i]) {
                double temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }
    return arr;
}

double Mean(double* arr, int n) { // return the mean of the list
    int ct = 0;
    for (int i=0; i < n; i++) {
        ct += arr[i];
    }
    ct /= n;
    return ct;
}
double Mode(double* arr, int n) { // return the mode of the list
    int* counts = new int[n];
    for (int i=0; i < n; i++) { // new array for counting the amount of times a number shows up
        counts[i] = 0;
    }

    double temp = arr[0]; // temp var to compare if the number we are on is the same
    int ct = 0; // counter to count the amount of the same numbers in the array
    double mode = 0; // mode of the array
    int t = 0; // index of counts array
    for (int i=0; i < n-1; i++) { // go through arr and count up how many there are of the same number
        if (temp == arr[i]) {
            ct++;
        }
        else { // if a new number is found
            temp = arr[i];
            counts[t] = ct;
            if (counts[t] > counts[t-1]) { // if it is the highest amount so far, make it the mode
                mode = arr[i-1];
            }
            t++;
            ct = 1;
        }
    }
    
    delete[] counts;
    return mode;
}

int main(int argc, char** argv) { // get lines from file, sort it and print it

    ifstream in("input.txt");
    if (in.fail()) {
        cout << "Error with file";
        exit(1);
    }

    double t;
    int n = 0;
    while(!in.eof()) { // count the amount of lines in the file
        in >> t;
        if (t >= 0) {
            n++;
        }
    }
    in.seekg(0); // go back to the start of the file
    double* arr = new double[n]; // declare array
    int count = 0;
    double temp;
    while (!in.eof()) { // put each item into the array
        in >> temp;
        if (temp >= 0) { // no negatives
            arr[count] = temp;
            count++;
        }
    }

    if (CheckSort(arr, n)) { // if the list is already sorted
        cout << "List is already sorted: " << endl;
        PrintList(arr, n);
    }
    else { // if the list is not sorted
        cout << "The list was not sorted" << endl;
        cout << "Sorted List: " << endl;
        arr = SortList(arr, n);
        PrintList(arr, n);
    }

    cout << endl;
    cout << "Min: " << arr[0] << endl;
    cout << "Max: " << arr[n-1] << endl;
    cout << "Mean: " << Mean(arr, n) << endl;
    if (n%2 == 0) { // even number array
        cout << "Median: " << arr[n/2-1] << endl;
    }
    else { // odd number array
        cout << "Median: " << arr[n/2] << endl;
    }
    cout << "Mode: " << Mode(arr, n) << endl;
    
    delete[] arr;
    return 0;
}