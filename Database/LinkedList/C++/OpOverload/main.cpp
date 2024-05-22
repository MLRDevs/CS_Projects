// https://www.geeksforgeeks.org/set-in-cpp-stl/

// Things to discuss
// How to l = l + 4
// How to l = 4 + l;
// How to l = l - 4;
// How to l = 4 - l;
// WHat the heck is l < 4
// Remember l might be null

// Due:  Friday before finals week


#include <iostream>
#include <set>
using namespace std;

class LinkedList {
    public:
        Node * head;
        LinkedList(Node * n) {
            head = n;
        }
        LinkedList() {
            head = nullptr;
        }
        void AddNode(int d) {
            if (!head) {
                head = new Node(d, nullptr);
            }
            else {
                head->AddNode(d);
            }
        }
        void DeleteNode(int d) {
            if (!head) {
                return;
            }
            else {
                head->DeleteNode(d);
            }
        }
        void Print() {
            if (head) {
                head->Print();
            }
            else {
                cout << "List is empty! " << endl;
            }
        }
        LinkedList &operator-(int d) {

        }
        LinkedList &operator+(int d) {
            LinkedList l;
            if (!head) {
                l.AddNode(d);
                return l;
            }
            l.head = head;
            l.AddNode(d);
            return l;

        }
        LinkedList &operator+(LinkedList l) {
            
        }
        bool &operator<(int d) {

        }
        friend ostream &operator<<(ostream &os, LinkedList &l) {
            l.Print();
        }
};
class Node {
    public:
        Node* next;
        int data;

        Node(int d, Node* n) {
            next = n;
            data = d;
        }
        void AddNode(int d) {
            if (!next) {
                next = new Node(d, nullptr);
            }
            else {
                next->AddNode(d);
            }
        }
        void DeleteNode(int d) {
            if (next) {
                if (next->data == d) {
                    if (next->next) {
                        next = next->next;
                    }
                    else {
                        next = nullptr;
                    }
                }
                else {
                    next->DeleteNode(d);
                }
            }
        }
        void Print() {
            cout << data << " ";
            if (next) {
                next->Print();
            }
        }
};

ostream &operator<<(ostream &os, set<int>&s)
{
   for (auto itr = s.begin(); itr != s.end(); itr++) {
        cout << *itr << " ";
    }
    return os;
}

void compare(set<int> &s1, LinkedList &l1)
{
    cout << "These should be the same" << endl;
    cout << s1 << endl;
    cout << l1 << endl;
}
int main()
{
    cout << "==========\n\n\n\n\n\n\n"  << endl;
    set<int> s;
    LinkedList l;
    s.insert(3);
    l = l + 3;
    compare(s, l);

    s.insert(13);
    //l = 13 + l;
    compare(s, l);


    s.insert(1); s.insert(2); s.insert(3); s.insert(4);
    l = l + 1 + 2 + 3 + 4;
    compare(s, l);


    s.erase(4);
    l = l - 4;
    compare(s, l);

    s.erase(1);
    l = l - 1;
    compare(s, l);

    s.erase(9999);
    LinkedList l2 = l - 9999;
    compare(s, l);

    if (l < 10)
	cout << "Good.  L has nothing greater than 10\n";
    else
	cout << "Bad answer\n";
    if (l < 1)
	cout << "Bad.  L does have something greater than 1\n";
    else
	cout << "Bad answer\n";
}