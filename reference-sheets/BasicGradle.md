# Introduction

This is a basic overview of Gradle.

## [What is Gradle?](https://www.geeksforgeeks.org/software-engineering/introduction-to-gradle/)

Gradle is a build-automation tool that lets us compile, package, and test our code quickly and easily.

It's open source, which means it is free for anyone to download and use.

Gradle is used by all Java-based FIRST teams to build our code and run tasks that simulate and deploy our code.

## [Installing Gradle](https://docs.gradle.org/current/userguide/installation.html)

Gradle is generally installed with that year's version of WPILib. However, if for whatever reason, it was not installed or you want to update it, make sure you check the deprecation warnings [here](https://docs.gradle.org/current/userguide/upgrading_version_9.html#changes_9.4.0). Deprecated features are features that were broken or were not being used so they were removed by the developers in the updated versions.

## [Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html#gradle_wrapper)
Gradle Wrapper is a script that automatically downloads and uses the correct version of Gradle to build or run certain programs.

FRC projects use WPILib, which comes with Gradle Wrapper already installed, so you don't need to manually install it.


## Common Gradle commands
There are two functions most commonly used with Gradle Wrapper: spotless apply and building.

Spotless apply formats your code in a way that allows for readability, both for your code and for building it properly, depending on the rules your team has added.
Building your code is necessary in order to simulate and deploy it, as it compiles it and catches any errors that may cause issues later on.

Running spotless apply can be done by inputting
```bash
./gradlew spotlessApply
```
or
```bash
./gradlew sA
```
in your terminal.

Running build can be done by inputting
```bash
./gradlew build
```
or
```bash
./gradlew b
```
in your terminal.

You can run both at the same time by inputting
```bash
./gradlew sA b
```
in your terminal.

## Where is Gradle used inside the project?
In FRC repositories, you will see a build.gradle file and a gradle-wrapper file, which configure Gradle. These allow for the use of gradle and gradle wrapper.
