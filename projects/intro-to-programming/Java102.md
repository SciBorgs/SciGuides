# Introduction

## Prerequisites

- Comfortable with all of the [goals for Java101](Java101.md#goals).
- Comfortable with [command-line navigation](link)
- Environment set up
	- [Code directory created](link)
	- [VSCode installed](link)
	- [Git & Github set up](link)
## Goals

Familiarity with the following concepts:
- Classes and Objects
	- fields
	- constructors
	- methods
	- static
	- public/private
- Polymorphism
	- Interfaces
	- Generics
	- Inheritance
- Functional Interfaces
- Streams
## Best Practices

See [Java101](Java101.md#best-practices).
## Setup

If you did [Java101](Java101.md), use the same repository that you used there. Otherwise, follow the [instructions in Java101 to set up a repository](Java101.md#setup).

Make another directory called `java102`. We'll be working in that directory. Make a file in java102 called `Main.java`, as well as a `README.md` file.

In the README, link [this guide](/projects/intro-to-programming/java102).
# Classes and Objects

## Objects

An *object* in Java is a bundle of related data and functions that work together to perform specific tasks in a program. Think of it as a custom-built tool that combines information ([fields](#glossary)) and actions ([methods](#glossary)) into a single unit.

For example, if you're planning the trajectory of a robot through a 2d plane, you might have a Point object. This object would store the x and y coordinates of the point, and would have one method to translate a Point in the x direction, and one to translate it in the y direction.
## Classes

In Java, a class is like a blueprint or template for creating objects. It defines what data and methods the objects will have. An object is an instance of a class - a specific realization of that blueprint. Classes can also hold what are called *static* methods or fields that are related to objects of that class, but that don't actually belong to individual objects. For example, a `Point` class might have a method that finds the distance between two `Point` objects.

A class can also be thought of as the [type](Java101.md) of an object. So if you were to make a point variable, the type of that variable would be `Point`. In fact, some of the types that we've been using are object types (specifically Strings and arrays -- although arrays are a special case). Generally, whenever there is a type that is capitalized, that is an object type.
## Point

Let's write out the class that is a blueprint for the `Point` object that we described:

First off, create a new file called `Point.java`. The contents should look like this:

```java
public class Point {

}
```
### Fields

Next, we'll declare the fields that will store data for the object. We want to store the x and y coordinates, both of which are doubles. We do this similarly to how we declared variables in [Java101](Java101.md#variables), but with a couple differences:
- We will not use the word `static`, because these fields belong to individual points.
- We will write `public final` before the type and name of each field.
	- We'll come back to the meaning of `public` in [Java103: Tic Tac Toe](/projects/intro-to-programming/tic-tac-toe).
	- Adding `final` before a variable ensures that that once initialized, a variable cannot be mutated. In this case, the x and y coordinates of a point should never change. If they did, we would no longer be talking about the same point, and that would get very confusing.
- We will *declare* our variables without *initializing* them. 
	- In other words, we will write the names and types of the variables, indicating that they exist and allowing us to reference them in other parts of the code. (This is called declaring a variable.)
	- But we will not give them values (also called initializing variables). Instead, each instance of the `Point` class (each `Point` object) will have its own values for `x` and `y`.

```java
public class Point {
	public final double x;
	public final double y;
}
```
### Constructor

Okay, we have now declared fields to store the x and y coordinates of our points.

Next up, we need to write what's called a *constructor*. A constructor is a special kind of function that creates an object. Each class has a constructor, and that constructor is called to generate a new object instance of that class. If there's anything about an object that you want to be different for each object, you generally do that in the constructor. 

So, in this case, we want each `Point` to have its own values for `x` and `y`, and we want whoever makes the `Point` to be able to decide those values. We can do that by having the constructor take `x` and `y` values as arguments (or inputs).

The syntax for writing constructors somewhat similar to how we wrote functions in [Java101](Java101.md#functions/methods). Here are the differences:
- We won't use the word `static` (again, this belongs to a particular `Point`).
- We will add the word `public`.
- We will not specify a return type (this is because the return type of a constructor is always going to be the type of the object, in this case a `Point`).
- The name of the constructor is always the same as the name of the class (so `Point`).
- We don't need to return anything. A new `Point` is automatically created and then returned.

Here we go:

```java
public class Point {
	public final double x;
	public final double y;

	public Point(double x, double y) {
		this.x = x;
		this.y = y;
	}
}
```

The one thing in the constructor that we haven't explained yet is the keyword `this`. The `this` keyword is used to refer to the top level scope of a particular object (the object scope). All non-static fields and methods are part of that scope. So when the constructor says `this.x`, it is referring to its `x` field. When the constructor just says `x`, however, without the `this`, it is referring to the argument `x` that was passed into the constructor. That `x` was declared more recently, so, as we discussed in Programming101 (link), it will by default shadow the top level field `x`.

This means that when the constructor has `this.x = x`, the first `x` refers to the field, and the second `x` refers to the argument. So it is setting the value of the field `x` to be whatever value for `x` was passed into the constructor as an argument (and the same with `y`).

So now we have a way to create a new `Point` object. Let's try it out! Go back to your main file, and add the following inside of the `main` function:

```java
Point point = new Point(4, 3);
```

The keyword `new` is always used before calling a constructor to create a new object (remember arrays -- add link). We passed into the constructor 4 and 3, so the coordinates of our point should be (4, 3). Let's check! We can access the fields of an object by using the notation `object.field`:

```java
System.out.println("x: " + point.x + "y: " + point.y);
```

Run the code, and see if the values that are printed are what you expect!
### Translation

Now, go back to the `Point.java` file. We're going to write a method to translate a point in the x direction. We'll do this just like we defined functions in [Java101](Java101.md#functions/methods), with the following changes:
- We won't use the word `static` because this method belongs to each particular `Point`.
	- In other words, each `Point` not only has its own values of `x` and `y`, but also its own methods for translation that use its values of `x` and `y`.
- We will add the word `public` (we'll explain this later).

Let's call this method `translateX`. This is a method that belongs to the `Point` class, so it already has access to the data stored in the object (`x` and `y`). The only other input that it needs is how much to translate by. We'll call that value `t`.

The return type of `translateX` will be a new `Point`, because it is returning the point that will result after a translation.

```java
public class Point {
	public final double x;
	public final double y;

	public Point(double x, double y) {
		this.x = x;
		this.y = y;
	}
	
	public Point translateX(double t) {
		return new Point(x + t, y);
	}
}
```

We can also add a method to translate in the y direction:

```java
public class Point {
	public final double x;
	public final double y;

	public Point(double x, double y) {
		this.x = x;
		this.y = y;
	}
	
	public Point translateX(double t) {
		return new Point(x + t, y);
	}
	
	public Point translateY(double t) {
		return new Point(x, y + t);
	}
}
```

Okay, let's test our our new methods! Go back to `Main.java`. Inside the `main` function, we're going to reflect `point` a few times.

```java
Point xTranslation = point.translateX(3); // should be (7, 3)
Point yTranslation = point.translateY(-7); // should be (4, -4)
Point xyTranslation = point.translateX(-4).translateY(-3); // should be (0, 0)
```

Now that we have the lots of translations, let's print out the x and y values of our new points to check that they're correct.

```java
System.out.println("x transl: (" + xTranslation.x + ", " + xTranslation.y + ")");
System.out.println("y transl: (" + yTranslation.x + ", " + yTranslation.y + ")");
System.out.println("xy transl: (" + xyTranslation.x + ", " + xyTranslation.y + ")");
```

You can run the code and make sure the values are what you expected.
### ToString

One thing you might notice is that the code we wrote to print out our points is pretty repetitive. We wrote essentially the same thing 3 times, but we used different variables. Usually, when you're writing repetitive code, there's a more efficient option. In this case, we're going to add a `toString` method.

A `toString` method tells the computer how to convert an object into a `String`. When you write `System.out.println(object)`, that object is automatically converted to a string and printed using its toString method. 

Each object has a default `toString` method. Let's try to print a `Point` using its default `toString` method and see what happens:

```java
System.out.println("point: " + point);
```

You should see something like this: `point: Point@15db9742` (the sequence of letters and numbers after the @ may be different).

That isn't a particularly helpful representation of a `Point`. What we actually want is something that tells us the `x` and `y` coordinates of the point. So we're going to override the default `toString` method to do that (we'll get into what overriding really means later on). Go back to `Point.java`.

```java
public class Point {
	public final double x;
	public final double y;

	public Point(double x, double y) {
		this.x = x;
		this.y = y;
	}
	
	public Point translateX(double t) {
		return new Point(x + t, y);
	}
	
	public Point translateY(double t) {
		return new Point(x, y + t);
	}

	@Override
	public String toString() {
		return "(" + x + ", " + y + ")";
	}
}
```

Now, we can simplify our code in `Main.java`! Instead of printing reflected points like this:

```java
System.out.println("x transl: (" + xTranslation.x + ", " + xTranslation.y + ")");
System.out.println("y transl: (" + yTranslation.x + ", " + yTranslation.y + ")");
System.out.println("xy transl: (" + xyTranslation.x + ", " + xyTranslation.y + ")");
```

We can do this:

```java
System.out.println("x transl: " + xTranslation);
System.out.println("y transl: " + yTranslation);
System.out.println("xy transl: " + xyTranslation);
```

### Distance

Okay, now that we've done that, let's add one last thing to our `Point` class: a method to find the distance between two points. We'll call it `distance`.

This `distance` method is going to take two `Point` objects and find the distance between them. Remember, the `distance` method will belong to the `Point` class as a whole, not to particular `Point` objects. It will be a `static` method.

*note: We used the static keyword when we were writing functions and variables in the `Main` class, because nothing we were writing was meant to be specific to instances of the `Main` class (in fact, we never created instances of that class).*

One last thing before we write our distance function: We're going to be using `Math.sqrt`, which takes the square root of a double, and `Math.pow`, which is how we calculate exponents (`Math.pow(a, b)` &rarr; $a ^ b$).

```java
public class Point {
	public final double x;
	public final double y;

	public Point(double x, double y) {
		this.x = x;
		this.y = y;
	}
	
	public Point translateX(double t) {
		return new Point(x + t, y);
	}
	
	public Point translateY(double t) {
		return new Point(x, y + t);
	}

	@Override
	public String toString() {
		return "(" + x + ", " + y + ")";
	}

	public static double distance(Point p1, Point p2) {
		return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
	}
}
```

Now let's test out the new distance function! Open `Main.java`. In the main function, create two points, `a` and `b`.

We access non-static members of a class with `object.member`. So for instance, to translate point `p`, we'd call `p.translate`. But static members don't belong to specific objects, they belong to classes. So instead, we use `Class.member`. In this case, that would be `Point.distance`. Run the following line of code and double check it with your own calculations!

```java
System.out.println(Point.distance(a, b));
```
### Practice: Center of Mass

Let's say we have a bunch of points, each of which represents a point mass of equal mass. The *center of mass* of those points is the average position of the points. So the x coordinate of the center of mass is the average of all of the x coordinates of the points, and the y coordinate is the average of all of the y coordinates.

Write a static method for the `Point` class that takes as an argument an array of `Point` objects, and returns the center of mass, as a `Point`. Here's the header (there will be a ; at the end, but when you actually write it there should be curly braces instead):

```java
public static Point centerOfMass(Point[] points);
```

When you're done, test our your new function with some simple examples!

Also, if you haven't yet, now would be a great time to commit and push your changes.

### Practice: Angle

Write a non-static method that calculates and returns the angle in degrees between a point and the positive x axis. Or more specifically, the angle of point p is the angle from the positive x axis to the line that goes through the origin and point p. Counterclockwise is positive. 

This will require trigonometry. If you're not familiar with basic trig, look at [this doc](Trigonometry.md).

You can look up how to perform trigonometric functions in Java (the Java trig functions generally operate in radians, so you'll need to use `Math.toDegrees` and `Math.toRadians` to make sure you're being consistent about units).

Also, be careful to think about all the cases! This should work in all four quadrants.

Here's the header:

```java
public double angle();
```
### Challenge: Rotation

As a challenge, try to write a method that rotates a point by `theta` degrees. To think about what this means, imagine a circle centered around the origin of a plane that passes through point p. The rotation of point p by positive 30 degrees is another point on that circle, but the angle between this new point and the positive x axis should be 30 degrees bigger than the angle between p and the positive x axis.

Making a generalized form of this function will require trig. But first, try making a method that just rotates a point by 90 degrees counterclockwise:

```java
public Point rotate90();
```

Once you've written and tested that, try a general rotate method:

```java
public Point rotate(double theta);
```
# Polymorphism

Polymorphism is a concept in programming that means "many shapes" or "many forms." It refers to the idea that single thing (like a piece of code) can behave differently depending on how it's used. It allows a single function or operation or class or structure to work with different types of data, making programs more flexible and easier to manage.

Think of it like how a tool like a wrench can work on different sizes of nuts and bolts. The wrench is one tool, but it can adjust to different tasks. Similarly, polymorphism lets code adjust and work in different situations without needing to be rewritten.

In Java, there are several forms of polymorphism that we're going to talk about.
## Generics

Generics are a form of what's called *parametric polymorphism*. They are perhaps the simplest polymorphism in Java - and you've actually already seen them used in several places.

Generics allows you to write classes and methods that can work with any data type while maintaining type safety. For example, an array uses generics so that it can store any type of object—`Integer`, `String`, `Boolean` etc—instead of having a separate class for each type of array.

Something to note: I used the capital words for each of those types. That's because generics must be object types. Non-capitalized types (i.e. int, boolean, etc) are not object types. Instead they are *primitives* (look it up if you're interested). But each of them does have a corresponding object type, so those are what we use for cases like this.
### ArrayLists

Now, arrays are somewhat of a special case, and there are actually several differences between generics in arrays and other generics.

So instead of talking about arrays, let's talk about ArrayLists. An `ArrayList` is similar to an array, but without a fixed length. So you can add new elements to an `ArrayList`.

Here's how that works: an `ArrayList` stores its values in an `Array` that is longer than the length of the `ArrayList` (so if there are 5 elements in the `ArrayList`, those elements might be stored in the first 5 spots of a 10 element `Array`). When you add an element to the `ArrayList`,  it populates the next spot. If you keep adding elements, the `Array` eventually becomes full. At that point, if you try to add another element, the `ArrayList` will create a new `Array` with 1.5 times the size of the old array (i.e. from 10 to 15), and copy all the elements from the old `Array` to the new one.

Let's look at how we would make an `ArrayList` of strings in the `main` method of our `Main.java` file:

```java
ArrayList<String> arr = new ArrayList<>();
```

So starting from the beginning of the line, the type for this variable is `ArrayList<String>`.  Inside the `ArrayList` class, the type of the element is not specified. It could be a `String` or an `Integer` or an `ArrayList` or a `double[]`, and whichever one it is, the `ArrayList` functions the same way. So when we make a new `ArrayList`, that's when we specify what the type of the elements are. The triangle brackets are the syntax in Java for doing that. So the type is `ArrayList<String>`, because it's an `ArrayList` with elements of type `String`.

After the assignment operator (=), we create a new `ArrayList` using the class's constructor. The square brackets are there as well because the constructor also needs to know the type of the elements. In this particular case, we don't need to actually put the type in there because we already specified the type earlier, so the computer can infer that the same type (`String`) applies to the constructor as well. If we weren't saving the `ArrayList` as a variable (and therefore specifying its type), we would have to specify in the constructor: `new ArrayList<String>()`. The `ArrayList` starts out with 0 elements.

We can (but do not have to) pass in an integer to the constructor. That integer sets not the initial size of the `ArrayList`, but instead the initial size of the `Array` in the `ArrayList`. This isn't typically something that will be necessary, but if you're creating an `ArrayList` and you know how long it's going to be, you might as well give that to the constructor.

Now that we have our ArrayList `arr`, let's do something with it! We can get values from an ArrayList using the `get` method that takes an index. We can set values using `set` which takes an index and the value to set. We can see how many values are currently there using the `size` method. And we can add values by using the `add` method which takes a value to add.

Oh, and unlike arrays, `ArrayLists` have `toString` methods that actually let us see the elements!

Okay, let's build up `arr`:

```java
arr.add("Hello");
arr.add("World");
System.out.println(arr);
arr.set(0, "Goodbye");
System.out.println(arr);
```

Now let's make another array:

```java
ArrayList<Boolean> conditions = new ArrayList<>();
conditions.add(true);
conditions.add(arr.get(0) == "Hello");
conditions.add(conditions.get(0) || conditions.get(1));
```

Try to figure out what each of the three elements of `conditions` should be. Then print out `conditions` and check that you were right!

Now let's make an Integer ArrayList with 50 elements, all of which are 0:

```java
ArrayList<Integer> intArr = new ArrayList<>();
for (int i = 0; i < 50; i++) {
	intArr.add(0);
}
System.out.println(intArr.size());
System.out.println(intArr.get(32));
```
### Grid

Now that we've used the generics in the context of `ArrayLists`, let's try making our own class that uses generics.

 Specifically, we're going to make a `Grid` class. Each `Grid` will represent a square grid of objects. We will be able to access and change each object in a `Grid`, as well as convert a `Grid` into a string. And all of this will work regardless of what kind of object each `Grid` contains - we could have one String `Grid` and one Integer `Grid` and one Boolean `Grid`, and they would all work.

We're going to store our grids as `ArrayLists` because using generic types with arrays gets complicated. 

Okay, so here's how we'd make our grid class:

```java
import java.util.ArrayList;

public class Grid<T> {
	private final ArrayList<ArrayList<T>> grid;
	public final int sideLength;

	public Grid(int sideLength, T defaultVal) {
		this.sideLength = sideLength;
		this.grid = new ArrayList<ArrayList<T>>(sideLength);
		for (int i = 0; i < sideLength; i++) {
			grid.add(new ArrayList<>(sideLength));
			for (int j = 0; j < sideLength; j++) {
				grid.get(i).add(defaultVal);
			}
		}
	}

	public T get(int row, int col) {
		return grid.get(row).get(col);
	}

	public void set(int row, int col, T val) {
		grid.get(row).set(col, val);
	}

	@Override
	public String toString() {
		String str = "";
		for (ArrayList<T> row : grid) {
			for (T element : row) {
				str += element + " ";
			}
			str += "\n";
		}
		return str;
	}
}
```

Okay, let's go through this step by step:

___

At the very top, above the class declaration, we have this line:

```java
import java.util.ArrayList;
```

Unlike Strings and Integers and all of the Math functions we've used, to use an ArrayList you need to import it. The definition of the `ArrayList` class is not accessible unless you do that, so you won't be able to use it.

___

The name of the class is not written simply as `Grid`, but as `Grid<T>`.  That indicates that this class uses a generic type called `T`. Within this class, whenever `T` is used, it is referring to the same unspecified type. When someone creates a new `Grid`, they will specify what type of `Grid` it is. If it is a string Grid, or a `Grid<String>`, then for that particular `Grid`, the type `T` will be `String`.

___

The `Grid` class has two fields: `grid` and `sideLength`. `sideLength` is simply the length of the grid (the number of values in each row and column). 

`grid`, on the other hand, actually stores the grid and its elements. Its type is `ArrayList<ArrayList<T>>` because the grid is represented by a 2D arraylist, and the elements of the grid are of course of type `T`.

A couple of things you may have noticed about `grid`: 

___

First off, I said at some point that the keyword `final` prevents variables or fields from being mutated. But `grid` is a final variable, and yet we mutate its values in the `set` method. What gives? Well, `final` variables cannot be reassigned to totally new values. If, however, the value of a `final` variable is an object that can be mutated, you *can* mutate the object. So if you have `final int[] arr = new int[4]`, you cannot then say `arr = {4, 3, 2}`, but you *can* say `arr[2] = 7`. And the same thing goes with a final `ArrayList` variable. You can't reassign the variable, but you can set values in the list.

So, when we say that `grid` is `final`, all that does is prevent anyone from reassigning `grid` to an entirely new `ArrayList`.

___

The other thing you may have noticed is that I used the keyword `private` here for the first time. Thus far, we have only used `public`.

The keywords `private` and `public` describe who is able to see and interact with different members of a class. Anything `public` can be accessed directly by anyone. Anything `private` can only accessed directly by other members of the class.

In `Point`, (LINK) our coordinates were `public`, so anyone could access them (i.e. in `Main.java` we were not inside of the `Point` class, but we were still able to access `point.x` and `point.y`). They were also `final`, which is important. An integer that is `public` and `final` can be seen by anyone, but it cannot be changed by anyone. If the coordinates were just `public` and not `final`, anyone would be able to see *and change* them. We would be able to, in `Main.java`, write `point.x = 1` and that would change the `x` value of `point` to be 1.

All of our methods have also been public, which is what allows us to call them in `Main.java`.

In our `Grid` class, we do want anyone to be able to see the values in our `grid` and set new values, so why would we make the `grid` a `private` field? Well, while we are okay with people setting values of the grid, we would not be okay with someone adding values or resetting an entire row. If `grid` was a `public final` variable, and we had a `Grid` object called `g`, we would be able to do both of those things:
1. Adding new rows/columns
```java
g.grid.add(new ArrayList<T>);
```
2. Resetting an entire row
```java
g.grid.set(0, new ArrayList<T>());
```

Generally, when you only want people to be able to interact with field in specific ways (i.e. see or change individual entries in a 2D ArrayList), it is best to make that thing field `private` and have all interactions with it happen through `public` methods.

___

Okay, next up, let's look at the constructor. All the constructor takes is a side length and a default value. Then it sets the sideLength field and generates the grid.

To start, it sets `grid` to a blank `ArrayList`. Then, it loops through the integers `i` from 0 to the `sideLength`, and for each value of `i` it adds another row to `grid` (that way in the end the number of rows is `sideLength`). Each row that it adds starts out as another blank `ArrayList`, but by using another for loop each row is populated with the `defaultValue`. The end result is a 2D `ArrayList` whose dimensions are `sideLength` by `sideLength`, and for which each element is `defaultValue`.

___

Now let's turn to the methods. Since `grid` is `private`, we need to make methods to access and change the elements in `grid`, which is why we have `get` and `set`. We also have a `toString` so that we can print a `Grid` and be able to see its values. Note however that if type `T` has an unhelpful default `toString` method (like with arrays), this won't be especially helpful.

Look through the three methods and make sure you understand everything that's happening.

___

It's time to test out our `Grid` class! Open `Main.java`. Write the following in the `main` function to make a new grid of integers:

```java
Grid<Integer> grid = new Grid<>(5, 0);
grid.set(2, 2, 4);
System.out.println(grid);
```

### Generics in methods: printArray

You can also have generics at the individual method scope. So, for instance, if you want a method that prints out all the values in an array, you want that to work generically, regardless of what type of array the method is given. Of course, one option would be to just write that method inside of the `Array` class, because everything inside the `Array` class has access to the generic type of the elements of the array. But that's not possible, both because we don't have access to that class and because arrays really are a special case.

So instead we're going to write a method `arrayToString` inside of `Main`. Instead of taking a specific kind of array, we're going to take a `T[]`, where `T` will represent whatever the type is of the elements of the array that is passed into our method.

Here's how we can do that:

```java
static <T> String arrayToString(T[] arr) {
    String str = "[";
    for (int i = 0; i < arr.length - 1; i++) {
		str += arr[i] + ", ";
    }
    return str + arr[arr.length - 1] + "]";
}
```

The key thing here is the `<T>` that comes before the return type. That says that for this function, we're going to be using some type `T`. The actual value of that type is determined anew each time the function is called (if it is called with a `String[]`, `T` is `String`).

Test this out with some arrays!
### Practice: Diagonal

Create a non-static method in `Grid` called `diagonal` that returns an `ArrayList` with the primary diagonal of the grid (from top left to bottom right). Here's the header:

```java
public ArrayList<T> diagonal();
```

### Practice: maxSideLength

Create a static method inside of `Grid` that returns the biggest `sideLength` of any `Grid` that's been made.

*Hint: use a static field to keep track of the current maximum, and update the maximum in the constructor.*

Here's the header:

```java
public static int maxSideLength();
```
## Interfaces

Interfaces are a form of *subtype polymorphism*. Before I explain what interfaces are, let's build up a scenario in which you might want to use them.
### Circle

We're going to make a `Circle` class. It'll be simple: just a center and a radius, and some methods to get basic values like its area or to do basic transformations.

```java
public class Circle {
	public final Point center;
	public final double radius;

	public Circle(Point center, double radius) {
		this.center = center;
		this.radius = radius;
	}

	public double area() {
		return Math.PI * Math.pow(radius, 2);
	}

	public double perimeter() {
		return 2 * Math.PI * radius;
	}

	/** 
	* @return Whether point p is inside of the circle.
	*/
	public boolean isInside(Point p) {
		return Point.distance(center, p) < radius;
	}

	/** 
	* @return Whether point p part of/on the border of the circle.
	*/
	public boolean isOn(Point p) {
		return Point.distance(center, p) == radius;
	}

	/** 
	* @param x How much to translate the circle by in the + x direction.
	* @param y How much to translate the circle by in the + y direction.
	* @return The circle that results from the translation.
	*/
	public Circle translate(double x, double y) {
		return new Circle(center.translateX(x).translateY(y), radius);
	}

	/** 
	* @return The circle that results from scaling by k.
	*/
	public Circle scale(double k) {
		return new Circle(center, radius * k);
	}

	@Override
	public String toString() {
		return "(center: " + center + "; radius: " + radius + ")";
	}
}
```

You may notice that I used a kind of comment that I haven't used before. These are called javadoc comments, and they're a great way to add commentary explaining how your methods work. When you're calling these methods from `Main` and you hover over the names of the methods, you should see the comments.

Go back to you `Main` file and play around with this class a little bit. Make some circles, get their areas, check if certain points are on or inside of the circles, make transformations.
### Square

Now we're going to make a `Square` class. Instead of a center and a radius, it will have the bottom left corner and the side length. (The sides of the square are necessarily parallel to the x and y axes). `Square` will have all of the same methods as `Circle`, as well as a method that returns an array of the corners. I will write some of the methods for you, and leave some blank for you to write.

```java
public class Square {
	public final Point corner;
	public final double sideLength;

	/**
	* @param corner The bottom left corner of the square
	* @param sideLength
	*/
	public Square(Point corner, double sideLength) {
		this.corner = corner;
		this.sideLength = sideLength;
	}

	public double area() {
		// write this
	}
	
	public double perimeter() {
		// write this
	}
	
	/** 
	* @return Whether point p is inside of the square.
	*/
	public boolean isInside(Point p) {
		double xDist = p.x - corner.x;
		double yDist = p.y - corner.y;
		return 0 < xDist && xDist < sideLength &&
			   0 < yDist && yDist < sideLength;
	}

	/** 
	* @return Whether point p part of/on the border of the square.
	*/
	public boolean isOn(Point p) {
		// write this
	}
	
	/** 
	* @param x How much to translate the sqaure by in the + x direction.
	* @param y How much to translate the squarer by in the + y direction.
	* @return The sqaure that results from the translation.
	*/
	public Square translate(double x, double y) {
		// write this
	}

	/** 
	* @return The sqaure that results from scaling the side length and maintaining the bottom left corner
	*/
	public Square scale(double k) {
		return new Square(corner, sideLength * k);
	}

	public Point[] corners() {
		// write this
	}

	@Override
	public String toString() {
		return "(corner: " + corner + "; side length: " + sideLength + ")";
	}
}
```

Fill in the missing functions, and experiment with some squares in `Main.java`.
### SumArea

Okay, so now I want to have, in the `Main.java` file, an array of shapes, both `Square` and `Circle` objects, and to have a function that finds the sum of the areas of all the shapes.

In untyped pseudocode (like in Programming101), here's how we might loop through an array of shapes to find the sum of the areas:

```java
def sumAreas(var shapes) {
	var sum = 0
	for (var shape : shapes) {
		sum += shape.area()
	}
	return sum
}
```

`Circle` and `Square` objects both have `area` methods, so if the computer followed those instructions the code would work. But the computer doesn't really have any way of *knowing* that it would work.

What happens when you try to take this code and add types to it? Well, what type is `shapes`? It's an array, but an array of what? It's definitely not a `Square[]` or a `Circle[]`. *We* may know that the `shape.area` method exists for every value in `shapes`, but for the computer to understand that this code is safe, it has to know that too. That's what types are for.

We want one type that describes both `Circle` and `Square` objects. And what information does the computer need to know about this new type? Well it needs to know that this type of object has an `area` method that it can call. (Ideally, it would also know that the new type had all of the other methods that `Circle` and `Square` objects have in common, although that's not important for `sumAreas` in specific).

We can do this by creating an interface. An interface allows us to define a contract that classes can implement, specifying what methods they should have without providing the implementation details.

In a `Shape` interface, we would want to have the methods that `Circle` and `Square` have in common. Let's start with just the `area` function, since it's relevant to our example:

```java
public interface Shape {
    double area();
}
```

Notice, we just write the headers of the methods, not the implementations. Different kinds of shapes will have their own unique implementations.

Now, we need to tell our program that `Circle` and `Square` objects follow the `Shape` interface. We say that these classes *implement* the `Shape` interface. Here's how we show that in the code:

```java
public class Circle implements Shape {
```

```java
public class Square implements Shape {
```

*Side note: classes can implement multiple interfaces*

Now that you've updated your `Square` and `Circle` classes, you should be good to go! At this point, if you were to delete the `area` method from one of these classes (try it!), you would get an error, because `Circle` and `Square` are now required to have an `area` method.

Okay, let's write our `sumArea` method in `Main.java`:

```java
static double sumArea(Shape[] shapes) {
	double sum = 0;
	for (Shape shape : shapes) {
		sum += shape.area();
	}
	return sum;
}
```

Now test it out in the `main` method!

```java
Shape[] shapes = {new Circle(new Point(1.8, -20), 2), 
				  new Square(new Point(100, 2.1), 5.4),
				  new Circle(new Point(0, 0), 1),
				  new Circle(new Point(4, 9.123), 98.32),
				  new Square(new Point(-321, 0), 0.02)};
System.out.println(sumArea(shapes));
```

You should get around $30414.09$.
### ScaleAll

Next, lets write a static method in main that takes a `double` and `Shape[]` and returns a new `Shape[]`, but with each of the shapes scaled by the `double`.

```java
static Shape[] scaleAll(Shape[] shapes, double k) {
	Shape[] scaled = new Shape[shapes.length];
	for (int i = 0; i < shapes.length; i++) {
		scaled[i] = shapes[i].scale(k);
	}
	return scaled;
}
```

The only problem with this is that it `Shape` objects only have `area` methods. For this purpose, we need them to have `scale` methods as well. So let's add that!

```java
public interface Shape {
	public double area();

	/** 
	* @return The shape that results from scaling by k.
	*/
	public Shape scale(double k);
}
```

One thing to note about this new header: the return type for `scale` is `Shape`.

In our `Circle` class, the return type for the `scale` method is `Circle`. In our `Square` class, the return type is `Square`. So why is the return type here `Shape`?

Well, the `Circle` and `Square` objects are both examples of `Shape` objects, since they implement the `Shape` interface. So `Circle` and `Square` do indeed both have `scale` methods that return `Shape` objects.

And that's enough information for us. We want to scale an array of `Shape` objects, and we want to put all of those return values into another array of `Shape` objects. So what we need to know, really, is that the `scale` method returns a `Shape`.

Now, we are losing some information here. With this `Shape` interface, I could do the following:

```java
public class FakeShape implements Shape {
	public double area() { return 0; }

	public Square scale(double k) { 
		return new Square(new Point(0, 0), 1); 
	}
}
```

I've created a new `Shape` class called `FakeShape`, but unlike `Circle` and `Square`, each of which have `scale` methods that return another instance of their own class, `FakeShape` has a `scale` method that returns a `Square`. That doesn't make much sense if you think about what it means to scale a shape - when you scale something you don't get a new type of shape, just a different size of the same shape. But the requirement in `Shape` is only that the return type of `scale` is a `Shape`, not that it's the same type as the class that its in.

But we're just going to ignore that and trust ourselves to write reasonable code. (This can also cause other minor issues that you're unlikely to run into, but that's how this language goes).

Test out the the `scaleAll` method in `main`! (It may take a little creativity since you can't just print out an array and see its contents).
### Shape

Anyway, we've now added `scale` to our `Shape` interface, but we don't have to stop there. There are more methods that all shapes (or at least the shapes in this guide) have. So let's add them all! Here's the new interface that defines what it means to be a `Shape`:

```java
public interface Shape {
	public double area();

	public double perimeter();

	/** 
	* @return Whether point p is inside of the shape.
	*/
	public boolean isInside(Point p);
	/** 
	* @return Whether point p part of/on the border of the shape.
	*/
	public boolean isOn(Point p);

	/** 
	* @param x How much to translate the shape by in the + x direction.
	* @param y How much to translate the shape by in the + y direction.
	* @return The shape that results from the translation.
	*/
	public Shape translate(double x, double y);

	/** 
	* @return The shape that results from scaling by k.
	*/
	public Shape scale(double k);
}
```
### Practice: fromPoints

In the `Circle` class, create a static method that generates a `Circle` from three points that are on the edge of the circle (if you don't remember and can't figure out how to do this, look it up).

```java
public static Circle fromPoints(Point p1, Point p2, Point p3);
```
### Practice: Right Triangle

Create a `RightTriangle` class that implements `Shape`. The sides of the triangle are necessarily parallel to the x and y axes, but the right angle can be in any corner (top right, bottom left, etc). You can store a corner and two side lengths (or any other combination of fields that describe a right triangle).

In addition to all the methods in `Shape`, `RightTriangle` should have a static method called `similar` that takes two `RightTriangle` objects and returns whether or not they are similar.
## Inheritance

Inheritance is a form of polymorphism in Java that allows a class to inherit properties and methods from another class. We're not going to spend much time on this because inheritance is rarely the best solution to a problem and generally introduces more issues than it solves. In most cases, interfaces or generics provide simpler and more elegant solutions. Understanding inheritance will be most useful for understanding and interacting with the infrastructure that has already been written by other people.

Inheritance is a way of having classes that *inherit* the traits (methods and fields) of other classes. If class `B` extends (or inherits from) class `A`, then a `B` object will also be an example of an `A` object and can b treated as such. This is similar to our interfaces, where `Circle` and `Square` were examples of `Shape` objects, with two main differences:
1.  `A` is just an ordinary class. You can't just make a new `Shape` -- that doesn't mean anything. you have to make a `Square` or `Circle`. But you *can* just make a new `A`.
2. The `A` class has methods with real implementations (including a constructor) and fields with values. It isn't just a template for its child classes (classes that inherit from it) to follow. `B` will be able to call methods from `A`. When you create a new `B`, the constructor for `B` will call the constructor for `A`. If you have an `B` object called `b`, you can call the methods that are defined in `A` on that object.

Let's add some code to go along with this example.

```java
public class A {
	protected final double field1;
	protected final double field2;

	public A(double field1, double field2) {
		System.out.println("the constructor of A has been called");
		this.field1 = field1;
		this.field2 = field2;
	}

	public void method1() {
		System.out.println("method 1 of A has been called");
	}
	
	public void method2() {
		System.out.println("method 2 of A has been called");
	}
}
```

So A is just a very simple class with two fields and two methods. The only thing here that you haven't seen at all is the word `protected`. The key word `protected` describes something which is visible only to a class, classes that inherit from it (its subclasses or child classes), and the other classes in its package. So in this case, all of the `protected` fields will be accessible by `B`, (as well as any files in the same folder as `A`), and nothing else.

```java
public class B extends A {
	public final String bField;
	
	public B(double field1and2, String bField) {
		super(field1and2, field1and2);
		this.bField = bField;
		System.out.println("the constructor of B has been called");
	}

	@Override 
	public void method2() {
		System.out.println("method 2 of B has been called");
	}

	public double field() {
		return super.field1;
	}
}
```

Let's go through this line by line:

```java
public class B extends A {
```

Adding `extends A` to the class declaration indicates that `B` inherits from/is a child class of `A`.

```java
super(field1and2, field1and2);
```

`super` is a keyword for a class to refer to its parent class (similar to `this`, a keyword for a class to refer to itself). So this line is calling the constructor of this class's parent class, `A`. The constructor of a child class *must* call the constructor of its parent class. In fact, it has to be the very first thing that the constructor does.

If the parent class has a constructor that takes no arguments at all, the child class doesn't have to explicitly call the parent constructor --- it will happen automatically. But if, as in this case, the parent's constructor needs to be given inputs, the child class has to do that explicitly.

In this particular case, `A` takes two double fields as inputs. `B` takes a double and a String. The double is passed to the constructor of `B` twice. So if you pass 4 to `B` as `field1and2`, it will construct an `A` with 4 and 4. Remember, `B` inherits the traits of `A`, including its protected fields `field1` and `field2`, so when `B` references `super.field1` or `super.field2`, those values Bu both be 4.

```java
@Override
public void method2() {
```

The interesting part of this code is the `@Override` decorator. `B` inherits the `method1` and `method2` of the `A` class already, so it doesn't need to create its own. With `method1`, it doesn't make its own. If you have a `B` object called `b` and you call `b.method1()`, the code that will run is the function definition for `method1` in the `A` class.

But sometimes child classes want to have their own separate implementations for methods, so they override the methods of their parents. That's what `B` is doing here. It's making it's own definition for `method2`, so if you were to call `b.method2()`, instead of the code in `A` running, the code for `method2` in `B` will run.

Adding the `@Override` decorator when you're overriding the method implementation of a parent class isn't technically necessary, but it's very good practice.

So, what will happen if we in our main class do the following?

```java
A a = new A(12.3, 430);
```

We expect that code to call the `A` constructor, at which point it prints `"the constructor of A has been called"`. So we expect to see that on the console. Try it!

What if we do this:

```java
B b = new B(-12.31, "hello");
```

Well, this will call the constructor of `B`. But the constructor of `B` also calls the constructor of `A`! So what will it print? Think it through and then run it to check your logic.

How about this?

```java
a.method1();
b.method1();
b.method2();
```

Again, think through what would print, and then check yourself by running it.

Now what if we do this:

```java
A bInDisguise = new B(1002.013, "world");
bInDisguise.method2();
```

This will work because `B` inherits form `A`, and therefore `B` is a type of `A`. So if we have a variable of type `A`, the value could actually be a `B` object and that's okay. So what would that print?

Now how about this:

```java
System.out.println(b.bField + " " + bInDisguise.bField);
```

What should that print? Does it work?

What will actually happen in this case is that you'll get a compile-time error. Why? Well, even though we know that the value of `bInDisguise` is a `B` object, the type of the variable is `A`, so the computer will always treat it only as an `A` object. And `A` doesn't have a `bField`, so you can't access the `bField` of `bInDisguise`, because it's being treated as an `A`.
### Object class

You have actually seen `@Override` in one other context in these guides: `toString` methods.

When we write a `toString` method for a class, we use the `@Override` to show that we are overriding the default method implementation. But what are overriding exactly? With `B`, we were overriding the method defined in `A`. But our `Circle` class didn't inherit anything, did it? 

Well, actually it did. In fact, every single class in Java extends a class called `Object`.  In the case of `Circle`, it did not extend any other classes, so its direct parent class was by default `Object` --- just like if we had written:

```java
public class Circle extends Object implements Shape {
```

If, like `B`, a class does have an explicit parent class other than `Object`, it no longer is directly a child of `Object` (no class can have multiple parent classes), but it still indirectly inherits from `Object`. Let's think about this with the `A` `B` example. `B` inherits from `A`, so it does not directly inherit from `Object`. But `A` doesn't inherit from anything explicitly, so it is a direct child of `Object`. And that means not only that it inherits traits from `Object`, but also that it passes those traits to `B`. So, through `A`, `B` does indirectly inherit from `Object`.

And what exactly do all these classes inherit from `Object`? Well, they inherit lots of methods that are useful for everything to have. I'm not going to go over all of them, but they include `toString`, `hashCode` (look it up if you're interested!), and `equals` (takes another object as an argument and returns whether they are the same).

### Library

Let's say we're building a system to keep track of item checkouts at a library. We're going to make this incredibly simple (unrealistically so): Each item will store whether or not it has been checked out, and have a method to check the item out and to return it. Each item will also have a method to check if it is available.

We're going to have two main types of items: books and DVDs. And there will be a class for each of these types of items.

We'll have a `LibraryItem` that will be the parent class to `Book` and `DVD`.

```java
public class LibraryItem {
    public final String title;
    public final String itemId;
    
    protected boolean isCheckedOut = false;

    public LibraryItem(String title, String itemId) {
        this.title = title;
        this.itemId = itemId;
    }

	public boolean available() {
		return !isCheckedOut;
	}

    public void checkOut() {
        isCheckedOut = true;
    }

    public void returnItem() {
        isCheckedOut = false;
    }
}
```

```java
public class Book extends LibraryItem {
    public final String author;
    public final int pageCount;

    public Book(String title, String itemId, String author, int pageCount) {
        super(title, itemId);
        this.author = author;
        this.pageCount = pageCount;
    }

	@Override
    public String toString() {
        return "Book: " + title + " by " + author + ", " + 
		        pageCount + " pages";
    }
}
```

```java
public class DVD extends LibraryItem {
    public final double runtime;

    public DVD(String title, String itemId, double runtime) {
        super(title, itemId);
        this.runtime = runtime;
    }

    @Override
    public String toString() {
        return "DVD: " + title + ", Runtime: " + runtime + " minutes";
    }
}
```

Read through this example carefully until you understand what's happening, and then complete the practice problems.
### Practice: returnAll

Make a static method in `Main` that takes an array of `LibraryItem` objects and returns them all to the library.

```java
public static void returnAll(LibraryItem[] items) {
```

Test your method when you're done!
### Practice: availableItems

Make a static method in `Main` that takes an array of `LibraryItem` objects and outputs an `ArrayList` of `LibraryItem` objects with all of the available items from the input array.

```java
public static ArrayList<LibraryItem> availableItems(LibraryItem[] items) {
```
# Glossary

| **word/phrase** | **meaning**                                 |
| --------------- | ------------------------------------------- |
| field           | A variable belonging to an object or class. |
| method          | A function belonging to an object or class. |
|                 |                                             |
