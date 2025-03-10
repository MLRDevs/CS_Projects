# MVVM (Model View Viewmodel) Pattern

*Forces*: Seperating development of GUI (Graphical User Interface) of the view from the backend code such as the bulk of the application work that the GUI doesn't need

*Solution*: The MVVM Pattern helps seperate making it easier to make modifications to the right area.

### Basic Concept
MVVM can be broken up to 3 parts:
* View
* ViewModel
* Model

<br>

### View
This is the visual representation of the application. For example let's say we have a button on the screen. When the button is clicked, the logic that makes that button worked is not written in the View. Instead, the View sends the command to the ViewModel that then deals with it, this is all just visual.

<br>

### ViewModel
This part is responsible for getting commands from the View to the Model. In the button scenario, this is the part that takes the command and sends it to the Model to then be executed. Any changes will go through the ViewModel and then notify the View. This is the link between the GUI and the backend code to make everything work together.

<br>

### Model
This is the backend code. This may include the data for the application that's tied to a database. This part is not visual and all happening behind the scenes of the user. The Model will send a notification to the ViewModel which will then send one to the View so everything is updated. This is also where commands sent from the ViewModel are made and then sent back.

<br>

*Preceding Pattern*

[Model View Controller](/MVC.md)

*Following Pattern*

[Observer Pattern](/ObserverPattern.md)