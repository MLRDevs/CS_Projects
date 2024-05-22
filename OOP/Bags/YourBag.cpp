// Alex Miller
// HW 3 Objects

#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class YourBag { // bag class, an array containing ints with a size and a counter
    int* data;
    int size;
    int count = 0;
    // count = total in array + 1
    // size = total size of array
    // del -> swap the one being deleted with the last one and count--;
    public:
        YourBag(int size2) { // constructor
            data = new int[size2];
            size = size2;
        }
        YourBag() { // constructor
            size = 1000;
            data = new int[size];
        }
        void add(int item) { // adding an item to the array
            data[count] = item;
            count++;
        }
        void sub(int item) { // delete an item
            for (int i = 0; i < count; i++) {
                if (data[i] == item) {
                    data[i] = data[count-1];
                    count--;
                    return;
                }
            }
        }
        void clear() { // clear the array
            count = 0;
        }
        int countItems(int item) const{ // count how many of a certain item --> const is needed if friend method also uses const
            int c = 0;
            for (int i=0; i < count; i++) {
                if (data[i] == item) {
                    c++;
                }
            }
            return c;
        }
        friend std::ostream& operator<< (std::ostream& stream, const YourBag& yourBag) { // printing the bag itself
            stream << "[";
            for(int i = 0; i < yourBag.size; i++)
            {
                int c = yourBag.countItems(i); // assigning to int c so the method only needs to run once and not twice for the if and stream
                if (c > 0)
                {
                    stream << i << ":" << c << ", ";
                }
            }
            stream << "]";
            return stream;
        };

};