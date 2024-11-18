# Introduction

![driveSim](https://github.com/user-attachments/assets/e6aba468-f3eb-4114-acfa-703089c8e9b5)

This project is going to cover how to make both a basic and an advanced differential drive.
## Prerequisites

- Comfortable with all the [goals](/projects/intro-to-programming/Java102.md#goals) and [prerequisites](/projects/intro-to-programming/Java102.md#prerequisites) of Java102.
- Comfortable with [functional interfaces & lambdas](/reference-sheets/AdvancedJava.md#functional-interfaces-lambdas)
- Familiarity with types of [sensors](/reference-sheets/Sensors.md)
- [WPILib installed](/reference-sheets/EnvironmentSetup.md#wpilib)
## Goals

Some understanding of and familiarity with:
- Robot code
- Simulation
- Testing robot code
- Control theory
- Command-based programming

Also, a working, simulated, tested differential drive!
## What is a differential drive?

![drive gif](https://github.com/user-attachments/assets/80fd7fac-beb5-4985-a0a5-8318654f5040)

A differential drive is a type of robot drivetrain where two separately-driven groups of wheels are used to move the robot. By varying the speed of each wheel, the robot can move forward, backward, or turn. This setup is widely used due to its simplicity and high degree of control over the robot’s movement.

To move the robot forward/backward, both wheels must move at the same speed in the same direction. To turn, the wheels must move at different speeds or in opposite directions.
## Creating your project repo

The first step will be to create a repository for this project. We'll be using [this](https://github.com/SciBorgs/SciGuidesRobotBase) base template for this project (and all other robot code projects in SciGuides). Follow the instructions in the README to create a new repository based on the template. Give your repository a descriptive name such as "Differential Drive Bot".

In the README of your new repository, link [this guide](link).

Make sure to clone the project on your computer inside of your code folder!

---
# Robot Code Structure

Robot code is structured using *subsystems* and *commands* within FRC's *command-based framework*. This architecture simplifies robot programming by breaking down complex tasks into smaller, manageable pieces. 

All of your Subsystem classes must extend `SubsystemBase`. (Commands extend `Command`, but you won't really be writing full Command classes).

Running commands and enforcing the one-command-per-subsystem rule is managed by the `CommandScheduler`. Essentially, if you want to run a command, you tell the `CommandScheduler`, and then each time the code runs the `CommandScheduler` goes through all the `Commands` that it has been told to run, and runs them.

---

Please read the following sheets before moving forward:
- [Subsystems and Commands]()
- [File Structure]()
# Understanding the hardware

In order to program a robot, you first need to understand the physical hardware that you are working with, and particularly the electrical components.

For this guide, we’ll be using *CANSparkMax motor controllers* paired with *NEO motors*.

- **CANSparkMax:** A motor controller developed by REV Robotics designed specifically for controlling brushless motors like the NEO.
- **NEO Motor:** A brushless motor designed by REV Robotics.

Let's look at what a differential drivetrain might look like:

<img src="https://docs.wpilib.org/en/stable/_images/layout.jpg">

The black cylinders between the two center wheels are motors. As you can see, there there are two motors attached to each side of the drivetrain.

These motors are also connected via wires to motor controllers, which are connected ultimately to a roboRIO (gray square thing on the top). The roboRIO is a piece of hardware which connects and interfaces with all of the sensors and actuators on the robot (sensors collect data, actuators move). We can control those sensors and actuators by running code on the RIO.
- Remember `Ports.java`? Well, in order to control our electronics and for the RIO to send them signals, we need to know what physical ports our components are connected to. That's what we mean when we say that this file stores the ports for our components.

The RoboRIO is connected to a radio (the white rectangle to the right of the RIO), which is how we generally connect our computers to the RIO.
# Drive Folder

Our first step will be to create a drive folder for everything related to the Drive subsystem. It will include:
- a `Drive.java` subsystem that extends `SubsystemBase` and contains the logic to control the motors and the drivetrain.
- `DriveConstants.java`, containing whatever constants we will need for our subsystem (i.e. the dimensions of the drivetrain).

Once you do that, your files should look something like this:

![file order](https://github.com/user-attachments/assets/d37980f3-c1d6-4a9a-9e5f-66c0163496d7)
# Ports

In our `Drive.jav` class, we will make all of our 4 motors using `CANSparkMax` objects. When you create a `CANSparkMax` object, you give it a port and a motor type (don't worry about what the motor type means for now). With that port, it is able to interface with the motor connected to the port through the RIO.

Before we create our motor objects, let's add our ports to `Ports.java`.

Currently, the file should look like this:
```java
package robot;

public final class Ports {
  // TODO: Add and change all ports as needed.
  public static final class OI {
    public static final int OPERATOR = 0;
    public static final int DRIVER = 1;
  }
}
```

We structure our ports by creating a new static class within the `Ports` class for each subsystem (or in the case of `OI`, that's for the Xbox controllers). So create a new class for `Drive` ports!

```java
package robot;

public final class Ports {
  // TODO: Add and change all ports as needed.
  public static final class OI {
    public static final int OPERATOR = 0;
    public static final int DRIVER = 1;
  }

  public static final class Drive {
    public static final int RIGHT_LEADER = 2;
    public static final int RIGHT_FOLLOWER = 3;
    // etc
  }
}
```

As we said earlier, there will be four motors total, two on the right and two on the left. We're going to call one on each side the leader, and one the follower. 

In the example code I added ports for the motors on the right. Make sure you add for the ones on the left as well! You can assign any values that you want, as long as they are all different (and if you ever want to test this on a real drive train, you'll need to make sure the ports are accurate).
# Drive Subsystem

Now let's go back to `Drive.java` and write our subsystem!
## Motor instantiation

First off, we have to actually make our motor objects. We'll use the ports form `Ports.java`, and the motor type for all of our motors will be `MotorType.kBrushless`.

To do this, you will first need to import `MotorType`, `Ports`, and `CanSparkMax`. You will also have to import `SubsystemBase` so that you can make `Drive` into a Subsystem:

```java
package robot.drive;

import com.revrobotics.CANSparkMax;
import com.revrobotics.CANSparkLowLevel.MotorType;

import edu.wpi.first.wpilibj2.command.SubsystemBase;
import robot.Ports;

public class Drive extends SubsystemBase {

}
```

We gave you all the imports for this, but in the future, a trick you can use is to start writing the thing you need to import and then press tab. So, in this case, if you were to start writing `Drive extends SubsystemBase`, but didn't finish the last word, `SubsystemBase` would come up as a suggestion:
![](/images/subsystembase.png)
If you then press tab, it will finish the word for you and *actually import SubsystemBase*!

Okay, now we're ready to make our motors:

```java
public class Drive extends SubsystemBase {  
  private final CANSparkMax leftLeader = new CANSparkMax(Ports.Drive.LEFT_LEADER, MotorType.kBrushless);
}
```

Below the instantiation of `leftLeader`, make variables for all the other motors! (`leftFollower`, `rightLeader`, and `rightFollower`).
## Motor configuration

For our motors to work the way we want them to, we'll need to configure some specific settings. This will happen inside of our constructor, and we will be using various methods of the `CANSparkMax` class.

The first thing that we'll do is reset all our sparks to a default state, clearing any old configurations that they may have had:

```java
  public Drive() {
    for (CANSparkMax spark : List.of(leftLeader, leftFollower, rightLeader, rightFollower) {
	    spark.restoreFactoryDefaults();
    }
  }
```

Next, we're going to set something called the idle mode of our motors, which essentially determines the behavior of the motor when it's not being told to do anything. The options are:
- `kBrake`: stop as fast as possible
- `kCoast`: don't provide any voltage and just let it spin freely

For a drivetrain, we don't want our robot to just keep drifting when we stop driving, so we want all our motors on brake mode (make sure you import `CANSparkBase.IdleMode`):

```java
  public Drive() {
    for (CANSparkMax spark : List.of(leftLeader, leftFollower, rightLeader, rightFollower)) {
	    spark.restoreFactoryDefaults();
	    spark.setIdleMode(IdleMode.kBrake);
    }
  }
```

For the next part, we're going to need to understand why we're calling our motors leaders and followers. If you think about it, for a differential drive to work all of the wheels on one side need to be moving at the same speed. The point of having two motors isn't actually to control two wheels *separately*. Instead, it's to have enough power to control two wheels *together*.

So that means that we always want the two motors on the right and the two motors on the left to be moving the same way. We accomplish this by telling one motor on each side (the *follower*) to follow the other one (the *leader*). That way we only have to control the two leaders, and the followers will just copy them. We can do this using the `follow` method that of the `CANSparkMax` class.

```java
  public Drive() {
      for (CANSparkMax spark : List.of(leftLeader, leftFollower, rightLeader, rightFollower)) {
	    spark.restoreFactoryDefaults();
	    spark.setIdleMode(IdleMode.kBrake);
    }
    
    rightFollower.follow(rightLeader);
    leftFollower.follow(leftLeader);
  }
```

Now, for our last setting, take a look back at the image of the drivetrain where you can see all of the electronics. Notice how the motors on the left are facing left, and the motors on the right are facing right.

By default, applying a positive voltage to the motors will make them go counterclockwise. So let's say that we want the robot to move straight, and so we apply the same positive voltage to both sides, and all of the motors move counterclockwise. Try to visualize what would happen.

Because the wheels are facing opposite directions, clockwise doesn't mean the same thing for the two sides. The left wheels will end up going backwards, and the right ones will go forwards, and instead of going straight, the whole drivetrain will rotate counterclockwise.

That's pretty confusing. Ideally, we'd like positive to mean forward for both sides. So in the code, we invert the left side. This means that it will negate every value we give it, so if we give it a positive voltage it will actually rotate counterclockwise. We do this using the `setInverted` method.

```java
  public Drive() {
      for (CANSparkMax spark : List.of(leftLeader, leftFollower, rightLeader, rightFollower)) {
	    spark.restoreFactoryDefaults();
	    spark.setIdleMode(IdleMode.kBrake);
    }
    
    rightFollower.follow(rightLeader);
    leftFollower.follow(leftLeader);

	leftLeader.setInverted(true);
  }
```
## Drive method

Now that our motors are configured, we can actually make a drive method that will allow the motors to run! This method will take in a `leftSpeed` and a `rightSpeed` which we will pass to our motors.

*Side note: calling these values speed is actually a misnomer, since they specify both speed and direction, but using the terms interchangeably is pretty standard practice in this context.*

We will be using the `set` method of the `CANSparkMax` class, which takes a number between -1 and 1, where 1 is full speed forwards, 0 is no speed, and -1 is full speed backwards. So we're actually giving percentages of our max speed, not the speed itself.

```java
  private void drive(double leftSpeed, double rightSpeed) {
    leftLeader.set(leftSpeed);
    rightLeader.set(rightSpeed);
  }
```

## Drive Command Factory

You might notice that the `drive` method above is private. But that means that we can't actually tell our robot to drive from `Robot.java`! So, why isn't it public? Well, when we tell subsystems to move, we generally always want that to be done through a `Command`, that way we can enforce the one-command-per-subsystem rule. So we actually don't want anybody outside of `Drive` to be directly calling this `drive` method.

Instead, we're going to write a *command factory*, which is just a fancy way of saying a method that returns a command. What specifically do we want our command to do? Well, our primary method of driving will be using inputs from a controller. We have an Xbox controller in `Robot.java` called `driver`, and the `leftSpeed` and `rightSpeed` values are actually going to be the y values of the left and right joysticks on that controller.

So our `drive` method should return a `Command` that drives the robot based on inputs from a controller. Since the controller is in `Robot.java`, not `Drive` (it is not part of the Drive subsystem), our method will need to take as inputs some way of retrieving the values from the controller.

Specifically, we're going to take two `DoubleSuppliers`, one for the left velocity and one for the right velocity. In `Robot.java`, we'll call our method and give it methods to get the left and right y values on the Xbox controller. So, here's our method header:

```java
public Command drive(DoubleSupplier vLeft, DoubleSupplier vRight)
```

*Note: the two `drive` methods have the same name, but are not the same method. As long as the types of the parameters are different, you can have multiple methods with the same name.*

Next up, let's decide what type of Command we want to use. This isn't just something we want to do once - we need to get new inputs from the controller each tick - so we'll use a run command. We've talked about `Commands.run`, but in a Subsystem there's actually another method just called `run`, which calls `Commands.run` but uses that subsystem as the requirement. So `drive.run(action)` is the same as `Commands.run(action, drive)`. That's the method we're going to use for this, since we want to create a `RunCommand` that requires a drive subsystem.

And the action is just going to be calling the other `drive` method using `vLeft` and `vRight`!

```java
  private Command drive(double vLeft, double vRight) {
    return run(() -> drive(vLeft.getAsDouble(), vRight.getAsDouble()));
  }
```
# Driving with the controller

Now we're going to go to `Robot.java` and write the code to actually drive the robot using the driver controller!

There should already be two `CommandXboxController` objects called `operator` and `driver` defined at the top of the class. You can delete the `operator` controller, and we'll use the `driver` one for driving.

Next up, we need to actually create our instance of the drive subsystem! You can do this right under the comment that says `// SUBSYSTEMS`:

```java
  Drive drive = new Drive();
```

Now that we have our drivetrain initialized, we can set up driving with controllers. We're going to do that by setting a *default command* for drive. A default command is a command that runs on a subsystem whenever no other commands that require that subsystem are running. For drive, if we're not telling it to do something else, we always want it to be listening to the controller and driving.

We set a subsystem's default command using `subsystem.setDefaultCommand(command)`. And we do those configurations in the `configureBindings` method inside of `Robot`. This method (along with `configureGameBehavior`) is called by `Robot`'s constructor, and are used to configure settings that need to be configured right when the robot is started up.

```java
  private void configureBindings() {
	drive.setDefaultCommand(drive.drive(driver::getLeftY, driver::getRightY));
}
```

Now, if you had a real robot to test on, it would drive!! But knowing that would probably be more exciting if you could see and drive around some sort of simulation. Unfortunately, we can't do that yet because to simulate the movement of the robot, we would need an estimate for where the robot is on the field, which we don't have yet. So let's work on getting that.
# Odometry

*Odometry* is the process of using data from sensors to estimate your position and how it changes. In this case, the sensors that we'll be relying on are encoders (for our wheels) to and a gyroscope.

Brush up on the [sensors guide](/reference-sheets/Sensors.md) if you're uncertain what encoders and gyros are.
## Adding encoders

Our first step is to add encoders to our `Drive` subsystem. We'll be using the relative encoders that are built-in to our sparks. We can get them using the `getEncoder` method of `CANSparkMax`.

You can add the encoders right under where the sparks themselves are declared. Note that we only need the encoders of the leaders, because the followers should be doing the same thing as the leaders!

```java
  private final RelativeEncoder leftEncoder = leftLeader.getEncoder();
  private final RelativeEncoder rightEncoder = rightLeader.getEncoder();
```
### Conversion factors

By default, the encoders measure rotations of the motors. But we want to measure distance traveled. There are a couple of conversions that we need to make to do that:
1. From rotations of the motor to rotations of the wheel
	- This is dependent on the gears that connect the motor to the wheel.
2. From rotations of the wheel to distance traveled
	- This is dependent on the radius of the wheels. One rotation of the wheel translates to traveling one circumference of the wheel.

So to convert between encoder readings, we need to know the gearing (wheel rotations per motor rotation) and circumference of the wheels. We can put these values in the `DriveConstants.java` file. We'll choose some arbitrary values, but if you're testing on a real robot make sure these values are accurate.

```java
package robot.drive;

public class DriveConstants {
  public static final double WHEEL_RADIUS = 0.08; //Meters
  public static final double CIRCUMFERENCE = 2.0 * Math.PI * WHEEL_RADIUS;
  public static final double GEARING = 8.0;
}
```

Then, from these values we can calculate our conversion factor for position. This is the number that we multiply the encoder rotations by to get distance traveled. We need to multiply by gearing to convert to wheel rotations, and then by circumference to convert to distance.

```java
  public static final double POSITION_FACTOR = CIRCUMFERENCE * GEARING;
```

We also need to calculate a separate conversion factor for velocity. The encoder by default gives you velocity in rotations per minute. We want it in meters per second. We can use the `POSITION_FACTOR` to convert to meters, and divide by 60 to convert from minutes to seconds.

```java
  public static final double VELOCITY_FACTOR = POSITION_FACTOR / 60.0;
```

Now we just need to use the conversion method from the encoder class in `Drive.java`.

```java
    leftEncoder.setPositionConversionFactor(DriveConstants.POSITION_FACTOR);
    rightEncoder.setPositionConversionFactor(DriveConstants.POSITION_FACTOR);

    leftEncoder.setVelocityConversionFactor(DriveConstants.VELOCITY_FACTOR);
    rightEncoder.setVelocityConversionFactor(DriveConstants.VELOCITY_FACTOR);
```
### Resetting the Encoders

At the start of the match (or any time you need to reset the robot's position), it's important to reset the encoder values to zero. This ensures that your distance calculations start from a known point.

We'll reset the encoders during the subsystem initialization (in the Constructor):

```java
    leftEncoder.setPosition(0);
    rightEncoder.setPosition(0);
```
## Adding a gyroscope

We're going to use the `AnalogGyro` class. We need to give the port of the gyro to the constructor, so we need to add that port in `Ports.java`. (Make up any integer that isn't already used).

Let’s add the AnalogGyro to the existing `Drive.java` file:

```java
  private final AnalogGyro gyro = new AnalogGyro(Ports.Drive.GYRO_CHANNEL);
```
### Resetting the Gyro

At the start of the match, it's important to reset the gyro so that your heading starts at 0. We'll do that in the constructor of `Drive.java`.

```java
  gyro.reset();
```

 You should reset the gyroscope anytime you need to ensure accurate heading data. Sudden robot movements, collisions, or physical rotation of the surface it is on can cause drift or skips over time, resulting in an incorrectly measured angle over the course of a match. Resets can correct for this.
## Adding Odometry

Using the encoders and gyro we just made, we can start actually estimating our position. We do this using a WPILib class called [DifferentialDriveOdometry](https://docs.wpilib.org/en/stable/docs/software/kinematics-and-odometry/differential-drive-odometry.html), which helps estimate the position and angle on the field of a differential drive bot, using encoder and gyro values. Let's start by declaring a `DifferentialDriveOdometry` object at the top of our `Drive` subsystem.

```java
  private final DifferentialDriveOdometry odometry;
```
### Initializing Odometry

We declared our odometry already, but we still need to initialize it. Odometry needs an initial orientation for the robot, so we're just going to assume that it starts at the origin with a heading of 0.

Read [this](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/geometry/pose.html) for a brief explanation of `Rotation2d`, `Translation2d`, and `Pose2d`.

Here’s how we initialize the odometry in the constructor:

```java
    odometry = new DifferentialDriveOdometry(
            new Rotation2d(), 
            0, 
            0, 
            new Pose2d());
```

`new Pose2d()` just creates a `Pose2d` where all angles and coordinates as 0.
###  Updating odometry

To keep track of the robot’s position in real-time, we need to update the odometry regularly with the latest encoder readings.

Here's how you might update odometry:

```java
  public void updateOdometry(Rotation2d rotation) {
    odometry.update(rotation, leftEncoder.getPosition(), rightEncoder.getPosition());
  }
```

*Note: We are passing in rotation as a parameter because once we want to simulate our robot, it'll be easier to distinguish between our real and sim rotation.*

Aside from updating our odometry, we might need to reset it. I will leave this up to you to figure out how to do. (Hint: `odometry` has a method called `resetOdometry`). We won't need it for this project but if you're using the drive for autos example, it is important to reset your odometry whenever autos start.

To ensure that our odometry is constantly updating as the robot moves, we run the `updateOdometry()` method periodically every tick (0.02 seconds by default). This will go in the `periodic()` method which all subsystems inherit from `SubsystemBase`, and is called every tick.

```java
  @Override 
  public void periodic() {
    updateOdometry(gyro.getRotation2d());
  }
```

Keep in mind, this will be changed in the simulation section to account for sim rotation.

## Getting pose

The last thing to finish up our basic drive will be to get our pose based on the odometry. We can do this by using the `getPoseMeters` method from `odometry`. Keep in mind this returns a Pose2d. We want the robot's pose to be easily accessible by other classes, so we'll create a public method in `Drive` that returns the pose.

```java
  public Pose2d pose() {
    return odometry.getPoseMeters();
  }
```
# Simulating

Now we've reached the point where we can actually simulate our robot and drive it around!
# Simulation and Logging

To finish our project up, we are going to simulate the drive we've made. Please read the [Simulation guide](/reference-sheets/Simulation.md) before continuing on with this.
## Setting Up the Simulation

To [simulate the drivetrain](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/drivesim-tutorial/index.html), we’re going to use the `DifferentialDrivetrainSim` class. This simulation will model the physical characteristics of our robot—like the motors, mass, and wheel dimensions—so we can see how the code will affect the robot in a virtual environment.

Here’s how we set it up in our `Drive.java` constructor:

```java
  private final DifferentialDrivetrainSim driveSim;
  // ...
  public Drive() {
    // ...
    driveSim =
        new DifferentialDrivetrainSim(
            DCMotor.getMiniCIM(2),
            DriveConstants.GEARING,
            DriveConstants.MOI,
            DriveConstants.DRIVE_MASS,
            DriveConstants.WHEEL_RADIUS,
            DriveConstants.TRACK_WIDTH,
            DriveConstants.STD_DEVS);
    //...
  }
```

Remember that all of these values would be stored in `DriveConstants.java`:

```java
  public static final double TRACK_WIDTH = 0.7112; // Meters
  public static final double WHEEL_RADIUS = 0.08; //Meters
  public static final double GEARING = 8.0;
  public static final double MOI = 7.5;
  public static final double DRIVE_MASS = 60.0; //kg
  public static final Matrix<N7, N1> STD_DEVS = VecBuilder.fill(0, 0, 0, 0, 0, 0, 0);
```

By setting up the simulation with these constants, we’re creating a physics model of our robot that behaves similarly to how it would in real life.

Before we start periodically updating our sim values, make sure to set the voltage to our sim drive in the `drive` method:

```java
    driveSim.setInputs(leftVoltage, rightVoltage);
```

Last thing to set up will be our sim rotation that was previously mentioned. We'll start by making a new `Rotation2d`:

```java
  private Rotation2d simRotation = new Rotation2d();
```

Then simply change our `updateOdometry` method in `periodic()` to account for our new rotation.

```java
  public void periodic() {
    updateOdometry(Robot.isReal() ? gyro.getRotation2d() : simRotation);
  }
```

- `Robot.isReal()` returns whether or not we are connected to a real robot
- What do the `?` and `:` do? That whole statement is referred to as a [ternary operator](https://www.baeldung.com/java-ternary-operator).
- We will update our `simRotation` value in `simulationPeriodic` as seen below.
### Simulation periodic

The `simulationPeriodic` method is where we update the simulation. This method is called regularly during the robot’s operation to keep the simulated sensors and drivetrain in sync with the rest of the code. The `@Override` annotation above the method is there so that the compiler knows it's the inherited method from `SubsystemBase`. However, it isn't neccessary to include.

```java
  @Override
  public void simulationPeriodic() {
    // sim.update() tells the simulation how much time has passed
    driveSim.update(Constants.PERIOD.in(Seconds));
    leftEncoder.setPosition(driveSim.getLeftPositionMeters());
    rightEncoder.setPosition(driveSim.getRightPositionMeters());
    simRotation = driveSim.getHeading();
  }
```

- `leftEncoder.setPosition` and `rightEncoder.setPosition` update the simulated encoder positions to match the simulated robot’s movement.
- `simRotation`: Updates the simulated Rotation2d based on the robot’s simulated heading.

This method ensures that our simulated sensors provide accurate feedback as the robot "moves" in the simulation, allowing us to test and tweak our code.
## Logging: Capturing Important Data

Now let’s talk about logging. Logging is crucial for understanding how our robot behaves over time, diagnosing issues, and improving performance. We’re going to use Monologue for logging, which gives us a structured way to record and analyze data from the robot’s systems.

This should already be set up in the `configureGameBehavior` method in `Robot.java`. You should see the following lines:

```java
    Monologue.setupMonologue(this, "/Robot", false, true);
    addPeriodic(Monologue::updateAll, kDefaultPeriod);
    addPeriodic(FaultLogger::update, 1);
```

This initializes Monologue with our robot, setting up the logging system to capture data as the robot runs and makes sure Monologue logs data at regular intervals, which we’ve defined with kDefaultPeriod. By logging data regularly, we can later review how the robot performed and make informed adjustments to our code.

### Using Monologue for NetworkTables Logging

We use NetworkTables (NT) to make logging specific variables or objects easier. Read the [Telemetry doc](/reference-sheets/Telemetry.md) for specifics on logging with NT. Any values that may be useful for debugging should be logged, including currently running commands, joystick inputs, voltages, positions, etc..

We’re going to use the `@Log.NT` annotation as it allows us to log key metrics in real-time while the robot is running, which we can then view on dashboards like Shuffleboard or SmartDashboard.

Let's get started by making a field:

```java
  @Log.NT private final Field2d field2d = new Field2d();
```

One other thing we're going to log is going to be our position on the field. Simply use the annotation on the `pose` method:

```java
  @Log.NT
  public Pose2d pose() {
    return odometry.getPoseMeters();
  }
```

Another quick little thing we're going to log is the distance travelled by our motors. Like before, we create a getter method that returns what we want and annotate it with `@Log.NT`, allowing us to see and interact with it in sim.

```java
  @Log.NT
  public double getDistance() {
    return (leftEncoder.getPosition() + rightEncoder.getPosition()) / 2;
  }
```

By logging these values, we can gain real-time insights into our robot’s performance, which is essential for making data-driven decisions and quickly diagnosing issues.

### Updating the Robot: periodic

Finally, the periodic method is where we update various elements of the robot regularly during operation. It’s like the heartbeat of our subsystems. Specifically, we are going to update the field display with the robot’s current position, which helps us visualize its movement.

```java
    field2d.setRobotPose(pose());
```
## Seeing the result

Start by launching sim and opening up NetworkTables. Use the [sim gui guide](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/simulation-gui.html) to help you navigate around. 

To see our `Field2d` widget, go to NetworkTables, then SmartDashboard, and click "field". 

Next, to see our logged data, click NetworkTables and the first option. You should see something similar to the image below.

![drive NT](https://github.com/user-attachments/assets/2be285f4-a3ea-40f5-bdf7-e9bb661f44ba)

Since our driver port is 1, make sure your joystick is also on the same port value in sim or else it will not get any inputs. 

Lastly, to control the differential drive properly, the joystick will require to have 6 total `axis` as shown below. You can add more and change the bindings by going to `DS` then clicking on the settings of which ever keyboard you are using.

![drive joystick](https://github.com/user-attachments/assets/a6624ad8-f944-4e62-bc4d-a29eda974891)
# Control Theory

Before we get started, please make sure you have read the [Control Theory reference sheet](/reference-sheets/Control-theory.md) as we are going to assume you are aware of what PID and Feedforward generally do.
#### Why Control Theory Matters for Driving

Before we dive into the code, let’s touch on why control theory is essential. For a robot to move precisely and respond accurately to commands, simply sending raw motor commands isn’t enough. We need to ensure that the robot can handle changes in conditions, like different terrains or obstacles, while still following the desired path. Control theory helps us achieve this by using techniques like PID and feedforward control to manage motor responses.
#### Setting Up PID Controllers

Let’s start by setting up the PID controllers. These controllers will help keep the motor speeds on track by constantly adjusting based on the difference between the desired and actual speeds. 

```java
  private final PIDController leftPIDController =
      new PIDController(PID.P, PID.I, PID.D);
  private final PIDController rightPIDController =
      new PIDController(PID.P, PID.I, PID.D);
```
#### Adding Feedforward Control

Next, we incorporate feedforward control. While PID handles errors after they occur, feedforward focuses on already known phyiscal disturbances like friction of a system to manipulate its inputs.

```java
  private final SimpleMotorFeedforward feedforward = new SimpleMotorFeedforward(FF.S, FF.V);
```

- The PID and FF values are stored in `DriveConstants.java` and are imported. Keep in mind these are just basic values to get you started with the project. The process to determine these values will be elaborated on later.

```java
  public static final class PID {
    public static final double P = 8.5;
    public static final double I = 0.0;
    public static final double D = 0.0;
  }

  public static final class FF {
    public static final double S = 1;
    public static final double V = 3;
  }
```
#### Integrating PID and Feedforward

Now, let’s see how these two control mechanisms work together. We’ll look at the drive method, which is responsible for controlling the motor voltages.

```java
  public void drive(double leftSpeed, double rightSpeed) {
    final double leftFeedforward = 
      feedforward.calculate(leftSpeed * DriveConstants.MAX_SPEED);
    final double rightFeedforward = 
      feedforward.calculate(rightSpeed * DriveConstants.MAX_SPEED);
  }
```

- `MAX_SPEED` is defined in DriveConstants as such:

```java
  public static final double MAX_SPEED = 2; // Meters per second
```
As you know, the inputs we receive will be between -1 and 1. So by multiplying by our max speed, we can vary the range of the speed at which our robot moves. 

Here, we’re calculating the feedforward voltage for each wheel based on the target speed. This helps to ensure that the motors get an initial boost that’s closer to what they need.

Next, we add the PID control:

```java
    final double leftOutput = 
      leftPIDController.calculate(leftEncoder.getVelocity(), 
      leftSpeed * DriveConstants.MAX_SPEED);
    final double rightOutput = 
      rightPIDController.calculate(rightEncoder.getVelocity(), 
      rightSpeed * DriveConstants.MAX_SPEED);
```

In this part, the PID controllers calculate how much they need to adjust the motor speed to correct any errors. They do this by comparing the actual speed (from the encoders) with the target speed.

Finally, we combine the outputs and send them to the motors:

```java
      double leftVoltage = leftOutput + leftFeedforward;
      double rightVoltage = rightOutput + rightFeedforward;

      leftLeader.setVoltage(leftVoltage);
      rightLeader.setVoltage(rightVoltage);
```

Here, the final motor voltage is calculated by adding the PID and feedforward outputs together. These voltages are then sent to the motors, controlling the movement of the robot.
# Unit Testing & System Checks

#### Unit Tests

Think of unit tests as a way to check that each small piece of your code—like a motor or sensor—is functioning properly on its own before you start putting them all together. It's much easier to fix problems when they’re isolated to a single component than when they’re all tangled up in the full system.

Let’s talk about the tests for our drivetrain. We'll start it by creating a `DriveTest.java` file in the robot folder of the tests folder.

First, we need to set things up before we run any tests. This is done in the `setup()` method:

```java
  Drive drive;

  @BeforeEach
  public void setup() {
    setupTests();
    drive = new Drive();
  }
```

Next, we will need to reset our drive between every test in order to experiment with different things at once.

```java
  @AfterEach
  void destroy() throws Exception {
    reset(drive);
  }
```

Once everything is set up, you can make tests with the `@Test` annotation. Here's a quick example of testing if our pose is changing as we drive. 

The `fastForward` allows time to pass to give our drive time to move. 

Then we call our `getPose()` method and compare it to a new Pose2d, which returns a value of 0. So this test ensures that whenever our drive method is called, the robot doesn't stay at the Pose2d but actually moves.

```java
  @Test
  public void testPose() {
    drive.drive(0.8, 0.8);
    fastForward();

    assertNotEquals(new Pose2d(), drive.getPose());
  }
```
#### Running the tests

To actually see if the tests are valid, open the WPILib command palette (top right corner logo) and search `Test Robot Code` and press enter. After it runs, it will show you the results of all your tests in the terminal.  

An alternative to this is using the *Test Runner* extension from vscode:

![Test runner](https://github.com/user-attachments/assets/6431c054-a699-4c45-806d-f7cbd41881ce)

![test pass](https://github.com/user-attachments/assets/28b6ac83-788a-4ec7-a0f1-7a82375a6428)

A step up from our previous test would be to see if the robot is actually moving in the right direction or try to predict the general x value of your pose. Here is a version of how you can do that:

```java
 @Test 
  public void testDirection(){
    double deltaT = 2;
    
    drive.drive(0.5, 0.5);

    fastForward(Seconds.of(deltaT));

    assert(drive.getPose().getX() > 1);
  }
```
Try to do the same but for the opposite direction and testing it out. 

Next, we need to create a `RobotTest` to ensure our `Robot` class functions correctly. This test checks that we can instantiate the `Robot` and call its `close()` method without any exceptions, which is essential for managing resources properly—like ensuring that motors, sensors, and memory are correctly initialized and released when no longer needed.

```java
public class RobotTest {
  @Test
  void initialize() throws Exception {
    new Robot().close();
    UnitTestingUtil.reset();
  }
}
```

Unit tests should be made for all key subsystems and are a great way to see if the logic behind the code actually makes sense and works. You should also try to test all parts of the subsystems to cover everything.  

The final type of assert most commonly used in tests is the `assertEqual`. This simply tests if two values are the same. Both in assertEqual and assertNotEqual, you can pass in a tolerance value that will pass the test if the two different values are within the tolarence. This is usually done by having a `DELTA` value set to your prefered tolarence.
#### System Checks

In addition to unit tests, it’s equally important to perform system checks to ensure the entire robot is operating as expected in real-world conditions. Think of system checks as a quick health check before it hits the field. You want to make sure that everything is working as it should—motors, sensors, and all. This is usually done in real life and it's a good habit to run full robot system checks before your matches.

Here is a simple example of what a drive systems check might look like. The logic is similar to unit tests as we will run a part of the drive before checking to see if it meets expectations. Remember to import the SciBorgs' testing libraries and not the built-in WPILib class. Note that this is created in the subsystem because of easy access to internal methods to check conditions.

Step 1: Define the command to run the system check

```java
  public Test systemsCheck() {
    Command testCommand = run(() -> drive(-0.8, -0.8)).withTimeout(0.5);
  }
```

Step 2: Define the assertions

```java
    Assertion leftMotorCheck = Assertion.tAssert(
        () -> leftLeader.getAppliedOutput() > 1,
        "Drive System Check Left Motor Output",
        "Expected left motor output to be greater than 1");

    Assertion rightMotorCheck = Assertion.tAssert(
        () -> rightLeader.getAppliedOutput() > 1,
        "Drive System Check Right Motor Output",
        "Expected right motor output to be greater than 1");
```

- `tAssert` is a truth assert that asks for a condition, a fault name, and a little description of what we're actually checking.

Step 3: Combine the command and assertions into a `Test`

```java
    Set<Assertion> assertions = Set.of(leftMotorCheck, rightMotorCheck);
    return new Test(testCommand, assertions);
```
#### Running systems check

To run the systems check, we use the `Test` mode of the robot. To get started, we need to make a command that's going to run whenever we enable `Test` mode using the built-in `test()` trigger. All of this is done in `Robot.java`. Keep in mind that this method would be responsible for the systems checks of all your subsystems, not just drive.

```java
  public Command systemsCheck() {
    return Test.toCommand(drive.systemsCheck());
  }
```

To actually run this in test, we tell it to run the previous command whenever test mode is enable. (This is done in `configureBindings`):

```java
    test().whileTrue(systemsCheck());
```
#### Viewing results

This is probably the most important part of systems check, checking if our tests passed. Using `FaultLogger`, we are able to pass the results of our checks into NetworkTables and see them in both sim and `Elastic`.  

- Elastic is a dashboard that's great use for drive team as it lets you see a bunch of robot data on a nice layout. You don't necessarily need this app for the project and can view this in sim.

Make sure you are periodically updating FaultLogger in `Robot.java`.

```java
    addPeriodic(FaultLogger::update, 2); 
```

Now launch the sim window (ctrl + shift + p) -> `simulate robot code`.
Once it's loaded, click the `Test` mode and then open NetworkTables info.

![NT faults](https://github.com/user-attachments/assets/1426c12d-7af7-4c33-8a99-53427df4cf31)

In Faults and Total Faults, we can see that we have indeed ran our checks and since there are no warnings, it is safe to assume that in this case the checks have passed.

- To see this in Elastic, click `Test` and then head to Elastic. Right click, click add widgets, click `Faults` and drag and drop `Total Faults` and `Active Faults` onto the layout. You should see the following if the tests have passed.

![elastic faults](https://github.com/user-attachments/assets/0442431c-b250-43bb-a9de-e89285fc71dc)

Same with Unit Tests, it's good to have system checks for all runnable parts of the robot to ensure the robot is fully ready for the game. As a notice, please make sure to run system checks while the robot is **ON** the robot cart.
## Bonus

If you don't like the two-handed control of a differential drive, take a shot at an arcade drive. Use the `DifferentialDrive` class from WPILib and make use of its `arcadeDrive` methods. An arcade drive functions like your generic video game character. The y axis of your left joystick can be used for forward/backward movement and the x axis for right/left movement. However, for our case the right and left would mean turning. 
## Continuing on

Once you feel ready for the next step, get started on the ArmBot project. It's going to have a different code structure than we discussed, but many of the ideas still remain. You can get started [here](/projects/BasicArmBot.md).

Sneak peek:

![arm gif](https://camo.githubusercontent.com/0fa588f2e99bfd0489a858dbc10bfddb918ae57cbf9987017c9c4af91863edd9/68747470733a2f2f692e6779617a6f2e636f6d2f63623631383964306335386333633238663835353863663838616638323766662e676966)
