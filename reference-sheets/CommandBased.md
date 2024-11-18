# [The Command-based Paradigm](https://docs.wpilib.org/en/stable/docs/software/commandbased/what-is-command-based.html)

For its wide capabilities and ease of use, we use WPILib's command-based paradigm to compartmentalize and control the different parts of our robot.

Subsystems represent independent parts of the robot and their hardware, which work together to achieve a desired action.

Commands safely direct those subsystems to perform actions in a wide suite of ways. They can be chained together in parallel or made sequential to one another, among other handy functions.

These are general definitions; there's actually a fair bit of nuance to both.

## [Subsystems](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html)

For our purposes, all subsystems extend WPILib's `SubsystemBase`. It provides command safety functionality, its [inherited periodic methods](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html#periodic), and [default commands](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html#default-commands). See in greater detail on [the official WPILib docs](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html).

More specifically, subsystems can be defined as collections of hardware that are not dependent on others to function well. As a result, multiple different mechanisms can be part of a single subsystem.

For instance, imagine a double-jointed arm. When the joint connected to the main pivot moves, the position of the arm stemming from the joint will change, making their movement and position dependent on one another.

As a result, it is good practice to contain both mechanisms in the same subsystem so that they have easy access to each other's information, which makes accounting for relative position easier. This limits code duplication and makes working with the whole simpler.

## [Commands](https://docs.wpilib.org/en/stable/docs/software/commandbased/commands.html)

Commands represent robot actions with the hardware. They should be used for actions that may interfere with how the robot is run (i.e actual robot movement or changing PID constants.)

Generally when we create commands, we do so using preexisting types of commands, and a set of helpful static methods in a class called `Commands` that return Commands. (Theoretically, you could also make a whole class for each command, but that's almost never a good idea).

Before we talk about types of commands, let's quickly go over what the technical definition of a Command is. The class `Command` is what all Command classes inherit from, and it has four primary methods that different Command classes override in order to define their behavior:
- `public void initialize()`
	- Called when the command is started
- `public void execute()`
	- Called every tic (every 0.02 seconds) while the command is running
- `public void end(boolean interrupted)`
	- Called when the command is ended
	- Commands can end either because their end condition is met or because they are interrupted by another command on the same subsystem. `end` takes whether or not the command has been interrupted as an input, so that you can change the end behavior of a command based on whether it reached its end condition.
- `public boolean isFinished()`
	- This is the end condition for a command. It is called each tic after a command has been executed, and if it is `isFinished` returns `true`, the command is un-scheduled and `end(false)` is called (`false` because the command has not been interrupted).

I used the passive voice for these explanations, but just to be clear, all of these methods are being called by the `CommandScheduler`, which is in turn called periodically by `Robot`.

So, just to summarize the progression:
1. A command `c` is scheduled
2. `c.initialize()` is called
3. Each tic until the command is over:
	1. `c.execute()` is called
	2. `c.isFinished()` is called, and if it returns `true` the command is over
4. `c.end(interrupted)` is called

Commands also have a set of subsystems that they require.

Now, let's go over a two of the most common types of Commands, how they work, and how to make them:
- Run command (`RunCommand`)
	- `isFinished()` always returns `false`, so it keeps on running forever until it is interrupted.
	- Constructor: `RunCommand(Runnable toRun, Subsystem... requirements)`
		- toRun will be run in `execute()`
		- `requirements` is all of the subsystems that the command requires. The `...` means that you can just add as many as you want.
	- How to create using `Commands`: `Commands.run(Runnable action, Subsystem... requirements)`
	- Example: `Command toToOrigin = Commands.run(() -> drive.goTo(0, 0), drive)`
- Run once command (`InstantCommand`)
	- `isFinished` always returns `true`, so it stops immediately after just one execution
	- How to create using `Commands`: `Commands.runOnce(Runnable action, Subsystem... requirements)`
	- Example: `Command stop = Commands.runOnce(drive::stop, drive)`

We then build on commands like these using various methods that allow us to combine or modify different commands.

A nice list of these individual commands can be found under the subclasses of WPILib's [Command class](https://github.wpilib.org/allwpilib/docs/release/java/edu/wpi/first/wpilibj2/command/Command.html).

_Note: we avoid using specific control commands like `PIDCommand` or `SwerveControllerCommand` as they limit our precision and capabilities compared to using their components individually._

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

## Triggers

A big part of the command-based ecosystem are triggers. Users can bind commands and `Runnable` actions to triggers, which are run in specified ways when the trigger is activated. 

Common operations with trigger commands include, but are not limited to:

- `onTrue()`, run once on trigger activation
- `whileTrue()`, run periodically while trigger is active

For instance, the `teleop()` trigger in `Robot.java` (and its sisters) run binded commands when teleop mode is activated on the robot (by DriverStation or FMS).

See [here for examples and specific usage in WPILib](https://docs.wpilib.org/en/stable/docs/software/commandbased/binding-commands-to-triggers.html).

## Specifics & Common Issues

### Singular Command Instances

Each instance of a command can only be scheduled once, otherwise risking unpredictable behavior. To remedy this, we create command factories that return new instances of a command each time it is called, like below:

```java
    public Command updateSetpoint(double velocity) {
        return run(() -> hardware.setVelocity(velocity));
    }
```

### Command Composition Requirements & Proxying

When created, command compositions take on the subsystem requirements of all of its parts, sometimes creating undesirable behavior as no other commands can be run on a subsystem even if the composition has sequenced past that point.

The current best solution to this (as of 24-25) is command proxying. See [the docs](https://docs.wpilib.org/en/stable/docs/software/commandbased/command-compositions.html#scheduling-other-commands) for a more in-depth discussion.