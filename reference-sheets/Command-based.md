# [The Command-based Paradigm](https://docs.wpilib.org/en/stable/docs/software/commandbased/what-is-command-based.html)

For its wide capabilities and ease of use, we use WPILIB's command-based paradigm to compartmentalize and control the different parts of our robot.

Subsystems represent independent parts of the robot and their hardware, which work together to achieve a desired action.

Commands safely direct those subsystems to perform actions in a wide suite of ways. They can be chained together in parallel or made sequential to one another, among other handy functions.

While these are generally their definitions, there's a fair bit of nuance to both.

## [Subsystems](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html)

For our purposes, all subsystems extend WPILib's `SubsystemBase`, providing command safety functionality, its [inherited periodic methods](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html#periodic), and [default commands](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html#default-commands). See in greater detail on [the official WPILIB docs](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html).

### A word on what makes a subsystem a subsystem

More specifically, subsystems can be defined as collections of hardware that are not dependent on others to function well. As a result, multiple different mechanisms can be part of a single subsystem.

For instance, imagine a double-jointed arm. When the joint connected to the main pivot moves, the position of the arm stemming from the joint will change, making their movement and position dependent on one another.

As a result, it is good practice to contain both mechanisms in the same subsystem so that they have easy access to each other's information, which makes accounting for relative position easier. This limits code duplication and makes working with the whole simpler.

**This is not a finite definition, and from year to year, the requirements for robot operation may change. Use your own discretion to see what sense of organization works best for your robot!**

## [Commands](https://docs.wpilib.org/en/stable/docs/software/commandbased/commands.html)

Every individual command has a defined structure, with methods that are called when it begins, throughout its runtime, and when it ends (as a result of a set end condition OR by interruption).

### Command Compositions

Commands can also be chained together to create much larger commands for complex routines. You'll likely be using these a lot:

- [Parallel Commands](https://docs.wpilib.org/en/stable/docs/software/commandbased/command-compositions.html#parallel) - allow multiple commands to be run at once with differing end conditions
  - Deadline
  - Race
- [Sequential Commands](https://docs.wpilib.org/en/stable/docs/software/commandbased/command-compositions.html#sequence) - allow commands to be run one after another

## Complications & Common Problems

Each instance of a command can only be scheduled once at a time, otherwise risking unpredictable behavior. To remedy this, we create command factories that return new instances of a command each time it is called, like below:

```java
    public Command updateSetpoint(double velocity) {
        return run(() -> hardware.setVelocity(velocity));
    }
```

- epxlain proxy (my eyes are going to fall)
