// Alex Miller

/*
    added == operator, tests if the data given is in the list or not
    list is also sorted as nodes get added and everything is recursive
*/

#include <iostream>
#include <cstdlib>
#include <string>
#include <set>
using namespace std;

class Node { // Node class
    public:
        Node* next;
        int data;

        Node(int d, Node* n) { // Constructor
            next = n;
            data = d;
        }
        bool CheckData(int d) { // return true if the data is in the list already
            if (data == d) {
                return true;
            }
            if (next) {
                return next->CheckData(d);
            }
            return false;
        }
        void AddNode(int d) { // Add a node to the list
            if (!next) {
                next = new Node(d, nullptr);
            }
            else if (d > data && d < next->data) { // if the new node to add comes in between two nodes
                Node* temp = new Node(d,next);
                next = temp;
            }
            else { // if the new node to add comes after next
                next->AddNode(d);
            }
        }
        void DeleteNode(int d) { // delete a node in the list
            if (next) {
                if (next->data == d) {
                    if (next->next) {
                        Node* temp = next->next;
                        delete next;
                        next = temp;
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
        void Print() { // Print the list
            cout << data << " ";
            if (next) {
                next->Print();
            }
        }
        void CopyList(Node* n) { // Copying list into a new list
            if (next) {
                n->next = new Node(next->data, nullptr);
                next->CopyList(n->next);
            }
        }
        Node* getTail() { // return the tail of the list
            if (next) {
                return next->getTail();
            }
            return this;
        }
};
class LinkedList { // LinkedList class
    public:
        Node * head;
        LinkedList() { // Constructor
            head = nullptr;
        }
        void AddNode(int d) { // Add a node to the list
            if (!head) {
                head = new Node(d, nullptr);
            }
            else if(!head->CheckData(d)) { // check if the node is already in list or not
                if (d < head->data) { // if the new node to add comes before head
                    Node* temp = new Node(d, nullptr);
                    temp->next = head;
                    head = temp;
                }
                else { // if the new node to add comes after head
                    head->AddNode(d);
                }
            }
        }
        void DeleteNode(int d) { // Delete a node from the list
            if (head) {
                if (head->data == d) {
                    if (head->next) {
                        Node* temp = head->next;
                        delete head;
                        head = temp;
                    }
                    else {
                        head = nullptr;
                    }
                }
                else {
                    head->DeleteNode(d);
                }
            }
        }
        void Print() { // Print the list
            if (head) {
                head->Print();
            }
            else {
                cout << "List is empty! " << endl;
            }
        }
        LinkedList &operator-(int d) { // - Operator (LinkedList - int)
            LinkedList *l = new LinkedList();
            LinkedList &returnlist = *l;
            if (head) {
                DeleteNode(d); // delete node from current list first before copying over
                if (head) {
                    l->head = new Node(head->data, nullptr); // create a new node in order to not point to the old list
                    head->CopyList(l->head);
                    return returnlist;
                }
            }
            return returnlist;
        }
        friend LinkedList &operator-(int d, LinkedList &l) { // - Operator (int, LinkedList)
            return l - d;
        }
        LinkedList &operator+(int d) { // + Operator (LinkedList + int)
            LinkedList *l = new LinkedList();
            LinkedList &returnlist = *l;
            if (!head) { // empty list
                l->AddNode(d);
                return returnlist;
            }
            else { // something is in the list
                l->head = new Node(head->data, nullptr); // create a new node in order to not point to the old list
                head->CopyList(l->head); // copy list
                l->AddNode(d); // add the new node
                return returnlist;
            }

        }
        friend LinkedList &operator+(int d, LinkedList &l) { // + Operator (int + LinkedList)
            return l + d;
        }
        bool operator<(int d) { // return true if anything in the list is lower than the data, only checks the first node since the list is sorted
            if (!head || head->data < d) {
                return true;
            }
            return false;
        }
        bool operator>(int d) { // return true if anything in the list is greater than data (LinkedList > int)
            if (!head || head->getTail()->data > d) { // since the list is sorted, just have to compare it to the last thing in the list
                return true;
            }
            return false;
        }
        bool operator==(int d) { // returns true if d is in the list (LinkedList == int)
            if (!head) {
                return false;
            }
            return head->CheckData(d);
        }
        friend ostream &operator<<(ostream &os, LinkedList &l) { // << Operator, Prints the list
            l.Print();
            return os;
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
    l = 13 + l;
    compare(s, l);


    s.insert(1); s.insert(2); s.insert(3); s.insert(4);
    l = l + 2 + 3 + 1 + 4 + 1;
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

    s.erase(2);
    l = 2 - l;
    compare(s,l);

    s.erase(3);
    s.erase(13);
    s.insert(3);
    l = l - 13;
    l = l - 2;
    l = l + 3;
    l = l - 4;
    compare(s,l);

    s.erase(3);
    l = 3 - l;
    compare(s,l);

    s.insert(3);
    l = 3 + l;
    s.insert(20);
    l = l + 20;
    s.insert(1);
    l = l + 1;
    compare(s,l);

    s.erase(1);
    l = 1 - l;
    compare(s,l);

    cout << endl;
    if (l < 10) {
        cout << "Good, L has something less than 10" << endl;
    }
    else {
        cout << "BAD" << endl;
    }
    if (l < 1) {
        cout << "BAD" << endl;
    }
    else {
        cout << "Good, l doesn't have anything less than 1" << endl;
    }
    if (l > 10) {
        cout << "Good, L has something greater than 10" << endl;
    }
    else {
        cout << "BAD" << endl;
    }
    if (l > 23) {
        cout << "BAD" << endl;
    }
    else {
        cout << "Good, L doesn't have anything greater than 23" << endl;
    }
    if (l == 3) {
        cout << "Good, L does have 3" << endl;
    }
    else {
        cout << "BAD" << endl;
    }
    if (l == 25) {
        cout << "BAD" << endl;
    }
    else {
        cout << "Good, L doesn't have 25" << endl;
    }

}