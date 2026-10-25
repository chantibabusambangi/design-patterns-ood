allow us to have an object which have different subscribers 
and they get notified about a change in the state of the object(publisher).

 When one object(publisher) changes state, 
 all its dependent objects (subscribers) are automatically notified and updated.
publisher should able to remove/add subscribers.
**Pattern Roles**
 1. Subject (Publisher)
Holds data
Maintains list of observers
Notifies observers when data changes

2. Observer (Subscriber)

Receives updates from subject

Reacts to changes