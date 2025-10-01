# Java 101

Hello! This guide will serve as an **introduction** to **the Java programming language**.

Here is what will be covered here:

1. **[What is a program?](#what-is-a-program)**
2. **[What is Java?](#what-is-java)**
3. **[How is Java code organized?](#how-is-java-code-organized)**
4. **[How do we store things?](#how-do-we-store-things)**
5. **[How do we do things with those stored values?](#how-do-we-do-things-with-those-stored-values)**
6. **[Basic Syntax and Convention](#basic-syntax-and-convention)**
7. **[Primitives and the Main Class](#primitives-and-the-main-class)**
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

Java employs very popular **code-organization** technique called **Object-Oriented-Programming**. In this type of programming we split our **actions** (like driving the robot) and **stored data** (like the position of our Joystick) among **classes** that are located in seperate **.java files**. 

>In Java (unlike trash python), EVERYTHING is an Object. EVERYTHING is inside something else (unless it's the **main class**). EVERYWHERE YOU LOOK is just *objects inside objects inside objects*...

**Stored data** in classes are called **fields**. **Actions** are organized into **methods**. Classes **do not hold these things** themselves (unless you use a specific keyword that we will talk about later). Classes define **how** a **chunk of memory** on your computer should be **reserved** to fit these things (there is the memory management I was talking about earlier). You use classes to create **objects** which are essentially **chunks of memory** where you can **store data** and **do things with that data**. 

>In the Sciborgs code, we have a **Robot** class and classes for **each subsystem**!

## How do we store things?

**Fields** (places where you can store data) are decently easy to make. All you need to do is **define the class** that you will be using to reserve that *chunk of memory*; and then **create a name** that you can use in your code to **reference** that object. You also have the ability to manage **where** fields can be accessed from in the program by adding certain **keywords** to the front of them.

```
Number num = 67;
Robot.setSpeed(num);
```

> Number is a **class**, 'num' is the **name of the field**, and 67 is the **value of the field**. 'setSpeed' is a **method**.

## How do we do things with those stored values?

**Methods** (actions that you can do on data) are also decently easy to make. Methods are special in that you can run them **with parameters** (data that you give the method as you run it) and **get an output** (data that the method spits out) from it. 

> **For Example:** I can have a method that blows up the robot with an **input** of time (till the robot blows up) and an **output** of whether or not the explosion was successful.

All you need to do to make a method is 
1. **Create a name for your method** (like 'blowUpRobot' or 'startMatch')
2. **Define the class of the output** (in order to **reserve space** for that output)
3. **Define the class of the input** (you can't really do much with 10111100110)
4. **Create names for all of the inputs** (so that you can use them in the method itself).

Methods **do not** have to output anything, not do they have to have **inputs**. 
>In these cases, you would switch out the output class with the **void** keyword. 

Inside methods, you can do a couple of things:
1. You can create **temporary objects** called **variables**. 
2. You can **run other methods** that are in your fields/variables. 
3. You can use **logic** (such as if-then statements) to make decisions. 
4. You can use the **return** keyword to end the method and **output** stuff. 

When you are **calling** a method that **has an output**, you can treat your method exactly the same as **any other form of stored data** (fields or variables).

> **For example:** If I had a method called **twoPlusOne** which returns **3** (Yes, this is a completly pointless thing to do but bear with me); The statement **twoPlusOne() - 4** is a completly valid math expression (that will return -1).

This is also why you need to define the output's **class**, since you need to  **reserve a space in memory** for the output to exist. 

>You do this by putting the **output class** before the **name**.

You need classes for inputs because your program can't really understand the jumble of 1's and 0's otherwise. When you **specify the class**, those 1's and 0's become actually readable **fields and methods**. 

>You put your **inputs** (along with their types) **inside the parantheses**.

You also have the ability to manage **where** methods can be accessed from in the program by adding certain **keywords** to the front of them (just like in fields).

>You put these keywords **before** the output-class.

```
public Number zeroer(Number input) {
	if (input == 67) {
		input = 0;
	} else {
		input = input + 1;
	}

	return 0;
}
```

## Basic Syntax and Convention

Here are some rules for **Java Syntax**: 

```
// Double Slashes create Comments! (these aren't part of the code)
End all of your statements with Semicolons;
{Wrap classes, methods, and the insides of logic statements in CurlyBraces}
(Wrap all method inputs and logic inputs in parenthesis)
DoNotIncludeSpacesInYourNames (Java can't handle it)

For Fields (Access refers to keywords such as public or private):
[Access] [Belonging] [Class] [Name] = [Value];

For Methods (make sure to seperate multiple inputs with commas):
[Access] [Belonging] [Class] [Name] ([Input Class] [Input Name]) {[Action]}

```

## Primitives and the Main Class

Java is all about objects inside objects inside objects. However, this does not go on forever.

## Objects and Constructors

## The Console