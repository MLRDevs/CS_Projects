// Alex Miller
#include <iostream>
#include <string>
using namespace std;

  // Print the array
void printArray(int data[], int count)
{
  for(int i = 0; i < count; i++)
  {
    cout << data[i] << " ";
  }
  cout << endl;
}

void fillWithRandom(int data[], int size)
{
  srand(time(0));

  // Fill the array with random
  for(int i = 0; i < size; i++)
  {
    data[i] = rand() % 20 - 2;
  }

}
// return true if there is a negative int in the array
bool hasNegatives(int* data, int size) {
    for (int i=0; i < size; i++) {
        if (data[i] < 0) {
            return true;
        }
    }
    return false;
}
// copys data into data2 but backwards
void copyBackwards(int* data, int* data2, int size) {
    int temp = size-1;
    for (int i=0; i < size; i++) {
        data2[i] = data[temp];
        temp--;
    }
}

int main()
{
  const int size = 7;
  int data[size];
  fillWithRandom(data, size);
  cout << "Normal array: " << endl;
  printArray(data, size);

  // Write a method/function that takes  two parameters:
  // an integer array and an integer size.  The function
  // returns a bool that is true if the array contains any
  // negative numbers, and a false if there are zero negative
  // numbers.  For example, on the array {1,2,-3,4,5,-6} it
  // should return true and for { 1,2,3,4,5,6 } it should return false.
  cout << endl;
  bool ans = hasNegatives(data, size);
  if (ans == true) {
    cout << "Has a negtaive number" << endl;
  }
  else {
    cout << "Has zero negative numbers" << endl;
  }
    cout << endl;
  // Write a method/function that takes two arrays and a size.
  // When the method is done, data2 consists of data1 BACKWARDS.
  // If data = {1,2,3,4,5} then data2 should become {5,4,3,2,1}
  int data2[size];
  copyBackwards(data, data2, size);
  cout << "Normal array: " << endl;
  printArray(data, size);
  cout << endl;
  cout << "Backwards array: " << endl;
  printArray(data2, size);


 }