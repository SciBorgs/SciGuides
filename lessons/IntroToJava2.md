# Introduction to Java: Part 2

**Hello young aspiring Sciborgs programmer!** This guide will serve as a practical introduction to **the Java programming language**.

Here is what will be covered here:

1. **[The Boolean Data Type](#the-boolean-data-type)**
2. **[Decision Making with Booleans](#decision-making-with-booleans)**
3. **[How to create conditions](#how-to-create-conditions)**
4. **[Different Types of Numbers](#different-types-of-numbers)**
5. **[Strings and Characters](#strings-and-characters)**
6. **[StringBuilder and String operators](#stringbuilder-and-string-operators)**
7. **[Lists, Arrays, Matrices, and Maps](#lists-arrays-matrices-and-maps)**
8. **[Scopes and Scope Keywords](#scopes-and-scope-keywords)**
9. **[Constructors and Overloading](#constructors-and-overloading)**
10. **[Console Input and Output](#console-input-and-output)**

If you are curious on **what apps you're gonna need to get started**, head over to [our Software Setup Guide](SoftwareSetup.md).

## The Boolean Data Type

Booleans are **the absolute simplest form of data storage possible**. A boolean is represented by a singular **1** or **0**. This represents the value of **one singular transistor** in the computer.

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

**Hello young aspiring Sciborgs programmer!** (I'm not sure how you got here). This part of SciGuides is currently **under construction**. 

*Greatness awaits us.*

## Different Types of Numbers

## Strings and Characters

## StringBuilder and String operators

## Lists, Arrays, Matrices, and Maps

## Scopes and Scope Keywords

## Constructors and Overloading

## Console Input and Output






