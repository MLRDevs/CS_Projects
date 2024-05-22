#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
using namespace std;

class Pizza { // pizza class, the product the builder class is building
    public:
        vector <string> toppings; // vector strings of toppings

        void ListToppings() { // print all the toppings
            cout << "toppings:" << endl;
            for (int i=0; i < toppings.size(); i++) {
                cout << toppings[i] << endl;
            }
        }
};
class Builder { // Builder class, ConcreteBuilder inherits from this class
    public:
        virtual ~Builder(){};
        virtual void AddPepperoni() = 0;
        virtual void AddMushroom() = 0;
        virtual void AddSausage() = 0;
        virtual void AddExtraCheese() = 0;
};
class ConcreteBuilder : public Builder { // concrete builder that adds all the toppings, thus building the pizza
    private:
        Pizza* pizza; // pointer to pizza

    public:
        ConcreteBuilder() { // when making a new pizza, reset the builder 
            Reset();
        }
        ~ConcreteBuilder() { // deallocating memory
            delete pizza;
        }
        void Reset() { // create a new pizza
            pizza = new Pizza();
        }
        void AddPepperoni() { // add pepperoni
            pizza->toppings.push_back("Pepperoni");
        }
        void AddMushroom() { // add mushroom
            pizza->toppings.push_back("Mushroom");
        }
        void AddSausage() { // add sausage
            pizza->toppings.push_back("Sausage");
        }
        void AddExtraCheese() { // add extra cheese
            pizza->toppings.push_back("Extra Cheese");
        }
        Pizza* getPizza() { // get the pizza
            Pizza* newpizza = pizza;
            Reset();
            return newpizza;
        }
};
class Director { // Director class, directs the builder for what to build
    private:
        Builder* builder; // builder pointer

    public:
        void setBuilder(Builder* b) { // set the builder
            builder = b;
        }
        void MakeSimplePizza() { // make a simple pizza, just pepperoni
            builder->AddPepperoni();
        }
        void MakeComplexPizza() { // making a more complex pizza with more toppings
            builder->AddPepperoni();
            builder->AddMushroom();
            builder->AddSausage();
            builder->AddExtraCheese();
        }
};
int main() { // main method
    // creating pointers to builder and director objects
    ConcreteBuilder* builder = new ConcreteBuilder();
    Director* director = new Director();

    director->setBuilder(builder); // setting the builder for the director

    // make a simple pizza
    cout << "Simple pizza ";
    director->MakeSimplePizza();
    Pizza* p = builder->getPizza();
    p->ListToppings();
    delete p;

    cout << endl;

    // make a more complex pizza
    cout << "Complex pizza ";
    director->MakeComplexPizza();
    p = builder->getPizza();
    p->ListToppings();
    delete p;

    cout << endl;

    // making a custom pizza, shows that you don't need the director
    cout << "Custom pizza ";
    builder->AddPepperoni();
    builder->AddSausage();
    p = builder->getPizza();
    p->ListToppings();
    delete p;

    // deallocating memory
    delete builder;
    delete director;
}