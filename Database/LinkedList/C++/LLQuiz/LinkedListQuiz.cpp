// Alex Miller
#include <iostream>
using namespace std;


class Node
{
   public:

	Node(int _val, Node *_next)
	{
		val = _val;
		next = _next;
	}
	int val;
	Node *next;
    bool monotonic() {
        if (next) {
            if (val > next->val) {
                return next->monotonic();
            }
            else {
                return false;
            }
        }
        return true;
    }
};

class Head
{
	public:
	Node *head;
	Head() { head = nullptr; }
	void insert(int val)
	{
		head=new Node(val, head);
	}
	friend ostream &operator<<(ostream &os, const Head &h)
	{
		for(Node *ptr = h.head; ptr != nullptr; ptr = ptr->next)
			os << ptr->val << " ";
		return os;
	}
    bool monotonic() { // return true if list is in order going downwards
        if (head) {
            return head->monotonic();
        }
        return false;
    }
};

int main()
{
	Head h1;
	h1.insert(11);
	h1.insert(22);
	h1.insert(33);
	h1.insert(44);
	cout << h1 << endl;
	if (h1.monotonic())
		cout << "That list is in order going downwards" << endl;
	else
		cout << "That list is NOT in order going downwards" << endl;
	cout << "That should have been a YES" << endl;




	Head h2;
	h2.insert(11);
	h2.insert(22);
	h2.insert(33);
	h2.insert(44);
	h2.insert(-3);
	cout << h2 << endl;
	if (h2.monotonic())
		cout << "That list is in order going downwards" << endl;
	else
		cout << "That list is NOT in order going downwards" << endl;
	cout << "That should have been a NO" << endl;

	Head h3;
	h3.insert(111111);
	h3.insert(22);
	h3.insert(33);
	h3.insert(44);
	cout << h3 << endl;
	if (h3.monotonic())
		cout << "That list is in order going downwards" << endl;
	else
		cout << "That list is NOT in order going downwards" << endl;
	cout << "That should have been a NO" << endl;


}