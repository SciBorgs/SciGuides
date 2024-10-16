# Table of Contents

- [Introduction](#introduction)
- [Technicals](#technicals)
  - [Setting up JUnit 5](#setting-up-junit-5)
  - [Imports](#imports)
  - [Structure](#structure)
  - [Types of methods](#types-of-methods)
  - [Annotations](#annotations)
  - [Assertions and Assumptions](#assertions-and-assumptions)
    - [Assertions](#assertions)
    - [Assumptions](#assumptions)
    - [AssumingThat](#assumingthat)
  - [Sim](#sim)
  - [Testable robot code](#testable-robot-code)
  - [Limitations](#limitations)
  - [Running tests](#running-tests)
  - [Example code](#example-code)
    - [Class structure](#class-structure-write-after-you-have-examples)
  - [Helpful links](#helpful-links)
- [Procedures](#procedures)
  - [When to use unit tests](#when-to-use-unit-tests)
  - [Java assert keyword](#java-assert-keyword)
  - [Best practices](#best-practices)
- [Troubleshooting](#troubleshooting)

# Introduction

Unit testing is a method of testing blocks (or units) of code. JUnit is a common unit testing framework for Java. We will be using JUnit 5.
# Technicals

## Setting up JUnit 5

1. Create path `src/test/java`. All tests should be at this address
2. OPTIONAL: Instal VSC extension *Test Runner for Java*
3. Make sure that the following clauses are in `build.gradle`:
    ```
    test {
        useJUnitPlatform()
        systemProperty 'junit.jupiter.extensions.autodetection.enabled', 'true'
    }
    ```
    ```
    dependencies {
        testImplementation 'org.junit.jupiter:junit-jupiter-api:5.8.2'
        testImplementation 'org.junit.jupiter:junit-jupiter-params:5.8.2'
        testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.8.2'
    }
    
    ```

## Imports

1. Assertions:
    ```
    import static org.junit.jupiter.api.Assertions.*;
    ```
2. Everything else:
    ```
    import org.junit.jupiter.api.*;
    ```
3. Remember to import whatever file you're testing!
4. Sim:
    ```
    import edu.wpi.first.hal.HAL;
    ```
5. Also import whatever specific devices/sim devices that you need. The most common one you'll be using is CANSparkMax:
    ```
    import com.revrobotics.CANSparkMax;
    ```

## Structure

1. Testing Classes
    - All testing code is written inside Testing Classes
    - **link to example coming soon**
2. Testing Suites
    - Testing Suites are sets of testing classes
    - VSCode does not yet support Testing Suites, but if that changes they'll be a useful tool

## Types of methods

There are many different types of methods to use inside of testing classes, and different kinds of methods are proceeded by different annotations

1. Test methods
    - These are the actual tests
    - Special types of test methods:
        1. Repeated Tests
            - Method repeats a specified number of times
            - Helps to ensure consistency
        2. Parameterized Tests
            - Method repeats multuiple times with different parameters
            - There are specified sources that it draws from, repeating once with each value
            - Types of sources:
                1. ValueSource: An array of literal parameters
                2. NullSource
                3. EmptySource
                4. Etc.
            - Increases efficiency/avoids redundancies
2. BeforeEach
    - These methods run before each test in a class
    - Often used to create an object
3. AfterEach
    - These methods run after each test in a class
    - Often used to destroy an object
4. BeforeAll
    - This is the first method to run in a testing calss
5. AfterAll
    - This is the last method to run in a testing class

## Annotations

1. `@Test`
    - Purpose
      - Goes before regular testing methods
    - Variations
      - Expected exception: `@Test( expected =` ***`insert expected exception`***`)`
2. `@BeforeEach`
    - Purpose
      - Goes before BeforeEach methods
3. `@AfterEach`
    - Purpose
      - Goes before AfterEach methods
4. `@BeforeAll`
    - Purpose
      - Goes before BeforeAll methods
5. `@AfterAll`
    - Purpose
      - Goes before AfterAll methods
6. `@Disabled`
    - Purpose
      - Goes before test methods or test classes
      - Indicates that the test(s) it precedes should not be run
7. `@Timeout(seconds)`
    - Purpose
      - Goes before test methods
      - Indicates that the test it precedes should timeout after the given number of seconds
8. `@Tag(tag name)`
    - Purpose
      - Goes before test methods or classes
      - Categorizes tests so that you can filter what tests based on the names
      - Generally used to filter what tests are included in Testing Suites
      - For instance, if you tagged all fast tests with one tag, you could make a Testing Suite that only includes fast tests
9.  `@IncludeTags(tag)`
    - Purpose
      - Goes in Testing Suites
      - Filters tests included in the suites by their tag
10. `@DisplayName(name)`
    - Purpose
      - Goes before test methods
      - The given name is displayed when the test runs
11. `@RepeatedTest(# of repititions)`
    - Purpose
      - Goes before RepeatedTest methods
12. `@ParameterizedTest`
    - Purpose
      - Goes before ParameterizedTest methods
13. `@ValueSource(array_name = {values}`
    - Purpose
      - Goes before ParameterizedTest methods
      - Includes sources for the test it precedes to draw from
14. `@NullSource`
    - Purpose
      - Goes before ParameterizedTest methods
      - The test it precedes will run once with a null parameter
15. `@EmptySource`
    - Purpose
      - Goes before ParameterizedTest methods
      - The test it precedes will run once with an empty parameter
16. More annotations can be found [here](https://junit.org/junit5/docs/current/user-guide/#writing-tests-annotations)

## Assertions and Assumptions

### Assertions 

Assertions go inside tests, and whether or not they succeeds decides whether or not the test does. Most tests have assertions, and those without fail only when an exception is thrown. There are many different kinds of assertions to choose from.

1. `assertEquals(expected, actual, optionalFailMessage)`
    - asserts that expected and actual are equal
2. `assertNotEquals(unexpected, actual, optionalFailMessage)`
    - asserts that unexpected and actual are not equal
3. `assertSame(expected, actual, optionalFailMessage)`
    - asserts that expected and actual refer to the same object
4. `assertNotSame(unexpected, actual, optionalFailMessage)`
    - asserts that uexpected and actual refer to different objects
5. `assertTrue(condition, optionalFailMessage)`
    - asserts that condition is true
6. `assertFalse(condition, optionalFailMessage)`
    - asserts that condition is false
7. `assertNull(object, optionalFailMessage)`
    - asserts that object is null
8. `assertNotNull(object, optionalFailMessage)`
    - asserts that object is not null
9.  `assertThrows(expectedExceptionType, executable, optionalFailMessage)`
    - asserts that executing executable returns and throws an exception of expectedExceptionType
10. `assertTimeout(timeout, executable, optionalFailMessage)`
    - asserts that executing executable takes no longer than timeout is exceeded
11. `fail(optionalFailMessage)`
    - automatically fails the test
12. `assertAll(executables...)`
    - asserts that all executables throw no exceptions
13. More assertions can be found [here](https://junit.org/junit5/docs/5.0.1/api/org/junit/jupiter/api/Assertions.html)

### Assumptions

Assumptions also go inside of tests, but unlike assertions, a failed assumption does not cause a failed test. Instead, when an assumption fails, the test that it's in is aborted. In other words, including assumptions in tests makes the tests conditional, only running if the assumption is true. There are two main kinds of assumptions.

1. `assumeTrue(assumption, optionalAbortMessage)`
    - aborts test unless assumption is true
2. `assumeFalse(assumption, optionalAbortMessage)`
    - aborts test unless assumption is false

### AssumingThat

The assumeThat method is a combination of an assertion and an assumption.

1. `assumingThat(assumption, executable)`
   - if assumption is true, runs executable
     - If the executable throws an exception, the test method fails 
   - if assumption is false, does nothing

## Sim

[Robot simulation](insert-link-when-it-exists) is the primary method of testing robot code with unit tests. When there isn't a physical robot to test on, we can test subsystems using simulated motors and other sensors/actuators.

To set up Sim, this line should be included in the BeforeEach method:

```
AssertTrue(HAL.initialize(500, 0));
```
**is it ever useful to not have that be 500?**

An explanation of HAL can be found [here](insert-link-when-it-exists).

Please read the section on [simulated devices](insert-link-when-it-exists), because they are used in unit testing to make sure your code is acting the way you want it to.

## Testable robot code

There are a few practices that are necessary to take when writing robot code to ensure that it is easily testable.

(some sort of resetting will be here but we need to figure out what that will look like)

## Limitations

While unit testing is a great tool, there are some important limitations, especially when it comes to robot code.

1. resetting shuffleboard...???
    - hopefully this will not be relevant this year so I'm going to hold off writing about it
2. Sim Accuracy
    - The first and most obvious limitation is that the tests can only be as accurate as sim is
    - There's still a lot of information that you can get, but just because something works in sim, doesn't mean it'll work in the real world

## Running tests

There are two ways to run tests:

1. Running tests using *Test Runner for Java*:
    - Either open the VSC testing tab and click run symbol, or go to any test or testing class and click on the little green/red symbol next to it
2. Running test using WPILib
    - Run the Test Robot Code command from the WPILib menu

## Example code

### Class structure (write after you have examples)

(this will be sort of explaining the examples)

- static subsystem
- class vars (can devices)

**coming soon**

## Helpful links

1. [Official JUnit 5 user guide](https://junit.org/junit5/docs/current/user-guide/)
2. [Other helpful JUnit 5 guide](https://www.baeldung.com/junit-5)
3. [JUnit 5 API](https://junit.org/junit5/docs/5.0.1/api/)
5. [WPILib unit testing docs](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/unit-testing.html)

# Procedures

## When to use unit tests

1. Subsytems: Every subsystem should have a testing class dedicated to it, where all of its functionality is tested (to whatever extent possible). (link to example)

2. Util classes: Each util classes should have a dedicated testing class as well. (link to example)

3. Commands: Not all commands need testing classes, but for more complex commands such as auto routines, have a testing class is advisable. (link to example)

For any class that is to be tested, it is the responsibility of the person who writing it to write the testing class. Ideally, that person would create the testing class when they create the class, and add tests as they add functionality to the class.

## Java assert keyword

As tempting as it may be, we do not use the java assert keyword for unit tests. It is practically the same as JUnit's AssertTrue in most ways, but there are a few key difference that make JUnit assertions a better choice:

- Java assert statements are not always enabled, whereas, in the context of unit tests, JUnit assertions are
- JUnit assertions have more options for methods
    - While many of the assertions tha JUnit provides could be accomplished in slightly different ways using only the assert keyword (or AssertTrue), using different, specific assertions often makes code more concise and readable.
    - Using more specific types of assertions also gets you more useful exceptions
- If you're using specific JUnit assertions such as AssertEquals or AssertSame in some tests, it is better to be consistant, and always use JUnit assertions

## Best practices

There are some standards and practices that we try to stick to as a team:

- delta
    - Each testing class should have a final class variable called delta, who's value the some small double representing acceptable deviation
    - This is generally written as ne-m
- naming conventions
    - naming testing classes
        - if the class that is being tested is named `X.java`, the testing class should be named `XTest.java`
        - for example, the testing class for `Climber.java` should be named `ClimberTest.java`
    - naming tests
        - names for tests should be clear and informative, and should always end in the word Test
        - for example, a method that tests the direction of a certain mechanism might be naimed directionTest()
    - @DisplayName
        -  The @DisplayName annotation should be used only when the test method name is long or unreadable. Ideally, this won't happen, but if, let's say, you're testing some method with a super long name, the test name might need to be super long as well. In this case, @DisplayName should be used to set a more readable name which will be desplayed when the test runs
- repeated tests
    - repeated tests should be use whenever the thing being tested has any significant amount of randomness or variability
    - for example, (*insert good example*)
- paramaterized tests
    - whenever paramaterized tests can be used to reduce redundancy, they should
    - for example, (*insert good example*)
- error messages
    - (currently not working great, but if i change that i'll add something here)

# Troubleshooting

NOTES:
- bullet points or numbers ***choose one***
- change structure so important things are higher
- add example code
- clean up sim
