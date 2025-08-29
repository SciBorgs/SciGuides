# Java

Java sucks.

Currently the only officially supported languages to program FRC robots in are C++, Python, Java. Out of these, C++ is too complex and inaccessible for our team and Python is unsafe and unfit for production software development. Since our school teaches Java in APCS, it is the language our team programs in.

Kotlin (and other languages with interop with C++ or Java) also exist, but aren't officially supported. Kotlin didn't have significant enough advantages for us to switch to it.

Additionally, as of 2024, Java is used by the vast majority of other FRC teams (and in FTC), meaning it will be the easiest to get support in and many libraries we use will be primarily in Java.

In the future, C# and Rust will likely be options. I personally would prefer us to use Rust, but that won't be up to me.

## Advanced Java

Just because Java isn't a particularly good programming language doesn't mean our code has to be mediocre.

### Records

[Records](https://openjdk.org/jeps/395), similar to data classes or structs in other languages, are a way to store [immutable objects](https://en.wikipedia.org/wiki/Immutable_object) in Java.

```java
public record Person(String name, int age, double favoriteNumber) {}
```

### Polymorphism

```java
public class Parent { ... }

public class Child { ... }

Parent child = new Child();
```

### Lambdas and Anonymous Functions

Functions are data.

```java
DoubleUnaryOperator op = x -> x + 1;
System.out.println(op.applyAsDouble(2.1)); // prints 3.1
System.out.println(op.applyAsDouble(4.3)); // prints 5.3
```

Is equivalent (in functionality only) to

```java
static double op(double x) {
  return x + 1;
}

System.out.println(op(2.1));
System.out.println(op(4.3));
```

You could even write

```java
DoubleUnaryOperator opReference = Main::op;
```

### Functional Interfaces

As shown in the previous example, we assign functions to variables of the type `DoubleUnaryOperator`. In better languages this would be represented as something like `(double) -> double`, but Java requires every anonymous function to have a type defined by a functional interface. The actual implementation from Android open source looks like this

```java
@FunctionalInterface
public interface DoubleUnaryOperator {
    /**
     * Applies this operator to the given operand.
     *
     * @param operand the operand
     * @return the operator result
     */
    double applyAsDouble(double operand);

    /**
     * Returns a composed operator that first applies the {@code before}
     * operator to its input, and then applies this operator to the result.
     * If evaluation of either operator throws an exception, it is relayed to
     * the caller of the composed operator.
     *
     * @param before the operator to apply before this operator is applied
     * @return a composed operator that first applies the {@code before}
     * operator and then applies this operator
     * @throws NullPointerException if before is null
     *
     * @see #andThen(DoubleUnaryOperator)
     */
    default DoubleUnaryOperator compose(DoubleUnaryOperator before) {
        Objects.requireNonNull(before);
        return (double v) -> applyAsDouble(before.applyAsDouble(v));
    }

    /**
     * Returns a composed operator that first applies this operator to
     * its input, and then applies the {@code after} operator to the result.
     * If evaluation of either operator throws an exception, it is relayed to
     * the caller of the composed operator.
     *
     * @param after the operator to apply after this operator is applied
     * @return a composed operator that first applies this operator and then
     * applies the {@code after} operator
     * @throws NullPointerException if after is null
     *
     * @see #compose(DoubleUnaryOperator)
     */
    default DoubleUnaryOperator andThen(DoubleUnaryOperator after) {
        Objects.requireNonNull(after);
        return (double t) -> after.applyAsDouble(applyAsDouble(t));
    }

    /**
     * Returns a unary operator that always returns its input argument.
     *
     * @return a unary operator that always returns its input argument
     */
    static DoubleUnaryOperator identity() {
        return t -> t;
    }
}
```

You can see that all the methods defined in this interface, except one, are using the `default` keyword. This keyword allows functions in interfaces to have default implementations that implementing classes don't have to override. Any interface with only one unimplemented method can be used as a functional interface, meaning functions can be stored as or casted to it. The `@FunctionalInterface` annotation isn't strictly necessary.

> Aren't interfaces supposed to define functionality for classes?

Yes, they are. Because of Java's limitations on representing data, lambdas are actually wrappers for anonymous classes that have one function. Functional interfaces represent an interface that these anonymous classes can implement, forcing them to conform to specific standards.

This code:

```java
DoubleUnaryOperator op = x -> x + 1;
```

Is internally equivalent to:

```java
DoubleUnaryOperator op = new DoubleUnaryOperator() {
  @Override
  public double applyAsDouble(double x) {
    return x + 1;
  }
}
```

### Switch Expressions and Pattern Matching

todo

### Javadoc

Aka: how to prevent your team from hating you

### Collections and Streams

todo

## Design Patterns

Design patterns are typically pretty stupid. These are simple ones that we use to keep our code organized and nice to maintain.

### Composition and Dependency Injection

These are very fancy terms for very simple and intuitive concepts. When you want to add functionality of class A to class B, you just put A in B.

```java
public class 
```

### Factories

todo replace example

```java
public static Arm createArm() {
  return new Arm(Robot.isReal() ? new RealArm() : new SimArm());
}
```

### Singletons

You probably don't want to use these.

```java
public class ExampleSingleton {
  private static instance;

  public ExampleSingleton getInstance() {
    if (instance == null) {
      instance = new ExampleSingleton();
    }
    return instance;
  }

  /** A private constructor to prevent new instances from being created */
  private ExampleSingleton() {}
}
```

The WPILib [`CommandScheduler`](https://docs.wpilib.org/en/stable/docs/software/commandbased/command-scheduler.html) is an example of a singleton, since it can be accessed statically with `CommandScheduler.getInstance()`.

Note: While subsystems may seem like a good candidate to be singletons, since there is only one instance of each piece of hardware, they are not and should be accessible from everywhere in the code. Every part of our code accessing every other part would result in a tangled web of dependency that would make debugging nightmarish.

### 

## Java's Flaws and Project Valhalla

You might notice that Java is separated into two distinct data types: primitives and objects. The main visual difference is that primitives have lowercase names and objects have `CamelCase` names

[Project Valhalla](https://openjdk.org/projects/valhalla/) is a project to eventually "fix" Java. *It was announced in 2014...*

## Style

- Variable names should be `camelCase`
- Class names should be `CamelCase` with a capital first letter
- Constant names should be `SNAKE_CASE`
- Every layer of our code should be
- Prefer `final` in fields
- Prefer `private` in fields, especially mutable ones

Note that we don't use [hungarian notation](https://en.wikipedia.org/wiki/Hungarian_notation), a strange naming convention used in WPILib that includes prefixing "members" with `m_` and constants with `k`
