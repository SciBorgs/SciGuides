# Java 101

Hello! This guide will serve as an **introduction** to **the Java programming language**.

Here is what will be covered here:

1. **[What is a program?](#what-is-a-program)**
2. **[What is Java?](#what-is-java)**
3. **[How is Java code organized?](#how-is-java-code-organized)**
4. **[How do we store things?](#how-do-we-store-things)**
5. **[How do we do things with those stored values?](#how-do-we-do-things-with-those-stored-values)**
6. **[Basic Syntax and Convention](#basic-syntax-and-convention)**
7. **[Objects and Constructors](#objects-and-constructors)**
8. **[The Console and System Class](#the-console)**

If you are curious on **what apps you're gonna need to get started** head over to [our Day 1 Guide](./Intro.md) to learn more.

## What is a program?

A **program** is **an ordered list of instructions** that are done **one-after-the-other** by the computer. We write **programs** with **code**. It is **written** in text with a special set of rules called **Syntax** (this is like **grammer** and **punctuation** rules, but for code). Every program has to be **broken down** into actions that a **CPU** can execute. These actions have to be in **binary** and are predefined **by the specific CPU that you are using** using specific **codes** (ARM and x86 processors are coded differently for this reason, they have different sets of commands).

> CPU Commands include things like **ADD** and **SUBTRACT**. These commands can be represented with **binary codes** such as 0110 or 0111 that the CPU can **read** and **understand**.

## What is Java?

**Java** is a **language** that we write code in. Java utilizes **english** words in a syntax that is very reliant on **Curly Braces { }** to define when certain **segements of code** start/stop, **Parentheses ( )** for operations and math, and **SemiColons;** to end specific **actions**. This lets Java code **ignore indentation** (and spacing for that matter) in order to **make writing/editing code easier**. Java also manages and interacts with the computer's **memory** for us (**instead of us having to do it ourselves**), allowing us to **store** data easily.

```
class Robot {
	Drivetrain drive;
	Arm scoringArm;
	
	void goBoom() {
		Boom = True;
  }
} 
```

## How is Java code organized?

Java employs very popular **code-organization** technique called **Object-Oriented-Programming**. In this type of programming we split our **actions** (like driving the robot) and **stored data** (like the position of our Joystick) among **classes** that are located in seperate **.java files**. The **stored data** in classes are called **fields**, and the **actions** are organized into **methods**. Classes **do not hold data or actions** themselves (unless you use a specific keyword that we will talk about later). Classes define **how** a **chunk of memory** should be **reserved** to **fit the fields and methods** that are described. You use classes to create **objects** which are essentially **chunks of memory** where you can **store data** and **do things with that data**. 

## How do we store things?

**Fields** (stored data) are decently easy to make. All you need to do is **define the class** that you will be using to reserve that *chunk of memory* and then **create a name** that you can use in your code to **reference** that object.

## How do we do things with those stored values?

## Basic Syntax and Convention

## Objects and Constructors

## The Console