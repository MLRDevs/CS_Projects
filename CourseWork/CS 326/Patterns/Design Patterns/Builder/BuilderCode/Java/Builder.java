// Alex Miller
// Builder Pattern Example

import java.io.*;
import java.util.*;

public class Builder {
	public static void main(String[] args) { // main method

		// create the builder and director
		ConcreteBuilder builder = new ConcreteBuilder();
		Director director = new Director();

		director.setBuilder(builder); // set the builder to the director

		// create a simple pizza and print the toppings
		System.out.print("Simple pizza ");
		director.MakeSimplePizza();
		Pizza p = builder.getPizza();
		p.ListToppings();

		System.out.println();

		// create a complex pizza and print the toppings
		System.out.print("Complex Pizza ");
		director.MakeComplexPizza();
		p = builder.getPizza();
		p.ListToppings();

		System.out.println();

		// don't always need the director, this creates a custom pizza and prints the toppings
		System.out.print("Custom pizza ");
		builder.AddPepperoni();
		builder.AddSausage();
		p = builder.getPizza();
		p.ListToppings();
	}
}
class Pizza { // product
	public List<String> toppings = new ArrayList<String>(); // list of all the toppings

	public void ListToppings() { // print the toppings
		System.out.println("toppings:");
		System.out.println(toppings);
	}
}
class Building { // builder
	public void AddPepperoni(){}
	public void AddMushroom(){}
	public void AddSausage(){}
	public void AddExtraCheese(){}
}
class ConcreteBuilder extends Building { // concrete builder
	private Pizza pizza; // pizza object

	public ConcreteBuilder() { // if new concrete builder then reset
		Reset();
	}
	public void Reset() { // make new pizza
		pizza = new Pizza();
	}
	public void AddPepperoni() { // add pepperoni
		pizza.toppings.add("Pepperoni");
	}
	public void AddMushroom() { // add mushroom
		pizza.toppings.add("Mushroom");
	}
	public void AddSausage() { // add sausage
		pizza.toppings.add("Sausage");
	}
	public void AddExtraCheese() { // add extra cheese
		pizza.toppings.add("Extra Cheese");
	}
	public Pizza getPizza() { // get the pizza, then reset old pizza
		Pizza p = pizza;
		Reset();
		return p;
	}
}
class Director { // direct builder what to build
	private Building builder;

	public void setBuilder(Building b) { // set the builder
		builder = b;
	}
	public void MakeSimplePizza() { // make a pizza with just pepperoni
		builder.AddPepperoni();
	}
	public void MakeComplexPizza() { // make a pizza with pepperoni, mushroom, sausage, and extra cheese
		builder.AddPepperoni();
		builder.AddMushroom();
		builder.AddSausage();
		builder.AddExtraCheese();
	}
}