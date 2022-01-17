# Linked List
-----------------

<img src="LinkedListQuickRef.PNG" height="600">

<img src="linkedList.PNG" height="125">
(Depicted Doubly Linked List because you have a reference to next and previous)

-  Expensive on memory (Need to know reference to next and previous, so takes up extra memory)
-  Made up of multiple nodes
    - Head Node - previous points to null
    - Tail Node - next points to null
    - Each Node contains reference to next node and reference to previous node
- LinkedLists are implementations of the Queue interface

```
LinkedList<Person> linkedList = new LinkedList<>();

linkedList.add(new Person("Alex", 21));
System.out.println(linkedList);
//returns:
//Person[name=Alex, age=21]

linkedList.add(new Person("Will", 25));
System.out.println(linkedList);

//returns:
//Person[name=Alex, age=21]
//Person[name=Will, age=25]

//Use a list iterator to loop through a list
ListIterator<Person> personListIterator = linkedList.listIterator();

//Loop forwards through list
while(personListIterator.hasNext())
{
  System.out.println(personListIterator.next());
}
//returns:
//Person[name=Alex, age=21]
//Person[name=Will, age=25]

//Loop backwards through list
while(personListIterator.hasPrevious())
{
  System.out.println(personListIterator.previous());
}
//returns:
//Person[name=Will, age=25]
//Person[name=Alex, age=21]
```

----------

### Remove from linked list

```
linkedList.remove("insertItemHere");
```

----------

Add implementations/parameters:

<img src="linkedListAdd.PNG" height="125">


-----------

```
  public class LinkedListNode {

    public int value;
    public LinkedListNode next;

    public LinkedListNode(int value) {
        this.value = value;
    }
}

LinkedListNode a = new LinkedListNode(1);
LinkedListNode b = new LinkedListNode(2);
LinkedListNode c = new LinkedListNode(3);

a.next = b;
b.next = c;

deleteNode(b);

```
