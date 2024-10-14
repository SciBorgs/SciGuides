# Introduction

"Unit testing is a software development practice where individual components or functions of a program are tested in isolation to ensure they work correctly. It involves writing and running automated tests for specific units of code to verify their behavior, catch bugs early, and facilitate easier maintenance and refactoring of the codebase." - Claude.ai
## JUnit

JUnit is a common unit testing framework for Java. We use JUnit 5.
### Setup

First off, make sure that you've installed the VSCode extension "Test Runner for Java".

If you're working in a non-WPILib project, without gradle, here's how you can set up JUnit:
1. Open your project directory in VSCode
2. Make sure there is at least one Java file (if there isn't make one). This should activate the VSCode Java extensions.
3. Press on the testing tab on the left side of the screen
   ![](/reference-sheets/images/testing-icon.png)
4. Press "Enable Java Tests"
5. Press "JUnit Jupiter". There should now be a `lib` folder in your project with the JUnit library necessary to run unit tests.

If you're working in a WPILib project and you're using [Hydrogen](link) or [SciGuidesRobotBase](link), it should be set up for you already. Otherwise,