# Introduction to Java: Part 2

**Hello young aspiring Sciborgs programmer!** This guide will serve as a practical introduction to **the Java programming language**.

Here is what will be covered here:

1. **[The Boolean Data Type](#the-boolean-data-type)**
2. **[Decision Making with Booleans](#decision-making-with-booleans)**
3. **[How to create conditions](#how-to-create-conditions)**
4. **[Different Types of Numbers](#different-types-of-numbers)**
5. **[Strings and Characters](#strings-and-characters)**
7. **[Lists, Arrays, Matrices, and Maps](#lists-arrays-matrices-and-maps)**
8. **[Scopes and Scope Keywords](#scopes-and-scope-keywords)**
9. **[Constructors and Overloading](#constructors-and-overloading)**
10. **[Console Input and Output](#console-input-and-output)**

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

```
boolean something = true;

if (something == true) {
    // This will only run one time.
    someObject.doSomething();
}
```

### **While** something is true, **keep doing** something

```
boolean something = true;

while (something == true) {
    // This will run repeatedly.
    // Probably will crash the PC.
    someObject.doSomething();
}
```

### **For** some amount of time, **keep doing** something

```
Number[] someDataSet = new Number[]{0, 1, 2, 3, 4, 5}; 

for (Number n: someDataSet) {
    // This will run for every element in the dataset.
    someObject.doSomethingWithN(n);
}
```

### **For** some number of times, **keep doing** something

```
// Here is another way to use for-loop!
for (int n = 1; n < 67; n++) {
    // This will run 67 times over.
    someObject.doSomethingWithN(n);
}
```

## How to Create Conditions

Java gives us a very specific way to make our conditions (what we put into the **parenthesis** of our **decision-making structures**).

In Java, you use two equal sign symbols `==` to create an **equation** between two boolean values **or** two objects.

```
True == False; // This is false!
False == False; // This is true!
True == True; // This is true!
```

In Java, you use the exclamation mark `!` symbol to **negate** a boolean value.

```
!True == False; // This is true!
!False == False; // This is false!
!False == True; // This is true!
```

In Java, you use two vertical bars `||` to create a **disjunction** between two boolean values (this is equivalent to using the word **"or"**).

```
True || False; // This is true!
True || True; // This is true!
False || False; // This is false!
```

In Java, you use two ampersand symbols `&&` to create a **conjunction** between two boolean values.

```
True && True; // This is true!
True && False; // This is false!
False && False; // This is false!
```

In Java, you use the greater-than `>` and less-than symbols `<` to create an **inequality** between two numbers.

```
6 < 7; // This is true!
6 > 7; // This is false!
```

In Java, you can use the greater-than or equal-to `>=` as well as the less-than or equal-to `<=` to create an **inclusive inequality**.

```
7 >= 7; // This is true!
7 <= 7; // This is true!

7 > 7; // This is false!
7 < 7; // This is false!
```

## Different Types of Numbers

There are **multiple** types of numbers in Java. All of these types of  numbers have different **memory sizes** and **ranges of values** that it can store.

```
Number number = 5; // This is not real!
```

**Bytes** ```byte``` are **whole numbers** that take up **8 bits** in size. They are the **smallest** form of number storage; only being able to store values from **-128 to 127**. The reason why values only go up to 127 is because **1 bit** is reserved by Java in order to describe **whether the number is positive or negative**. 

```
// Positive/Negative Bit --> *0* 0101000
byte coolNumber = 40; 
```

**Shorts** ```short``` are **whole numbers** that take up **16-bits** in size. They are the **second-smallest** form of number storage; being able to store values from **-32768 to 32767**. Once again, one bit is reserved for the **signature**.

```
// 0000000110111000
short coolNumber = 440; 
```

**Integers** ```int``` are **whole numbers** that take up **32-bits** in size. They are **much bigger** than shorts; being able to store values from **-2147483648 to 2147483647**. Once again, one bit is reserved for the **signature**.

```
// 00000000000000001010110110011000
int coolNumber = 44440; 
```

**Longs** ```long``` are **whole numbers** that take up **64-bits** in size. They are **much bigger** than integers; being able to store values from **-9223372036854775808 to 9223372036854775807**. Once again, one bit is reserved for the **signature**.

```
// 00000000 00000000
// 00000000 00000000
// 00001100 01101011
// 11110100 01000010

// Make sure to add the 'L'!
long coolNumber = 4444444440L; 
```

**Floats** ```float``` are **fractional numbers** that take up **32-bits** in size. They are the same size as integers. Floats are **extremely** complicated and would require another **40 minute lecture** to properly understand. Therefore, **we won't be going into detail about them**.

```
// I am not even going to try this one.
float weirdNumber = 3.00002f;
```

**Doubles** ```double``` are **fractional numbers** that take up **64-bits** in size. They are the same size as longs. Doubles are also **extremely** complicated. Therefore, **we won't be going into detail about them**. Just know that they are **structured** and **function** the same as floats, except they are **twice as large**.

```
// I am not even going to try this one either these numbers are weird.
double weirderNumber = 3.14159265358;
```

## Strings and Characters

**Characters** are what makes up **text** . Each character has a specific **whole number** assigned to it that will **represent it in memory**. 

>These numbers are assigned by the *American Standard Code for Information Interchange* also known as **ASCII**.

**Characters** ```char``` are represented using ```'Single Quotes'``` while **Strings** ```String``` are represented using ```"Double Quotes"```.

>Hello young aspiring Sciborgs programmer! As you can tell, this part of SciGuides is **under construction**. Stay tuned for more code stuff!


## Lists, Arrays, Matrices, and Maps

## Scopes and Scope Keywords

## Constructors and Overloading

## Console Input and Output






