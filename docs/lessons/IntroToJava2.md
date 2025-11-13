# Introduction to Java 2

**Hello young aspiring programmer!** This guide will serve as a practical introduction to **the Java programming language**.

Here is what will be covered here:

1. **[The Boolean Data Type](#the-boolean-data-type)**
2. **[Decision Making with Booleans](#decision-making-with-booleans)**
3. **[How to create conditions](#how-to-create-conditions)**
4. **[Different Types of Numbers](#different-types-of-numbers)**
5. **[Strings and Characters](#strings-and-characters)**
6. **[Lists and Arrays](#lists-and-arrays)**
7. **[Scopes and Scope Keywords](#scopes-and-scope-keywords)**
8. **[Constructors and Overloading](#constructors-and-overloading)**
9. **[Console Input and Output](#console-input-and-output)**

If you are curious on **what apps you're gonna need to get started**, head over to [our Software Setup Guide](SoftwareSetup.md).

## The Boolean Data Type

Booleans are **the absolute simplest form of data storage possible**. A boolean is represented by a singular **1** or **0**. This represents the value of **one singular transistor** in the computer. However, to save time, Java only operates with **bytes** or chunks of **8 bits** (8 transistors). Therefore, Java takes up **1 byte** to store **1 boolean value**, however it will only take up **1 byte** to store **8 boolean values**.

>Similar to how a number can be used to represent both **the price of a RoboRIO** or **the amount of members on the Sciborgs robotics team**. A boolean can also be interpreted in many ways.

A boolean can used to represent:

1. **The Answer to a Yes or No Question**
2. **Whether a mechanism is on or off**
3. **Whether a statement is true of false**

Booleans are heavily used in **decision-making** because, surprisingly, nearly everything in logic comes down to **statements** being either **true or false**.

## Decision Making with Booleans

There are a couple of different **decision making techniques** that can be used in Java.

### **If** something is true, **then** do something

```java
boolean something = true;

if (something == true) {
    // This will only run one time.
    someObject.doSomething();
}
```

### **While** something is true, **keep doing** something

```java
boolean something = true;

while (something == true) {
    // This will run repeatedly.
    // Probably will crash the PC.
    someObject.doSomething();
}
```

### **For** each element in a list, **keep doing** something

```java
Number[] someDataSet = new Number[]{0, 1, 2, 3, 4, 5}; 

for (Number n: someDataSet) {
    // This will run for every element in the dataset.
    someObject.doSomethingWithN(n);
}
```

### **For** some number of times, **keep doing** something

```java
// Here is another way to use for-loop!
for (int n = 1; n < 67; n++) {
    // This will run 67 times over.
    someObject.doSomethingWithN(n);
}
```

## How to Create Conditions

Java gives us a very specific way to make our conditions (what we put into the **parenthesis** of our **decision-making structures**).

Use two equal sign symbols `==` to create an **equation** between two boolean values **or** two objects.

```java
True == False; // This is false!
False == False; // This is true!
True == True; // This is true!
```

Use the exclamation mark `!` symbol to **negate** a boolean value.

```java
!True == False; // This is true!
!False == False; // This is false!
!False == True; // This is true!
```

Use two vertical bars `||` to create a **disjunction** between two boolean values (this is equivalent to using the word **"or"**).

```java
True || False; // This is true!
True || True; // This is true!
False || False; // This is false!
```

Use two ampersand symbols `&&` to create a **conjunction** between two boolean values.

```java
True && True; // This is true!
True && False; // This is false!
False && False; // This is false!
```

Use the greater-than `>` and less-than symbols `<` to create an **inequality** between two numbers.

```java
6 < 7; // This is true!
6 > 7; // This is false!
```

Use the greater-than or equal-to `>=` as well as the less-than or equal-to `<=` to create an **inclusive inequality**.

```java
7 >= 7; // This is true!
7 <= 7; // This is true!

7 > 7; // This is false!
7 < 7; // This is false!
```

## Different Types of Numbers

There are **multiple** types of numbers in Java. All of these types of  numbers have different **memory sizes** and **ranges of values** that it can store.

```java
Number number = 5; // This is not real!
```

**Bytes** ```byte``` are **whole numbers** that take up **8 bits** in size. They are the **smallest** form of number storage; only being able to store values from **-128 to 127**. The reason why values only go up to 127 is because **1 bit** is reserved by Java in order to describe **whether the number is positive or negative**.

```java
// Positive/Negative Bit --> *0* 0101000
byte coolNumber = 40; 
```

**Shorts** ```short``` are **whole numbers** that take up **16-bits** in size. They are the **second-smallest** form of number storage; being able to store values from **-32768 to 32767**. Once again, one bit is reserved for the **signature**.

```java
// 0000000110111000
short coolNumber = 440; 
```

**Integers** ```int``` are **whole numbers** that take up **32-bits** in size. They are **much bigger** than shorts; being able to store values from **-2147483648 to 2147483647**. Once again, one bit is reserved for the **signature**.

```java
// 00000000000000001010110110011000
int coolNumber = 44440; 
```

**Longs** ```long``` are **whole numbers** that take up **64-bits** in size. They are **much bigger** than integers; being able to store values from **-9223372036854775808 to 9223372036854775807**. Once again, one bit is reserved for the **signature**.

```java
// 00000000 00000000
// 00000000 00000000
// 00001100 01101011
// 11110100 01000010

// Make sure to add the 'L'!
long coolNumber = 4444444440L; 
```

**Floats** ```float``` are **fractional numbers** that take up **32-bits** in size. They are the same size as integers. Floats are **extremely** complicated and would require another **40 minute lecture** to properly understand. Therefore, **we won't be going into detail about them**.

```java
// I am not even going to try this one.
float weirdNumber = 3.00002f;
```

**Doubles** ```double``` are **fractional numbers** that take up **64-bits** in size. They are the same size as longs. Doubles are also **extremely** complicated. Therefore, **we won't be going into detail about them**. Just know that they are **structured** and **function** the same as floats, except they are **twice as large**.

```java
// I am not even going to try this one either these numbers are weird.
double weirderNumber = 3.14159265358;
```

## Strings and Characters

**Characters** are what makes up **text**. Each character has a specific **whole number** assigned to it that will **represent it in memory**.

>These numbers are assigned by the *American Standard Code for Information Interchange* also known as **ASCII**. 'A' would be represented by a **65**.

**Characters** ```char``` are represented using ```'Single Quotes'``` while **Strings** ```String``` are represented using ```"Double Quotes"```.

Strings are **not** primitives, they are **classes** that hold **a list of characters**. Strings have many different **utility methods** to aid in working with them.

1. **String.length()** - returns the length of the string
2. **String.charAt()** - returns the character in a specific position of the string
3. **String.equals()** - returns whether-or-not two strings are equal.

> **Do not** use '==' when working with strings! (Strings compare memory addresses **instead** of content when using '==')

## Lists and Arrays

**Lists** ```List<Class>``` are used to hold **multiple objects** in an organized fashion (each object has an **position** in the list). Lists can be made of **any object** simply by specifying the **class of those objects** in the ```<Angle Brackets>```. Lists **cannot** hold primitives.

```java
// There are many different types of lists!
// Just use ArrayList for now.
List<Integer> coolList = new ArrayList<>();

coolList.add(5); // Index: 0
coolList.add(6); // Index: 1
coolList.add(7); // Index: 2

coolList.get(2); // Returns 7!
```

**Arrays** ```[]``` are similar to Lists in that they store **an ordered set of objects**. You create arrays by putting their elements in ```{Curly Braces}```. There are some key **differences** between Lists and Arrays.

1. **Arrays can operate on primitives**
2. **Arrays cannot change in length after they are created**
3. **Arrays are not classes**
4. **Arrays are faster to use than Lists**

The reason why **Arrays** are much more **rigid** and **fast** than Lists are is because Arrays are **a fundamental feature of Java** while the List class is written **using Java**.

```java
// Array with a permanent length of 5.
int[] coolArray = {0,1,2,3,4};

coolArray[1]; // This returns 1!

coolArray[67]; // This throws an error!
coolArray[67] = 2; // This also throws an error!
```

## Scopes and Scope Keywords

**Scope** describes **where a field/variable can be accessed**. Something with a ```private``` scope can only be accessed **within the object that it has been created inside**. Something with a ```public``` scope can be accessed from **outside the object that it has been created inside**.

```java
// Here is the "Stephanie" class.
public class Stephanie {
    // This class has two fields!
    private int height = 67;
    public int labubus = 4;

    public Stephanie() {}
}

// This is another class!
public class Main {
    // Here is a "Stephanie" object made from the "Stephanie" class.
    Stephanie steph = new Stephanie();

    // You cannot do this!
    int stephHeight = steph.height;

    // You can do this!
    int stephLabubus = steph.labubus;
}
```

Things are not only scoped **in space**, but also **in time** (according to Einstien). **You cannot use something before it has been created**.

```java
System.out.print(x); // You can't access 'x' before it has been created!

int x = 5;

System.out.print(x); // Prints out "5".
```

Because Java utilizes **Object-Oriented-Programming**, all fields and methods are created **simultaneously**.

```java
public class Arthur {
    public double getGPA() {
        return apCSGrade * 0.04;
    }

    // This doesn't break the laws of special relativity!
    int apCSGrade = 100;
}
```

Only things **inside** of the methods have to worry about the **scope** of their **timing**.

## Constructors and Overloading

In order to make **objects** using **classes**, we need to define a **constructor method**. A constructor is a **special** type of method that is called using the **new** keyword. The reason why this type of method is special is because **no other method** has the power to **construct objects**.

```java
// Lets go back to the Stephanie class...
public class Stephanie {
    private int height = 67;
    public int labubus = 4;

    // This is the constructor!
    public Stephanie() {
        // This code will be ran when a Stephanie object gets created!
    }
}
```

Constructors have a **special format** that is used **to make them** (so that Java can tell what methods are constructors). They have to **be named after the class** and **not have a specified output-type** 

>Notice how there is no output-type in the above example.

Constructors return **the newly created object** which can then be assigned to **fields/variables** to store them.

```java
Stephanie steph = new Stephanie();
```

Another important feature of constructors is that they allow you to run code **immediately** after the object has been created. 

>**Anything in the curly braces will be ran once the Stephanie object has been created**.

## Console Input and Output

There are many ways in which Java has the power to **interface** (send and receive information) with the user. The **simplest** and **fastest** method is through **the console**. The console is essentially **just a bunch of text that can be manipulated to mean something**. What separates the **console** from the **terminal** is that the console **exclusively** serves to help us interact with our program

>The terminal has the power to do almost anything!

To **write something** into the console we use the ```System.out``` object. There are only two notable methods here:

1. **System.out.print ( )**
2. **System.out.println ( )**

Regular printing ```print``` prints things **on the same line** while line-printing ```println``` prints out **an entire line**.

```java
System.out.println("5");

System.out.print("6");
System.out.print("7");
```

> **5** ( Line 1 )

> **6 7** ( Line 2 )

**NOTE:** System.out.print will only accept **one type of data** at a time! If you want to print **a number and a letter**, you must convert both to a **String** by adding ```""```

```java
System.out.println("" + 5 + 'a');
```

To **read something** from the console (that the user types in), we use the ```System.in``` object along with the ```Scanner``` class.

```java
// We are scanning System.in for inputs!
Scanner scanner = new Scanner(System.in);

scanner.nextInt(); // The next number that the user types out.
scanner.next(); // The next string that the user types out.
```

>That is all! Farewell young aspiring programmer!
