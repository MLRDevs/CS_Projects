// Alex Miller
// Factory Method Example
#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class Car { // product
    public:
        virtual ~Car() {}
        virtual string getCar() = 0; // getting the data the product holds
};
class AudiCar : public Car { // type of product
    public:
        string getCar() {
            return "Audi";
        }
};
class FordCar : public Car { // type of product
    public:
        string getCar() {
            return "Ford";
        }
};
class Factory { // factory that makes the product
    public:
        virtual ~Factory() {}
        virtual Car* FactoryMethod() = 0;

        string BuildCar() { // building the product
            cout << "Building your car..." << endl;
            Car* car = this->FactoryMethod(); // getting an instance of the correct product
            string result = "Car built: " + car->getCar(); // printing result
            delete car; // deallocating memory
            return result; // returning result
        }
};
class CreateAudi : public Factory { // create the Audi
    public:
        Car* FactoryMethod() {
            return new AudiCar();
        }
};
class CreateFord : public Factory { // create the Ford
    public:
        Car* FactoryMethod() {
            return new FordCar();
        }
};
int main() { // main method

    // create Audi
    cout << "Attempting to create an Audi" << endl;
    Factory* factory = new CreateAudi(); // create the Audi
    cout << factory->BuildCar() << endl; // print the result

    cout << endl;

    // create Ford
    cout << "Attempting to create a Ford" << endl;
    factory = new CreateFord(); // create the Ford
    cout << factory->BuildCar() << endl; // print the result
}