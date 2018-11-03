
/*
 *   By Emily Einhorn
 *   An implementation of the Map interface.
 *
 *   A doubly linked list implementation is used.
 *   Front and rear sentinel nodes are used.
 */

public class Map <K, V> implements MapInterface<K, V>
{
    private Node header;   // Pointer to the front sentinel of the list.


    // The Constructor sets up the sentinel nodes with
    // header pointing to the front.

    public Map()
    {
        Node front = new Node();   // Construct the sentinel
        Node rear = new Node();    // nodes.

        front.prev = null;   // Link the sentinels.  All map
        front.next = rear;   // items will be between the sentinels
        rear.prev  = front;  // so each items is assured to have
        rear.next  = null;   // a node in front and in back.

        header = front;  // The header points to the front node.
    }


    public int getSize()
    {
        Node ptr = header.next;     //skips the front sentinel
        int count = 0;              //counts number of nodes

        while (ptr.next != null)
        {
          count++;                  //adds 1 to the count
          ptr = ptr.next;           //moves to next node
        }
        return count;               //once at end, return the number of nodes
    }

    public void makeEmpty()
    {
        Node ptr = header;          //pointer to the front sentinel of list

        while (ptr.next != null)    //traverses the list to the rear sentinel
          ptr = ptr.next;

        ptr.prev = header;          //assigns the rear sentinel to point to the front
        header.next = ptr;          //assigns the front sentinel to point to the rear
    }


    public void insert(K key, V value)
    {
      Node ptr = header.next;       //skips front sentinel

      while (ptr.next != null)      //traverses the list
      {
        if (ptr.key.equals(key))    //if current node's key is equal to the key
        {
          ptr.value = value;        //replace node's value with new value
          return;                   //key was found, so method exits
        }
        else
          ptr = ptr.next;           //if current node's key not equal to key,
      }                             //move to next node

        Node newNode = new Node();  //if key was not found, create a new node
        newNode.prev = ptr.prev;
        newNode.next = ptr;
        newNode.key = key;
        newNode.value = value;

        ptr.prev.next = newNode;   //set the previous node to point to new node
        ptr.prev = newNode;        //set the rear sentinel to point to new node
    }


    public void remove(K key)
    {
        Node ptr = header.next;     //skips the front sentinel

        while (ptr.next != null)
        {
          if (ptr.key.equals(key))  //if current node's key equals parameter key
          {
              ptr.prev.next = ptr.next;  //assigns the previous node to point to
                                         //the node after the removal node
              ptr.next.prev = ptr.prev;  //assigns the next node to point to
                                         //the node before the removal node
              return;
		  }
          else                      //if current node's key not equal to key,
            ptr = ptr.next;         //move to next node
        }

    }


    public V getValue(K key)
    {
        Node ptr = header.next;         // skips the front sentinel

        while (ptr.next != null)
        {
          if (ptr.key.equals(key))      //if the current node's key is parameter key
            return ptr.toString();           //return that key's value
          else
            ptr = ptr.next;             //if keys don't match, move to next node
        }
        return null;                    //if key not found in list, return null
    }

    public boolean isEmpty()
    {
        if (getSize() == 0)             //if there are no nodes in the list
          return true;
        else                            //if there are nodes in the list
          return false;
    }

    /*
     *   toString() - return a String representation
     *                of the map.
     */

    public String toString()
    {
        String str = "The Map\n--------------\n";

        Node ptr = header.next;

        while (ptr.next != null) {
            str = str + "key: ";
            str = str + ptr.key.toString() + "\n";
            str = str + "Date of Birth: ";
            str = str + ptr.birthday.toString() + "\n";
            str = str + "Blood Type: ";
            str = str + ptr.bloodType.toString() + "\n";
            str = str + "Allergies: ";
            str = str + ptr.allergy.toString() + "\n";
            str = str + "Gender: ";
            str = str + ptr.gender.toString() + "\n";
            str = str + "Surgical History: ";
            str = str + ptr.surgery.toString() + "\n";
            str = str + "\n";

            ptr = ptr.next;
        }

        str = str + "--------------\n";

        return str;
    }

    /*
     *    Inner Class - Node objects for Map items
     *                  in a doubly linked list.
     *
     */

    private class Node
    {
        public K key;       // The item's key.
        public T birthday;
        public T bloodType;
        public T medication;
        public T allergy;
        public T gender;
        public T surgery;
        public Node prev;   // Pointer to the previous Node.
        public Node next;   // Pointer to the next node.
    }

}
