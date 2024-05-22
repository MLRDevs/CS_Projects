# Builder Pattern

*Forces*: having too complex of an object can lead to having multiple parameters in the same constructor

*Solution*: using the Builder Pattern, you can break it down into steps and delegate it to a director to decrease the client and constructor code

### The following example will use C++
```
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
```
### Output:
```
Simple pizza toppings:
Pepperoni

Complex pizza toppings:
Mushroom
Sausage
Extra Cheese

Custom pizza toppings:
Pepperoni
Sausage
```

***

<br>

### Breakdown:
```
class Pizza {
    public:
        vector <string> toppings;

        void ListToppings() {
            cout << "toppings:" << endl;
            for (int i=0; i < toppings.size(); i++) {
                cout << toppings[i] << endl;
            }
        }
};
```
This is the pizza class, this class is the product that the builder class creates. In this example, this will be a pizza.

<br>

```
clas Builder {
    public:
        virtual ~Builder(){};
        virtual void AddPepperoni() = 0;
        virtual void AddMushroom() = 0;
        virtual void AddSausage() = 0;
        virtual void AddExtraCheese() = 0;
};
```
This is the builder class, it holds the virtual methods for the ConcreteBuilder class, these methods are the steps to building the object you want.

<br>

```
class ConcreteBuilder : public Builder {
    private:
        Pizza* pizza;

    public:
        ConcreteBuilder() {
            Reset();
        }
        ~ConcreteBuilder() {
            delete pizza;
        }
        void Reset() {
            pizza = new Pizza();
        }
        void AddPepperoni() {
            pizza->toppings.push_back("Pepperoni");
        }
        void AddMushroom() {
            pizza->toppings.push_back("Mushroom");
        }
        void AddSausage() {
            pizza->toppings.push_back("Sausage");
        }
        void AddExtraCheese() {
            pizza->toppings.push_back("Extra Cheese");
        }
        Pizza* getPizza() {
            Pizza* newpizza = pizza;
            Reset();
            return newpizza;
        }
};
```
This is the ConcreteBuilder class that inherits from the Builder class. When these methods are called they start building the object you want. The Director class calls these methods. If you only want a pizza with Sausage and Mushroom, you can only call those methods, this is the heart of this pattern, just call the ones you need. When you build a brand new pizza, you call ```Reset()``` to start a fresh pizza.

<br>

```
class Director {
    private:
        Builder* builder;
    
    public:
        void setBuilder(Builder* b) {
            builder = b;
        }
        void MakeSimplePizza() {
            builder->AddPepperoni();
        }
        void MakeComplexPizza() {
            builder->AddPepperoni();
            builder->AddMushroom();
            builder->AddSausage();
            builder->AddExtraCheese();
        }
};
```
The Director class is what calls the Builder, in the main method, instead of calling all the seperate steps, you can just make a method to call all of the steps for you and just call the one method in the main method. The ```MakeSimplePizza()``` method just calls the step ```AddPepperoni()``` while the ```MakeComplexPizza()``` calls more steps to making a pizza for more toppings.

<br>

```
ConcreteBuilder* builder = new ConcreteBuilder();
Director* director = new Director();

director->setBuilder(builder);
```
This creates the ConcreteBuilder and the Director used for calling the steps. We set the builder in the director to the ConcreteBuilder we just made.

<br>

```
director->MakeSimplePizza();
Pizza* p = builder->getPizza();
p->ListToppings();
```
Here, we call the method ```MakeSimplePizza()``` to make a simple pizza. That method calls steps to create a pizza, this method only makes a simple pizza calling the step ```AddPepperoni()``` we then get the pizza and print the list of toppings.

<br>

```
director->MakeComplexPizza();
p = builder->getPizza();
p->ListToppings();
```
This makes a more complex pizza, gets the pizza, and then prints the toppings. Without doing it this way we would have to call all the steps individually everytime we want to make a complex pizza. This way, it's all in one method call ```MakeComplexPizza()```. Otherwise we would have to call the methods: ```AddPepperoni()```, ```AddMushroom()```, ```AddSausage()```, ```AddExtraCheese()``` individually.

<br>

```
builder->AddPepperoni();
builder->AddSausage();
p = builder->getPizza();
p->ListToppings();
```
This shows you don't need the Director class if you don't want it, it just makes it easier when you need to call a lot of steps for one object. If you want an object that doesn't have a method to call all the steps, you can always call each step individually, using this we make a custom pizza with two toppings, Pepperoni and Sausage by calling the steps that add those toppings, ```AddPepperoni()``` and ```AddSausage()```. There is no method to call both of these methods with one call, so this way we have to call each individually. Or we could create a method in the Director class to call these for us.

<br>

```
Simple pizza toppings:
Pepperoni

Complex pizza toppings:
Mushroom
Sausage
Extra Cheese

Custom pizza toppings:
Pepperoni
Sausage
```
That is how we get this output:

* create the director and assing it a new concrete builder

* call the director to call the steps to make the object you want, or call the builder to call the specific steps you want to creat the object

* you now have a pointer to the object so now you can do what you want with it, in this example we printed the list of the toppings (steps)

*Preceding Pattern*

[Template](/TemplatePattern.md)

*Following Pattern*

[Visitor](/VisitorPattern.md)