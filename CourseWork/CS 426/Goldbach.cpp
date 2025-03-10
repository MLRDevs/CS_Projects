// Alex Miller
// golbach conjecture with multiple threads and locking

#include <iostream>
#include <cstdlib>
#include <string>
#include <thread> // threads
#include <mutex> // locks
#include <math.h> // sqrt
using namespace std;

mutex l; // lock
int nxt = 6; // global next value to check
int minn = 3; // minimum number


bool isPrime(int n) { // check for primes (based on python code given)
    if (n == 1) return false; // base case
    if (n%2 == 0) return false; // base case
    else {
        for (int i=3; i < sqrt(n)+1; i+= 2) { // loop to check if not prime
            if (n%i == 0) return false;
        }
    }
    return true; // if prime
}
void checkPrimes(int num, int value, int mm) { // method to figure out the primes
    if (isPrime(value) && isPrime(num-value)) { // if they are both prime
        if (min(value,num-value) > mm) { // if its bigger than the minimum
            l.lock();
            minn = min(num-value,value); // change the value of minn
            l.unlock();
            cout << num << " " << min(num-value,value)<< " " << max(num-value,value) << endl; // print primes
            return;
        }
        else return; // return if the minn value is higher than the minimum golbach pair
    }
    checkPrimes(num,value+2,mm); // recursion to find the goldbach pair with lowest prime
}

void goldbach() { // lock the thread and find print if its a new minimum primes

    // setting the while loop
    int n = 0;
    int mynum;
    int mymin;
    int mm = 0;

    while (mm < 1000) { // loop a few times to get a lot of numbers

        // getting next number
        l.lock();
        mynum = nxt;
        nxt += 2;
        mymin = minn;
        l.unlock();

        // get the prime numbers
        checkPrimes(mynum, 3, mymin);

        /*
            checkPrimes() starts at 3 to check primes then moves up from there, I have
            tried starting at mymin and going up from there to be faster 
            but have hit many segmentation faults. 
        */

        // update mm to update while loop
        l.lock();
        mm = minn;
        l.unlock();
    }
}

int main() { // main method

    // get the threads
    int threads = 0;
    cout << "Enter the amount of threads: ";
    cin >> threads;
    cout << endl;

    thread* tarr = new thread[threads]; // thread array
    
    for (int i=0; i < threads; i++) { // adding a thread to the array and starting it
        tarr[i] = thread (goldbach);
    }
    for (int j=0; j < threads; j++) { // joining all the threads together
        tarr[j].join();
    }

    return 0;
}