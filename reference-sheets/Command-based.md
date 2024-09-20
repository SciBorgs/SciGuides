# [The Command-based Paradigm](https://docs.wpilib.org/en/stable/docs/software/commandbased/what-is-command-based.html)

For its wide capabilities and ease of use, we use WPILib's command-based paradigm to compartmentalize and control the different parts of our robot.

Subsystems represent independent parts of the robot and their hardware, which work together to achieve a desired action.

Commands safely direct those subsystems to perform actions in a wide suite of ways. They can be chained together in parallel or made sequential to one another, among other handy functions.

While these are generally their definitions, there's a fair bit of nuance to both.

## [Subsystems](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html)

For our purposes, all subsystems extend WPILib's `SubsystemBase`, providing command safety functionality, its [inherited periodic methods](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html#periodic), and [default commands](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html#default-commands). See in greater detail on [the official WPILib docs](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html).

Advanced readers may want to know [more about what a subsystem is](#a-word-on-what-makes-a-subsystem-a-subsystem).

## [Commands](https://docs.wpilib.org/en/stable/docs/software/commandbased/commands.html)

Commands represent robot actions with the hardware. They should be used for actions that may interfere with how the robot is run (i.e actual robot actions or changing PID constants) or cause dangerous movement.

Every individual command has a defined structure, with methods that are called when it begins, throughout its runtime, and when it ends (as a result of a set end condition OR by interruption). Check the [official docs](https://docs.wpilib.org/en/stable/docs/software/commandbased/commands.html) for specfics.

A nice list of these individual commands can be found under the subclasses of WPILib's [Command class](https://github.wpilib.org/allwpilib/docs/release/java/edu/wpi/first/wpilibj2/command/Command.html).

We avoid using specific control commands like the `PIDCommand` or `SwerveControllerCommand` as they limit our precision and capabilities compared to using their components individually.

### Command Compositions

Commands can also be chained together to create much larger commands for complex routines. You'll likely be using these a lot:

- [Parallel Commands](https://docs.wpilib.org/en/stable/docs/software/commandbased/command-compositions.html#parallel) - run multiple commands / runnables at once
  - Deadline and Race Commands (different end conditions)
- [Sequential Commands](https://docs.wpilib.org/en/stable/docs/software/commandbased/command-compositions.html#sequence) - run commands / runnables after the previous one ends

For more examples, see a good list [here](https://docs.wpilib.org/en/stable/docs/software/commandbased/command-compositions.html#composition-types).

### Decorators

WPILib provides command methods that can chain onto other commands to dynamically create compositions like the one below.

These include methods like `andThen()` and `alongWith()`, representing the creation of a sequential and parallel command respectively.

When properly composed, complex commands can often be read through like plain english, like below:

```java
    operator
        .leftTrigger()
        .whileTrue(
            shooting.shootWithPivot(PivotConstants.FEED_ANGLE, ShooterConstants.DEFAULT_VELOCITY));
    // while the operator controller's left trigger button is held, shoot
```

Individual commands and command groups each have their own singular / group of decorators. The majority can be found [here](https://github.wpilib.org/allwpilib/docs/release/java/edu/wpi/first/wpilibj2/command/Command.html).

Commands can also be accessed through [WPILib's `Commands`](https://github.wpilib.org/allwpilib/docs/release/java/edu/wpi/first/wpilibj2/command/Commands.html) class.

## Specifics & Common Issues

### Singular Command Instances

Each instance of a command can only be scheduled once at a time, otherwise risking unpredictable behavior. To remedy this, we create command factories that return new instances of a command each time it is called, like below:

```java
    public Command updateSetpoint(double velocity) {
        return run(() -> hardware.setVelocity(velocity));
    }
```

### Command Composition Requirements & Proxying

When created, command compositions take on the subsystem requirements of all of its parts, sometimes creating undesirable behavior as no other commands can be run on a subsystem even if the composition has sequenced past that point.

The current best solution to this (as of 24-25) is command proxying. See [the docs](https://docs.wpilib.org/en/stable/docs/software/commandbased/command-compositions.html#scheduling-other-commands) for a more in-depth discussion.

### A word on what makes a subsystem a subsystem

More specifically, subsystems can be defined as collections of hardware that are not dependent on others to function well. As a result, multiple different mechanisms can be part of a single subsystem.

For instance, imagine a double-jointed arm. When the joint connected to the main pivot moves, the position of the arm stemming from the joint will change, making their movement and position dependent on one another.

As a result, it is good practice to contain both mechanisms in the same subsystem so that they have easy access to each other's information, which makes accounting for relative position easier. This limits code duplication and makes working with the whole simpler.

**This is not set in stone, and from year to year, the requirements for robot operation may change. Use your own discretion to see what sense of organization works best for your robot!**
