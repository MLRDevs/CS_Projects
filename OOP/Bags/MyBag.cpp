#include <iostream>
using namespace std;

class MyBag
{
  int *data;
  int size;
 public:
  MyBag(int _size)
  {
    data = new int[_size];
    for(int i = 0; i < _size; i++)
      data[i] = 0;
    size = _size;
  }
  MyBag()
  {
    size = 100;
    data = new int[size];
    for(int i = 0; i < size; i++)
      data[i] = 0;
  }
  void add(int pos)
  {
    if (pos >= 0 && pos < size)
      data[pos]++;
    else
      cout << "Bad bad bad" << endl;
  }
  void sub(int pos)
  {
    if (pos >= 0 && pos < size)
    {
	if (data[pos] > 0)
      		data[pos]--;
    }
    else
      cout << "Bad bad bad" << endl;
  }
  int count(int item)
  {
    return data[item];
  }
  void clear()
  {
    for(int i = 0; i < size; i++)
        data[i] = 0;
  }
  friend std::ostream& operator<< (std::ostream& stream, const MyBag& bag)
  {
    stream << "[";
    for(int i = 0; i < bag.size; i++)
    {
      if (bag.data[i] > 0)
      {
        stream << i << ":" << bag.data[i] << ", ";
      }
    }
    stream << "]";
    return stream;
  }
};