# Contents

- Enums
- Records
- [Lambdas & Functional Interfaces](#lambdas-functional-interfaces)
- Switch Expressions
# Enums

coming soon!
# Records

coming soon!
# Lambdas & Functional Interfaces

## Functional Interfaces 

### Example: filtering a list

Often, we want to be able to pass around functions like they are objects. For instance, maybe we want to write a static method that filters a list based on some condition. So we want to take a `List` with elements of type `T` (a generic type), and some condition, and then return a new `List` of type `T` that only includes the elements of our first list that meet the condition.

So, what would the type of our condition be? Well, we need to be able to check each individual element of the list. So it would make sense if our condition was actually a function, that takes in something of type `T` and returns a boolean.

For instance, let's say we had a function `isEven` that takes in an integer and returns whether it is even, and we wanted to filter a list of integers `intList` so that we'd only have the even numbers. We would like to be able to accomplish that by doing something resembling the following:

```java
List<Integer> filtered = filter(intList, isEven);
```

And then our function `filter` should go through each element in `intList`, feed it into `isEven`, and if the result is `true` it add it to a new filtered list.

But if we want to do that, to pass `isEven` around in Java, it needs to have a type, which means it needs to be an instance of some class. Think about it: if we try to write the header for our filter method, we need to have a type for `condition`:

```java
public static <T> List<T> filter(List<T> l, ___ condition);
```

*Side note: having the \<T\> before the return type of the method is the notation for declaring a generic type to be used in a method rather than an entire class.*

So let's think about what type `condition` should be. All that really matters is that it is a function with an input of type `T` and an output of type `boolean`. So we want to have some simple way to specify that.

That's where functional interfaces come in!  A functional interfaces is an interface that specifies *one* (abstract) method only. Remember, interfaces have methods that they define the shape of but don't actually implement. And then everything that uses an interface has to have implementations for all of the methods specified in the interface.

With functional interfaces, there is just one method that needs to be overridden/implemented. So for instance, there is a functional interface called `Function` which has two generic types, `T` and `R`.

```java
@FunctionalInterface
public interface Function<T, R> {

}
```

(The annotation `@FunctionalInterface` above the class header tells Java to treat the class as a functional interface.)

`Function<T, R>` is meant to represent the type of a function that takes an input of type `T` and has an output of type `R`. So the single method inside of the `Function` interface is called `apply`, and does just that:

```java
@FunctionalInterface
public interface Function<T, R> {
	R apply(T t);
}
```

The `apply` method has an input of type `T` and an output of type `R`. So if you have a variable `condition` of type `Function<Integer, Boolean>`, you can call `condition.apply(5)` and get a boolean in return.

That is how we can write our `filter` method (you can also use the `Predicate` interface)!
```java
public static <T> List<T> filter(List<T> l, Function<T, Boolean> condition) {
	ArrayList<T> filtered = new ArrayList<>();
	for (T element : l) {
		if (condition.apply(element)) {
			filtered.add(element);
		}
	}
	return filtered;
}
```

But then, if we want to call `filter` with `isEven`, do we need to make a whole new class that implements `Function<Integer, Boolean>` and has an `apply` function that calls `isEven`? That seems like too much work.

But that's actually the special thing about functional interfaces - we don't have to do that at all. If we just pass in our function, `isEven`, using a particular notation, Java will basically make that class for us.

The notation for referring to methods as functional interfaces is:

```java
// for static methods
Class::method
// for non-static methoods
object::method
```

In this case, `isEven` is definitely a static method. Let's say it's inside of a class called `Foo`, here's how we would filter our list:

```java
List<Integer> filtered = filter(intList, Foo::isEven);
```
### Other functional interfaces

Here are some other useful functional interfaces to know:
-  `Runnable`
	- method: `void run()`
	- no inputs, no outputs
- `Supplier<T>`
	- method: `T get()`
	- no inputs, output of type `T`
- `Consumer<T>`
	- method: `void accept(T t)`
	- input of type `T`, no output
- `BooleanSupplier`
	- method: `boolean getAsBoolean()`
	- works like a `Supplier<Boolean>`, but more efficient
- `DoubleSupplier`
	- method: `double getAsDouble()`
	- works like a `Supplier<Double>`, but more efficient

There are many others as well, and if you ever need a functional interface that doesn't exist, you can make your own!
## Lambdas

We've talked about functional interfaces, and how we can use them to pass around methods that belong to a class or object. Now we're going to talk about a different way of generating instances of functional interfaces.

A *lambda expression* is a concept in functional programming (you don't need to know what that means) that refers to an anonymous function, or a function without a name. In Java, lambdas are essentially a notation for creating implementations of functional interfaces.

Here's the basic, oversimplified notation:
```java
inputs -> output
```

So, if we wanted to filter a list to only have even numbers, but didn't have (or want to write) a whole separate `isEven` method, we could do the following instead:

```java
List<Integer> filtered = filter(intList, i -> i % 2 == 0);
```

Java will take that lambda expression that I wrote, and turn it into an instance of the `Function` interface, where the apply function takes an integer `i` and returns `i % 2 == 0`.

If you want a lambda expression that takes no inputs and returns something (i.e. an implementation of `Supplier`), you would use this notation:

```java
() -> output
```

If you want a lambda expression that takes multiple inputs (i.e. an implementation of `BiFunction`), you would use this notation:

```java
(input1, input2) -> output
```

If your lambda expression isn't supposed to have an output, but is instead supposed to do something, you use the same notation. So for instance, if you are writing a `Runnable` that takes no inputs and prints `Hello World`, it would look like this:

```java
() -> System.out.println("Hello World")
```

If your lambda expression has multiple lines, you use curly braces. So for instance, here's how you'd write a `Function<Integer, Integer>` that prints the integer input and then returns that integer times two:

```java
i -> { 
		System.out.println(i);
		return i * 2; 
	  }
```

Note that when you have curly braces, if your lambda has an output you need to write `return`!
# Switch Expressions

coming soon!