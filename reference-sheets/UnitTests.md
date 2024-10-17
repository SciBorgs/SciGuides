# Introduction

"Unit testing is a software development practice where individual components or functions of a program are tested in isolation to ensure they work correctly. It involves writing and running automated tests for specific units of code to verify their behavior, catch bugs early, and facilitate easier maintenance and refactoring of the codebase." - Claude.ai
## JUnit

JUnit is a common unit testing framework for Java. We use JUnit 5.
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
#
Things that should be included:
- what is a testing class
- assertions
- what is the general concept?

```java

```