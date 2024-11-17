# Introduction

"Unit testing is a software development practice where individual components or functions of a program are tested in isolation to ensure they work correctly. It involves writing and running automated tests for specific units of code to verify their behavior, catch bugs early, and facilitate easier maintenance and refactoring of the codebase." - Claude.ai
## JUnit

JUnit is a common unit testing framework for Java. We use JUnit 5 Jupiter.
## Setup

First off, make sure that you've installed the VSCode extension "Test Runner for Java".

If you're working in a non-WPILib project, without gradle, here's how you can set up JUnit:
1. Open your project directory in VSCode
2. Make sure there is at least one Java file (if there isn't make one). This should activate the VSCode Java extensions.
3. Press on the testing tab on the left side of the screen
   ![](/reference-sheets/images/testing-icon.png)
4. Press "Enable Java Tests"
5. Press "JUnit Jupiter". There should now be a `lib` folder in your project with the JUnit library necessary to run unit tests.

If you're working in a WPILib project and you're using [Hydrogen](link) or [SciGuidesRobotBase](link), it should be set up for you already. Otherwise, here's how you can set it up:
1. Open your project directory in WPILib VSCode
2. Create path `src/test/java`. All tests should be at this path.
3. Add the following clauses to `build.gradle`:
```
dependencies {
	testImplementation 'org.junit.jupiter:junit-jupiter-api:5.+'
    testImplementation 'org.junit.jupiter:junit-jupiter-params:5.+'
    testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5+'
}

test {
    useJUnitPlatform()
    systemProperty 'junit.jupiter.extensions.autodetection.enabled', 'true'
}
```
Additionally, if you're using unit testing for robot code, and will be using our libraries:
1. If you're using systems checks: add the following clause to `build.gradle`:
```
dependencies {
	implementation 'org.junit.jupiter:junit-jupiter-api:5.+'
}
```
2. For unit testing: copy [this file](https://github.com/SciBorgs/Hydrogen/blob/main/src/main/java/org/sciborgs1155/lib/UnitTestingUtil.java) into your project (probably into a lib folder).
3. For systems checks: copy [these](https://github.com/SciBorgs/Hydrogen/blob/main/src/main/java/org/sciborgs1155/lib/Test.java) [three](https://github.com/SciBorgs/Hydrogen/blob/main/src/main/java/org/sciborgs1155/lib/FaultLogger.java) [files](https://github.com/SciBorgs/Hydrogen/blob/main/src/main/java/org/sciborgs1155/lib/Assertion.java) into your project (probably into a lib folder).
# How does JUnit work?

A JUnit test class is a Java class that contains all the test methods for testing a specific class in your codebase. These classes contain various methods to test specific parts of your code. Annotations (labels before methods/variables/classes that start with @) are used heavily to mark different kinds of methods.

Test methods (usually marked with @Test) are the actual tests that are run. For each test that is run, JUnit will create a fresh instance of the test class, to ensure that tests don't interfere with each other. Generally, test methods contain assertions (statements that check if certain conditions are true, and throw exceptions if they are not).

Test classes also often contain methods that run before/after each test (or all tests) has been run.

Please read the following: (only the specified sections - ignore everything else)
- [Vogella JUnit tutorial](https://www.vogella.com/tutorials/JUnit/article.html)
	- 1.2
	- 1.3
	- 1.6
	- 2 (overview)
	- 2.1
	- 2.4
	- 3.2 (ignore the part about adding dependencies)
- [JUnit 5 guide](https://www.baeldung.com/junit-5)
	- 4
	- Optional: 5, 6
- [RepeatedTest guide](https://www.baeldung.com/junit-5-repeated-test) (very short)
	- 1
	- 3
	- 4
	- 5
	- Optional: 6, 7
# Best Practices

If you're only going to remember a few best practices, these are some important ones:
1. Test *every part of your code* that you can test!
2. Write tests as you go! Don't wait until you finish writing all the code.
3. Make sure that your tests are self-contained. They should not impact/be impacted by other tests or parts of your code.
4. Instead of just having one test case, use parameterized tests to test a variety of cases.
5. Whenever you are testing something that is non-deterministic or has randomness, use repeated tests to ensure that it works reliably!

Read the following sections of [this page](https://www.baeldung.com/java-unit-testing-best-practices):
- 1
- 2
- 3.4
- 3.5
- 3.6
- 3.7
- 3.9 (this will turn out to be very important for robot code, but don't worry if you don't fully understand what they're saying)
- 3.10
- 3.11
- 3.12
# Testing Robot Code
Coming soon!