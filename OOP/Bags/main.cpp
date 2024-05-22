#include <iostream>
#include <string>
#include "MyBag.cpp"
#include "YourBag.cpp"
using namespace std;

const int maxItem = 100;

void insertRandomData(MyBag &b1, YourBag &b2)
{
  int size = rand() % 1000 + 5;
  for(int i = 0; i < size; i++)
  {
    int command = rand() % 100;
    int item = rand() % maxItem;
    if (command < 50)
    {
      //cout << "Added " << item << endl;
      b1.add(item);
      b2.add(item);
    }
    else if (command < 99)
    {
      //cout << "Deleted " << item << endl;
      b1.sub(item);
      b2.sub(item);
    }
    else
    {
      //cout << "Clear!" << endl;
      b1.clear();
      b2.clear();
    }
  }
}

bool compare(MyBag mb, YourBag yb)
{
  bool ans = true;
  for(int i = 0; i < maxItem; i++)
  {
    if (mb.count(i) != yb.countItems(i))
    {
      cout << "Error item " << i << ": I say " << mb.count(i) << ".  You say " << yb.countItems(i) << endl;
      ans = false;
    }
  }
  return ans;
}

int main()
{  
  MyBag myBag(maxItem);
  YourBag yourBag;
  for(int i = 0; i < 100; i++)
  {
    //cout << "----------New Test--------" << endl;
    insertRandomData(myBag, yourBag);
    bool good = compare(myBag, yourBag);
    if (!good)
    {
	    cout << "Mybag: " << endl << myBag << endl;
	    cout << "Yourbag: " << endl << yourBag << endl;
        break;
    }
  }
  cout << myBag << endl;
  cout << yourBag << endl;
}