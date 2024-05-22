# MVC (Model View Controller)

*Forces*: needing a layered architecture where a layer of objects can interact with other objects without them knowing that the objects that are interacting with them even exist. They only interact with what they need.

*Solution*: [Observer Pattern](/ObserverPattern.md)

### Layers
This pattern uses layers to control objects and update them when needed. An example could be a User Interface and a Database. The Database has no clue that the User Interface exists but the User Interface could display stuff that the Database holds.

<br>

*Following Pattern*

[Observer Pattern](/ObserverPattern.md)

*Preceding Pattern*

[Template](/TemplatePattern.md)