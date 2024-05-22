// Alex Miller
// Example of Visitor Pattern

#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
using namespace std;

class Visitor {
    public:
        virtual void visitSquare(Square* s) = 0;
        virtual void visitCircle(Circle* s) = 0;
};
class Shape {
    public:
        virtual ~Shape() {};
        virtual void Accept(Visitor* v) = 0;
};
class Square : public Shape {
    public:
        void accept(Visitor* v) {
            v->visitSquare(this);
        }
        string getSquare() {
            return "Square";
        }
};
class Circle : public Shape {
    public:
        void accept(Visitor* v) {
            v->visitCircle(this);
        }
        string getCircle() {
            return "Circle";
        }
};
class ConcreteVisitor : public Visitor {
    public:
        void visitSquare(Square* s) {
            cout << s->getSquare() << " SquareVisitor" << endl;
        }
        void visitCircle(Circle* s) {
            cout << s->getCircle() << " CircleVisitor" << endl;
        }
};
int main() {
    

}