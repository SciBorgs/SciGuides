# Introduction
## Prerequisites

- Comfortable with all of the [goals for Programming101](Programming101.md#goals).
- Comfortable with [command-line navigation](link)
- Comfortable with [git](link)
- Environment set up
	- [Code directory created](link)
	- [VSCode installed](link)
	- [Git & Github set up](link)
## Goals

Familiarity with the following topics:
- Java file structure and syntax
- Printing
- Types
- Operations, if statements, variables, loops, functions, and arrays in Java
	- Multi-dimensional arrays
## Best Practices

As always, follow the general [best practices](/projects/README.md#best-practices).

For this guide, you should be following along on your own computer. When there are pieces of example code, first think about out how the code works, and then try running it yourself. After each section, try to play around with the concepts you've learned! Make your own examples similar to the ones given.

There will be some practice problems, but not as consistently, so it's really important that you actually are following along, experimenting on your own, and just making sure you really understand what's happening.

And if you need help, ask!
# Setup

## Create GitHub Repo

A GitHub repository, often referred to as a "repo," is a central location where you can store, manage, track, and control changes to your project files. It's like a folder for your project that is hosted on GitHub's servers. It also allows you to easily share your code, or collaborate with others.

You're going to create a repo for the code that you write in this tutorial.
1. Open [GitHub](github.com) and log in.
2. Create a new repository
	- Click the '+' icon in the top-right corner of the page.
	- Select "New repository" from the dropdown menu.
3. Set up your repository
	- Choose a name for your repository (e.g., "Learning Java").
	- Add a brief description (optional).
	- Choose "Public" or "Private" for your repository visibility (if you choose Private, no one will be able to see it unless you explicitly add them).
		- You can always change this later
	- Check the box to "Initialize this repository with a README".
	- Press the ".gitignore template" dropdown under "Add .gitignore" and choose "Java"
	- Click "Create repository"
4. Clone the repository on your local machine
	- On your new repository's page, click the green "Code" button.
	- Copy the HTTPS URL provided.
	- Open Terminal for Mac/Linux, or PowerShell for Windows
	- Navigate to the directory where you want to store your project, and clone the repository:
```
cd path/to/your/code/folder
git clone HTTPS-LINK
```
Replace `path/to/your/code/folder` with the path to the directory you created for your code, and replace `HTTPS-LINK` with the URL you copied.
5. Verify the clone
	- Look at the contents of your code directory in Command Line and check that the new repository is there:
```
ls
```

## Open Repo in VSCode

1. Open VSCode
	- If you installed regular, non-WPILib VSCode, open that
2. Open the repository folder
	- In VSCode, go to File > Open Folder (or use the keyboard shortcut: Ctrl+K Ctrl+O on Windows/Linux, Cmd+O on Mac).
    - Navigate to the directory where you cloned your repository.
    - Select the repository folder and click "Select Folder" (or "Open" on Mac).

In the left sidebar, you should see the file explorer with your repository's files (README.md and .gitignore).
## Write README

A README file is a text file that introduces and explains a project.

Open your README.md file, and write a few words about what this project is. Some suggestions:
- Say that you're learning Java
- **Link to the [intro to programming readme](/projects/intro-to-programming/README.md)**
	- This README (like this guide) is written in Markdown, a simple language for formatting text. Here's how you embed a link in Markdown:
```
[text](link)
```

## Create java101 Directory

You will be using this repository for the remainder of the intro to programming series, so it will be helpful to have separate directories for each part. Make a new directory called `java101`. We will be working in that directory.

Inside of `java101`, make a new `README.md` file. In this README file, link [this guide](/projects/intro-to-programming/Java101.md).

Also in `java101`, make a file called `Main.java`.

You have two options for how to make these files:
1. Use the `touch` command
	1. Open Terminal or PowerShell (or open the VSCode version using Control + ~)
	2. Navigate to `java101` (if you're using VSCode CommandLine, you should start whatever folder you have open in VSCode)
	3. Make a new file called `Main.java`
2. Use the VSCode file explorer
	1. Right click in the file explorer on the left
	2. Select "New File"
	3. Name your file "Main.java"
## Set Up Main File

It's time to set up your first Java file!

Open `Main.java` in VSCode using the file explorer. Your file should either be empty or look something like this:
```java
public class Main {

}
```

If it's empty, copy the code in from here.

Put your curser on the line in between the two curly braces. Write "main" and then hit tab. Your file should end up looking like this:

```java
public class Main {
	public static void main(String[] args) {
	
	}
}
```

Above the words `public static void` you should see a little `Run | Debug`. You should be able to press on either word.
## Make Initial Commit

Now it's time to update your git repository with the changes you just made!

First off, open Terminal or PowerShell (in VSCode if you'd prefer). Navigate to your project directory (if you're in `java101`, do `cd ..`).

Then, type the following in:
```
git add .
git commit -m "added readme and main file"
git push
```

Okay, you're all set up!
# File Structure

At least at first, there are a lot of little things that you're going to be ignoring. I promise, we'll get to them later (mostly in [Java102](Java102.md)).

Here's the list of things you don't need to understand as of right now:
- what `public` means
- what `class` means
- what `static` means
- what `String[] args` means
- what the `public class Main { }` block is doing

Here's what you *do* need to know to get started:
- DO NOT DELETE ANYTHING that is currently there.
	- Do not delete any curly brackets. Do not delete `public class Main`. Leave it all.
- All code that you write will be inside of the outer pair of curly braces (in the `public class Main { }` block).
- The line `public static void main(String[] args] {}` is defining a function. I'm not going to explain the syntax yet, all you need to know is this:
	- When you press `Run`, the code written inside of that `main` function, between the open and closed curly braces will run. No other code will run unless called in the `main` function (or in a variable definition).
- Outside of the main function, you can create other functions and you can define variables (those are the only things you can do that are currently relevant).
- What you need to know about the order of definitions in your Java file:
	- Function definitions:
		- You can define functions in any order within the file.
		- A function can be called from anywhere in the file, even if it's defined below.
	- Variable definitions (for variables defined outside of functions):
		- Variables can be used in any function, regardless of where the variable and function are defined in the file.
		- When defining a variable `x`, you can only reference other variables inside the definition if they are defined *above* `x`.
# Java Syntax

A few key things to remember about Java syntax and style:
- There must be a semicolon at the end of each complete statement (i.e. returning a value, mutating a variable, calling a function, etc.) or declaration (i.e. defining a variable or function).
- Java uses curly braces (`{}`) to denote code blocks (unlike python which uses colons).
- In Java, variable and function names are written in [camelCase](https://en.wikipedia.org/wiki/Camel_case) with the first letter lowercase.
	- File names are written with the first letter capitalized.
# Printing

In Java, if you want to be able to see the result of a piece of code that you write, you need to print it. Whatever it is that you print will appear on the console as text.

*Note: printing is an example of a side effect*

If you try to print something that doesn't have an automatic conversion to text (i.e. an array), some combination of characters that represents that object but is illegible to you will appear. So be careful with what you print.

You can print by using the function `System.out.println()`. (In VSCode, you can also just write `sysout` and hit tab, and the rest should autocomplete).

So for instance, if you run this code:
```java
public class Main {
	public static void main(String[] args) {
		System.out.println("Hello World");
	}
}
```

This will appear on the console:
```
>> Hello World
```

Note, if you want to print raw text (like "Hello World"), *you must put quotation marks around the text*. When you do that, you mark the text as a String (the data type for raw text). If you do not put quotation marks, the computer will think that you are trying to refer to a symbol like a function or variable.
# Operations

Exactly the same as in [Programming101](Programming101.md#operations)!
# If Statements

Exactly the same as in [Programming101](Programming101.md#if-statements)!
# Types

Java is what is called a *statically typed* language (often just called *typed*). This is one of the biggest differences between Java and languages like Python and Javascript, which are dynamically typed (often called *untyped*).

This will impact your experience as a developer in two primary ways:
1. You will need to explicitly state the [data types](Programming101.md#data-types) of many values
2. Your computer will catch more bugs and you will get more informative error messages!

For right now, we're going to focus on the following data types:
- integers
- doubles
- booleans

The key words in Java that allow us to identify something as being of these types are `int`, `double`, and `boolean`.

So, when do we need to declare types? Essentially, types are required whenever you create something. So, when you make a new variable, you need to specify what type that variable is (even if the variable is created in the header of a for loop). And when you make a function, you must specify the return type (the type of the output) as well as the types of all inputs to the function.
# Variables

Here is the basic syntax for defining variables in Java:
```java
type name = value;
```

So, for example, if you wanted to create an integer called x with the value 6, you would write:
```java
int x = 6;
```

So what would you expect the following code to print? (First think it through on your own, and then you can run the code on your computer and check that the output is as you expected).
```java
public class Main {
	public static void main(String[] args) {
		int x = 6;
		System.out.println(x + 4);
		System.out.println(x);
		System.out.println(x % 2 == 0);
	}
}
```

For now, if you create a variable outside of a function, you need to put the word `static` before the type. I'm not going to explain what that means or why you need it yet, but we'll get there in [Java102](Java102.md). Here's an example:
```java
public class Main {
	static int x = 6;
	
	public static void main(String[] args) {
		System.out.println("x: " + x);
		// reassigning the value of x to be the old x plus 4
		x = x + 4;
		System.out.println("new x: " + x);
	}
}
```
# Arrays

One data type we did not talk about yet in this guide is an array. Unlike a boolean or integer or double, there are many different kinds of arrays. There can be an array of integers, of booleans, of doubles, etc. So if we were to declare the type of something as an array, that wouldn't really be enough information. Instead, the type of an array has to also include the type of the elements in the array.

Here's how we do that by taking the type of the elements and adding `[]` to the end. So the type of an array of doubles would be: `double[]`

Next, let's go over how we actually create arrays. There are two methods we can use.

The first is to explicitly initialize all the elements in the array. We do that using the following syntax:
```java
{element1, element2, element3}
```

Here's an example of using this method to create a 4 element double array:
```java
public class Main {
	static double[] arr = {4.5, 6, 9.0, 8};
	
	public static void main(String[] args) {
		// to find the length of an array, use array.length
		System.out.println(arr.length);
	}
}
```

The other option is to tell the computer to create an array with a specified number of elements. All elements will initially be the default value for that type. For ints and doubles, the default value is zero. For booleans the default is false. Then, if you want to change the values you can.

You can do this with the following syntax:
```java
new elementType[length]
```

The `new` keyword is what we use when we're telling the computer to create a new value of a certain type (there's more to this, but we'll get to that in [Java102](Java102.md)).

Here's an example of using this method to initialize a 100 element boolean array:

```java
public class Main {
	static boolean[] arr = new boolean[100];
	
	public static void main(String[] args) {
		System.out.println(arr[0]);
		// setting the 4th element in arr to true
		arr[3] = true;
		System.out.println(arr[0] || arr[3]);
		System.out.println(arr.length);
	}
}
```

## 2D Arrays

Just as we can have an array if booleans or integers or doubles or Strings, we can also have an array of arrays. We call such an array a 2d array.

So, let's say we want to represent a tic tac toe board. And let's say we've decided to represent blank, x ,and o with $0$, $1$, and $-1$ respectively. We could then represent each row as an integer array of length three. And to represent the entire board, we would use an array of three rows. So in the end, that's an array of length three, where each element is an integer array of length three.

In other words, we can represent a tic tac toe board as a 2 dimensional integer array.

We usually denote array types by taking the type of the element and adding `[]` to the end. That method works here as well.

The values in the outer array are of type `int[]`. So the final type of the board is `int[][]`.

And if we want to extract a value from the board, we can index the arrays just like we would a one dimensional array.

```java
public class Main {
	static int[][] board = new int[3][3];
	
	public static void main(String[] args) {
		// to start, let's extract the first row
		// (aka the first element in the array)
		int[] firstRow = board[0];
		// now, we'll get the first value in that row
		int firstVal = firstRow[0];
		System.out.println(firstVal);
	}
}
```

We did that in two steps - one to get the row, one to get the value. But we can also consolidate that into one step:

```java
public class Main {
	static int[][] board = new int[3][3];
	
	public static void main(String[] args) {
		int firstVal = board[0][0];
		System.out.println(firstVal);
	}
}
```

In general, we can index this board using `board[row][column]` where row and column are integers between $0$ and $3$ representing the row and column of the value we want to extract.

*Note: You can also have higher dimensional arrays (3D, 4D, 5D, etc).*
# Loops

The syntax for while loops is the same as in [Programming101](Programming101.md#while-loops):
```java
while (condition) {
	// code to run
}
```

The syntax for for-each loops is very similar to [Programming101](Programming101.md#for-each-loops):
```java
for (type element : collection) {
	// code to run for each element
}
```

There are two differences:
1. The type of `element` is declared. `element` is a variable that we are creating, so we must state its type.
2. I used the word `collection` instead of `array`. This is because there are other types of collections that you can iterate through in Java. In this guide we'll really only use arrays, but if you're ever using an `ArrayList`, `Set`, `Map`,  or other similar object, you can iterate through those using for each loops as well.

Here's a simple example of a for each loop in Java:
```java
public class Main {
	public static void main(String[] args) {
		int[] fib = {1, 1, 2, 3, 5, 8, 13};
		int sum = 0;
		for (int e : fib) {
			// add each element of fib to sum
			sum = sum + e;
		}
		System.out.println(sum);
	}
}
```
## For Loops

Java actually has a third kind of loop. It's called a for loop, but is more closely related to a while loop than a for each loop.

Let's start with an example of when you might want to use a for loop:

You want to create an array with 100 elements, where every element with an odd index has the value 1, and every element with an even index has the value 2. (Not that this particular scenario has any practical uses that I can think of).

Here's how you might do that with a while loop:
```java
public class Main {
	public static void main(String[] args) {
		int[] arr = new int[100];
		int index = 0;
		while (n < 100) {
			if (index % 2 == 0) {
				arr[index] = 2;
			} else {
				arr[index] = 1;
			}
			index = index + 1;
		}
	}
}
```

Alternatively:
```java
public class Main {
	public static void main(String[] args) {
		int[] arr = new int[100];
		int index = 0;
		while (index < 100) {
			arr[index] = 2 - index % 2;
		}
		index = index + 1;
	}
}
```

Let's examine these code examples. In both implementations, there are three parts of the code that define how the iteration works. These lines are all we need to know how many times the loop will run, and what the values of the variables it uses will be each time. Here are the lines:
1. 
```java
int index = 0;
```
2. 
```java
index < 100
```
3. 
```java
index = index + 1;
```

The first line creates the variable that we use for our iteration. The second line tells us how we use that variable to decide when the loop ends. The third line tells us how we update the variable each time we run the loop.

For loops are basically shorthand for this, allowing us to do all three of these things in the header of the loop. Here's the basic syntax:
```java
for (define variable; condition; code to update variable) {
	// code to run
}
```

Here's how we'd do the same thing we just did with a while loop, but using a for loop:
```java
public class Main {
	public static void main(String[] args) {
		int[] arr = new int[100];
		for (int index = 0; index < 100; index = index + 1) {
			arr[index] = 2 - index % 2;
		}
	}
}
```

In general, we use for loops when we want to iterate through a range of values in a predictable, consistent way. So, for instance, if we want to loop through all the indices of an array, or if we want to loop through the multiples of two below 1000.

Sometimes, we just have a piece of code that we want to run the exact same way some number of times, and we can use for loops for that as well. For instance, let's say we want to have a 9 by 9 grid of dashes that we can print. 

For this example, we're going to be working with [strings](Programming101.md#data-types), which we haven't done much of thus far. The key word for the string type is `String` (note the capital first letter). We'll get to why this type is capitalized when others in [Java102](Java102.md).

Before we get to the implementation, we need to introduce a few new things:
- String addition
	- For strings, we use the `+` operator for concatenation (the process of joining strings)
		- Example: `"hello " + "world"` &rarr; `"hello world"`
	- You can also take strings and add onto them values that are not strings. If you do that, the non-string values will be automatically converted into strings.
		- Example: `"the lowest prime number is " + 2` &rarr; `"the lowest prime number is 2"
- `"\n"`
	- This is the newline symbol. If there is `"\n"` in a string and you print that string, there will be an enter or a new line where that symbol is.
- `+=`
	- The `+=` operator is an assignment operator, allowing you to easily add to variables. It is shorthand for the following:
		- `x = x + 3` becomes `x += 3`
	- There are several other similar assignment operators (`-=`, `/=`, `%=`, `*=`) that can be used to easily adjust variables.
- `++`
	- The `++` operator is yet another assignment operator, and it is shorthand for increasing a variable by exactly 1.
		- Example: `x += 1` &rarr; `x++`
	- There is also a `--` operator that decreases a variable by 1.

```java
public class Main {
	public static void main(String[] args) {
		String s = "";
		for (int i = 0; i < 9; i++) {
			s += "- - - - - - - - -\n";
		}
		System.out.println(s);
	}
}
```
# Functions/Methods

Before we start learning Java functions, we have some vocabulary to go over.

In Java, what we've thus far been calling a function is actually called a method. For now, we will use the terms interchangeably. In [Java102](Java102.md), we will flesh out the differences between functions and methods.

Okay, let's get started! Here's a simplified version of the basic syntax for functions/methods in Java (later on we'll learn about situations where this doesn't apply):
```java
static returnType name(argumentType argumentName) {
	// code to run
	return // value to return
}
```

Some things to note:
1. For now, you must have the word `static` in front of your functions (we'll get to why in [Java102](Java102.md)).
2. You must specify the return type (the data type of the return value) of your function.
3. You must specify the type of each argument that your function takes

Here's how we would write a function analogous to this mathematical function: $f(x) = 2x$

```java
static double f(double x) {
	return 2 * x;
}
```

Then you can test the function by calling it in the main function and printing the result:

```java
public static void main(String[] args) {
	System.out.println("f(3): " + f(x));
}
```

But if you have to specify the return type, what do you do if you want to write a function that doesn't return anything? Well, instead of a return type you use a key word that means no return type: `void`

As an example, let's write a function that prints an integer array in a readable format:

```java
static void printIntArray(int[] arr) {
	String str = "(";
	for (int i = 0; i < arr.length; i++) {
		str += arr[i];
		if (i != arr.length - 1) {
			str += ", ";
		}
	}
	str += ")";
	System.out.println(str);
}
```

Go through this line by line until you understand what's happening. Once you've done that, test it out on a few arrays!

Now, like many functions that use side effects, this isn't necessarily the best way to accomplish our goal. Instead of having a function that returns nothing and prints the array, we could have a function that returns the string form of the array, and we could print that ourselves, like this:

```java
static String intArrToString(int[] arr) {
	String str = "(";
	for (int i = 0; i < arr.length; i++) {
		str += arr[i];
		if (i != arr.length - 1) {
			str += ", ";
		}
	}
	return str + ")";
}
```

```java
public static void main(String[] args) {
	int[] arr = {1, 4, 6, 9};
	System.out.println(intArrToString(arr));
}
```

This would allow us to build on our function in the future. For instance, let's say we wanted to be able to print a 2d int array (like our tic tac toe board), we could do the following:

```java
static String boardToString(int[][] board) {
	String str = "";
	for (int i = 0; i < board.length; i++) {
		str += intArrToString(board[i]);
		if (i != board.length - 1) {
			str += "\n";
		}
	}
	return str;
}
```
## Practice Problems

Before you start, let's do some setup. Make a new file called something like `PracticeProblems.java`. The file should look something like this:
```java
public class PracticeProblems {
	
}
```

Write all your functions inside `PracticeProblems`. To test them, go back to your `Main.java` file and run your tests from the `main` function. You can call a function `f` in `PracticeProblems` using `PracticeProblems.f()`. Here's an example:
```java
public class Main {
	public static void main(String[] args) {
		int[] arr = {4, 3, 2, 8, 3};
		System.out.println(PracticeProblems.countOccurances(arr, 3));
	}
}
```

**Important**: Whenever you get to a stopping point (solve a problem, close your computer to take a break) save your changes by committing and pushing!
```
git add .
git commit -m "description of what you did"
git push
```
## Problems
1. Write a function called `countOccurrences` that takes an integer array `arr` and an integer `n`, and returns the number of times that `n` appears in `arr`.
2. Write a function called `reverseArray` that takes an integer array `arr` and returns a new array with the elements of `arr` but in reverse order.
3. Write a function called `sumGrid` that takes a 2d double array `grid` and returns the sum of all the elements. *Hint: you can do this with nested for loops (look up what that is).*
4. Write a function called `fib` that takes an integer `n` and returns the `nth` number in the fibonacci sequence (starting with $0$ $1$).