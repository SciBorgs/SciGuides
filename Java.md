# Java

Java sucks.

Currently the only officially supported languages to program FRC robots in are C++, Python, Java. Out of these, C++ is too complex and inaccessible for our team and Python is unsafe and unfit for actual software development. Since our school teaches Java in APCS, it is the language our team programs in.

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

### Lambdas and Anonymous Functions

todo

### Functional Interfaces

todo

### Switch Expressions and Pattern Matching

todo

### Javadoc

Aka: how to prevent your team from hating you

### Collections and Streams

todo

## Design Patterns

Design patterns are typically pretty stupid. These are simple ones that we use to keep our code organized and nice to maintain.

### Composition and Dependency Injection

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

### 

## Java's Flaws and Project Valhalla

You might notice that Java is separated into two distinct data types: primitives and objects. The main visual difference is that primitives have lowercase names and objects have `CamelCase` names

[Project Valhalla](https://openjdk.org/projects/valhalla/) is a project to eventually "fix" Java. *It was announced in 2014...*

## Style

- Variable names should be `camelCase`
- Class names should be `CamelCase` with a capital first letter
- Constant names should be `SNAKE_CASE`
- Every layer of our code should be

Note that we don't use [hungarian notation](https://en.wikipedia.org/wiki/Hungarian_notation), a strange naming convention used in WPILib that includes prefixing "members" with `m_` and constants with `k`
