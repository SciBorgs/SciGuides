# Basic Arm Bot Tutorial

![Simulated arm moving side to side](https://i.gyazo.com/cb6189d0c58c3c28f8558cf88af827ff.gif)

## Description & Prerequisites

In this tutorial, you will write code for a robot with a single-jointed arm and simulate its movement. The desired robot will have a single arm joint with an elevated axis of rotation, equipped with a static (non-pivoting) intake mechanism at the end of the arm.

You are expected to have completed some level of the [Differential Drive projects](/DifferentialDriveBasic.md), as this project will build upon that codebase. You should also be familiar with the concepts and usage of interfaces, inheritance, and the command-based paradigm.

All code examples are subject to change as a result of future library updates and improvements.

## Setting up your environment

Using your knowledge of Git, create a new branch for your arm bot. Name it something like `basic-arm-bot`. *Make sure to also move to that branch!*
If unfamiliar, please check our style sheet for ideal code and git practices.

[comment]: # (add style sheet link when completed)

Before you move on, create an `Arm.java` subsystem and an associated `ArmConstants.java` file in the robot folder of your project.

## Creating your arm

Before we start, we'll be abstracting the hardware components to streamline our code.

Moving hardware like motors and encoders to class implementations of an interface decouples them from subsystem code, enabling modularity that supports simulation and flexibility in using different hardware or none at all! For a deeper dive, you should look at our [hardware abstraction datasheet](/HardwareAbstraction.md).

Begin by creating your first IO interface in its Java file. This will act as an abstraction for a real and simulated set of hardware, so only include method headers that you think they will share.

It should look something like this:

```java
public interface ArmIO {
    void setVoltage(double voltage); // reminder: interfaces only have method headers;

    double position(); // all method bodies are specified in classes that implement ArmIO!
} 
```

Now, create a real implementation of your `ArmIO` named `RealArm` in its own file.

Think about what kind of hardware sensors the robot should use, especially when thinking about the encoder. See our [sensors doc](/reference-sheets/Sensors.md) for background.

Since we want to know exactly where our arm is at all times, we will use absolute encoders. WPILib has support for RIO-connected absolute encoders with `AnalogEncoder` and [`DutyCycleEncoder`](https://github.wpilib.org/allwpilib/docs/release/java/edu/wpi/first/wpilibj/DutyCycleEncoder.html); we'll be using the latter.

Following Java rules, `RealArm` must implement the bodies of the three methods above. Try it on your own before looking at the snippets below, and remember your goal!

We create our hardware components...

```java
public class RealArm implements ArmIO {
    private final PWMSparkFlex motor = new PWMSparkFlex(0);
    private final DutyCycleEncoder encoder = new DutyCycleEncoder(1);

    public RealArm() {
        // ...
    }
}
```

...and create implementations for the methods in `ArmIO`.

```java
    @Override
    public void setVoltage(double voltage) {
        motor.setVoltage(voltage);
    }

    @Override
    public double position() {
        return encoder.get();
    }
```

Now, create a [simulated implementation](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/physics-sim.html) of `ArmIO` called `SimArm`.

WPILib has many classes to simulate numerous different types of mechanisms, seen [here](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/physics-sim.html#wpilib-s-simulation-classes). It'll look very similar to the above, only that the motor and encoder will be simulated by WPILib's `SingleJointedArmSim` class.

### Constants

Digging deep into the innards, you'll notice that the constructors are BIG.

```java
    // One of its many constructors; this is the one that we will be using
    public SingleJointedArmSim(
      LinearSystem<N2, N1, N1> plant,
      DCMotor gearbox,
      double gearing,
      double armLengthMeters,
      double minAngleRads,
      double maxAngleRads,
      boolean simulateGravity,
      double startingAngleRads)
```

[comment]: # (might just include the ArmConstants file in the template)

They need a plethora of physical information to be able to accurately simulate your system, and we obviously don't have a real robot. All this information will also require a lot of organization.

For your convenience, you may copy-paste these relevant predetermined constants into `ArmConstants`:

```java
    import static edu.wpi.first.units.Units.*;

    // ...

    /**
     * The factors by which encoder measurements are different from actual motor rotation; default
     * units.
     */
    public static final double MOTOR_GEARING = 12.0 / 64.0 * 20.0 / 70.0 * 36.0 / 56.0 * 16.0 / 54.0;

    public static final double THROUGHBORE_GEARING = 16.0 / 54.0;

    /** Unit conversions objects for the encoders. Uses the Java units library. */
    public static final Measure<Angle> POSITION_FACTOR = Rotations.of(THROUGHBORE_GEARING);
    public static final Measure<Velocity<Angle>> VELOCITY_FACTOR = POSITION_FACTOR.per(Minute);

    /** Offset from the center of the robot to the pivot's axis of rotation */
    public static final Translation3d AXLE_FROM_CHASSIS =
        new Translation3d(Inches.of(-10.465), Inches.zero(), Inches.of(25));

    /** The arm's moment of inertia; resistance to rotational movement. */
    public static final Measure<Mult<Mult<Distance, Distance>, Mass>> MOI =
        (Meters).mult(Meters).mult(Kilograms).of(0.17845);

    public static final Measure<Angle> POSITION_TOLERANCE = Degrees.of(0.8);

    public static final Measure<Mass> MASS = Kilograms.of(1);
    public static final Measure<Distance> LENGTH = Inches.of(16);

    public static final Measure<Velocity<Angle>> MAX_VELOCITY = RadiansPerSecond.of(4);
    public static final Measure<Velocity<Velocity<Angle>>> MAX_ACCEL =
        RadiansPerSecond.per(Second).of(6);

    public static final Measure<Angle> STARTING_ANGLE = Degrees.of(20);

    public static final Measure<Angle> MIN_ANGLE = Degrees.of(-45);
    public static final Measure<Angle> MAX_ANGLE = Degrees.of(225);

    public static final double kP = 8.0;
    public static final double kI = 0.0;
    public static final double kD = 0.5;

    public static final double kS = 0.14296;
    public static final double kV = 1.7305;
    public static final double kA = 0.01;
    public static final double kG = 0.12055;
```

Note the `Measure<T>` constants; this is part of WPILib's [Java Units Library](https://docs.wpilib.org/en/stable/docs/software/basic-programming/java-units.html), which helps ensure correct units are used throughout the code. You'll see it used later on as well.

One last we can add are static imports, which will save a bit of space. At the top of `SimArm`, type

```java
import static org.sciborgs1155.robot.arm.ArmConstants.*;
```

to import all static objects in `ArmConstants` and simplify `ArmConstants.MAX_VELOCITY` to `MAX_VELOCITY`.

Only use static imports for constants and when it makes sense stylistically and syntactically.

### Finishing up

Initialize your arm simulator with the new constants, like below...

```java
  private final SingleJointedArmSim sim =
      new SingleJointedArmSim(
          LinearSystemId.createSingleJointedArmSystem(
              DCMotor.getNEO(4),
              MOI.in((Meters).mult(Meters).mult(Kilograms)),
              1.0 / MOTOR_GEARING),
          DCMotor.getNEO(4),
          1.0 / MOTOR_GEARING,
          -LENGTH.in(Meters), // the Units library in action
          MIN_ANGLE.in(Radians), // initialized as degrees, converted to radians
          MAX_ANGLE.in(Radians), // as required by the constructor
          true,
          STARTING_ANGLE.in(Radians));
```

...and implement the ArmIO methods using the methods provided by the sim. Be sure to update the sim periodically in your input methods with its `update(double dtSeconds)` method.

```java
    sim.setInputVoltage(voltage);
    sim.update(PERIOD.in(Seconds)); // every 0.02 secs
```

To complete this IO subsystem, create the last implementation called `NoArm`. It should describe a non-existent arm, without any hardware but with methods returning 0 or doing nothing.

This class is useful for when a mechanism is broken or is not on the robot, allowing us to run the rest of the robot without major errors.

### Subsystem Integration

Now, it's time to work with the actual subsystem. `Arm.java` should include a few things:

- IO implementations of the hardware (that we just created!)
- any control run on the RoboRIO (versus a motor or other hardware)
- all [commands](/reference-sheets/Command-based.md#commands), command factories, and related methods

Think about how exactly we want our arm to act. It should be quick, but safe.

For a long and heavy arm (relative to other mechanisms), it's dangerous to use a regular PID controller, which will command the arm straight down at high speeds.

| ![Arm with regular PID](https://i.gyazo.com/37f07bb43986f5102ebde16da9a641f8.gif) | ![Simulated arm moving side to side](https://i.gyazo.com/cb6189d0c58c3c28f8558cf88af827ff.gif) |
|:--:|:--:|
| Regular PID; with identical constants | ProfiledPID; with constraints |

Of course, we still want the arm to reach the setpoint quickly.

A smoother alternative to the regular PID would be the addition of a trapezoid profile. Velocity will increase, coast, and then decrease over time under a set of velocity and acceleration limits to reach a goal smoothly, plotting a graph in the shape of a trapezoid. WPILib has [its own implementation of this](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/controllers/profiled-pidcontroller.html) in `ProfiledPIDController`. *Please read the docs*.

Considering that the mechanism is an arm, it should be intuitive that gravity will have a much greater (non-negligible) effect on it than other mechanisms. To account for this, we can use [WPILib's `ArmFeedForward`](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/controllers/feedforward.html#armfeedforward), which incorporates a G term for output.

The top of your file should look similar to this:

```java
import static org.sciborgs1155.robot.arm.ArmConstants.*;

public class Arm extends SubsystemBase implements Logged {
    // We declare our objects at the top...
    private final ArmIO hardware;
    private final ProfiledPIDController pid;
    private final ArmFeedforward ff;

    public Arm(ArmIO hardware) {
        // ...and initialize them in the constructor (for stylistic purposes).
        this.hardware = hardware;
        pid = new ProfiledPIDController(kP, kI, kD, new TrapezoidProfile.Constraints(MAX_VELOCITY, MAX_ACCEL));
        ff = new ArmFeedforward(kS, kV, kA);

        // set tolerance since setpoint will never be reached
        pid.setTolerance(POSITION_TOLERANCE.in(unit-of-choice));
        // unit should be same as input unit
  }
  // ...
}
```

Now, let's create our command factories to make this arm move given a certain goal to reach. If you haven't already, read the [`ProfiledPIDController` docs](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/controllers/profiled-pidcontroller.html) for usage details and clarifications.

First, we'll create a non-factory method to set voltage with our controllers given a goal. This helps us avoid use of a multi-line lambda in the command factory.

```java
  public void updateGoal(double goal) {
    double pidOutput = pid.calculate(hardware.position(), goal);
    // Notice the distinction between goal and setpoint; 
    // the feedforward uses the pid's newly generated setpoint as input
    // and thus will help reach that setpoint.
    double ffOutput = ff.calculate(pid.getSetpoint().position, pid.getSetpoint().velocity);
    hardware.setVoltage(pidOutput + ffOutput);
  }
```

Then, we'll use this method in our command factory. Think about how we want to ideally control it.

Hint: we'd want to repeatedly run the method above until we reach our goal, after which we stop the arm (and the command!). Never forget your end condition & behavior.

It'll look something like this:

```java
    public Command moveTo(double goal) {
        return run(() -> updateGoal(goal)).until(pid::atGoal).finallyDo(() -> hardware.setVoltage(0));
        // repeatedly runs the updateGoal() method with the given goal until the arm has reached that goal, and ensures stopping on completion
    }
```

You might even want to [overload](https://www.w3schools.com/java/java_methods_overloading.asp) it to take in a goal using the Units library, but that's just for safety and not strictly required.

Finally, make a static `create()` method that will actually instantiate the `Arm` with IO implementations. You can read on why we do this in our style sheet.

[comment]: # (add style sheet link when completed)

```java
    /**
     * A factory to create a new arm based on if the robot is real or simulated.
     */
    public static Arm create() {
        return Robot.isReal() ? new Arm(new RealArm()) : new Arm(new SimArm());
    }
```

We use the ternary operator; if the robot is real, we create the subsystem with real hardware, otherwise we create the subsystem with simulated hardware.

## Organizing the file system

With the introduction of this IO system, notice the substantial number of files. Multiply that by the two additional subsystems, and that makes for an unreadable file system. So, let's change that.

On the SciBorgs, subsystem files and their constants are put in one specific subsystem folder. This folder is located in a subsystems folder on the same level as the key robot files, defining the levels of contact each part of the robot should have with each other. In other words...

```text
├── Autos.java
├── Constants.java
├── Main.java
├── Robot.java
└── subsystems
    └── arm
        └── Arm.java
        └── ArmIO.java
        └── RealArm.java
        └── SimArm.java
        └── NoArm.java
        └── ArmConstants.java
    └── claw
        └── ...
    └── ...
```

This file system structure can be referenced at any time here, or in our style sheet.

[comment]: # (add style sheet link when completed)

## Making the claw

Congrats! We've learned how to make an IO subsystem, so now's the time you put your skills to the test. Write IO subsystem code for the static claw at the end of the arm.

Think about the requirements of this claw. Here's a hint: how fast the claw runs is nearly irrelevant for what the claw should do. Its only goal is to intake, hold, and spit out whatever's in its grasp when told to.

In the same vein, it won't be substantial to create a simulated version; we don't care about simulating it, unless we want to make a full-fledged game relying on intaking (maybe a cool idea)?

Try to do this one by yourself!

For reference, the generic IO interface for the claw only really needs one method to run the rollers and pick up gamepieces.

## Converting the drivetrain

Here's your final challenge! Turn your basic drivetrain subsystem to a subsystem implementation. If you've completed the previous Differential Drive projects, you should have everything good to go. Good luck!

## Simulating the arm

Now that you've completed all of your subsystems and mechanisms, it's time for the fun part. Piecing it all together!

For starters, get set up and get the gist of what's happening in [our simulation docs](/Simulation.md). You'll be using a `Mechanism2d` to simulate your arm, like in the blocky arm you saw at the beginning of the tutorial.

We'll only be simulating the arm; the claw won't be that useful.

Follow [these docs](https://docs.wpilib.org/en/stable/docs/software/dashboards/glass/mech2d-widget.html) to help create your arm.

### Putting the widget together

There should be one central encapsulating `Mechanism2d` to create the widget, a `Mechanism2dRoot` as the axis of rotation, and one `Mechanism2dLigament` to act as the actual arm. This ligament is the part that directly receives position measurements and moves to fit that, effectively simulating the arm's position.

Be sure to use the provided constants in the constructor(s).

Create your `Mechanism2d` with a proper window size and an associated root with 3D translations to the axis of rotation on the physical robot...

```java
    private final Mechanism2d mech = new Mechanism2d(2, 2);
    private final MechanismRoot2d chassis =
        mech.getRoot("Chassis", 1 + AXLE_FROM_CHASSIS.getX(), AXLE_FROM_CHASSIS.getZ());
```

...before adding a `Mechanism2dLigament` to the root, and updating its position with proper position coordinates accordingly.

```java
    private final MechanismLigament2d arm =
        chassis.append(
            new MechanismLigament2d("Arm", LENGTH.in(Meters), 0, 4, new Color8Bit(Color.kAliceBlue)));

    // ...

    @Override
    public void simulationPeriodic() {
        arm.setAngle(hardware.position());
    }
```

### Conversions

Note that `Mechanism2d`'s `setAngle(double)` only takes in degree measurements, which may require a conversion depending on the units of the returned measurement.

In sim, the `SingleJointedArmSim` method for returning position only returns radian measurements[^1]. Since this shouldn't ever change, use of Java's conversion library is acceptable.

[^1]: This may be subject to change; check the [method comment](https://github.wpilib.org/allwpilib/docs/release/java/edu/wpi/first/wpilibj/simulation/SingleJointedArmSim.html#getAngleRads()) to see if the above is still valid!

```java
    @Override
    public void simulationPeriodic() {
        arm.setAngle(Units.radiansToDegrees(hardware.position()));
    }
```

While we're here, let's also set the real robot's encoder conversion factor.

REV encoders' default measurements are rotations, which should be converted to radians or degrees for use on the robot. This can be easily done with Java's Units library.

Use the predetermined `POSITION_FACTOR` constant in `ArmConstants` as the base, and convert that into your angular unit of choice.

```java
    public RealArm() {
        // ...

        encoder.setDistancePerRotation(POSITION_FACTOR.in(Radians));
        // or
        encoder.setDistancePerRotation(POSITION_FACTOR.in(Degrees));
    }
```

### Logging

Before we can actually see your widget, we need to send it to [NetworkTables](https://docs.wpilib.org/en/stable/docs/software/networktables/networktables-intro.html). Using [Monologue](https://github.com/shueja/Monologue/wiki), this can easily be done using the `@Log.NT` annotation, like so:

```java
    @Log.NT private final Mechanism2d mech = new Mechanism2d(2, 2);
    // like other Java annotations, can be placed next to or above
```

Using this, you can also log other useful data, including your PID object, and even return values from methods. Be aware though; only primitive types and classes implementing `Sendable` can be sent over NetworkTables.

For more in-depth information, we highly encourage you to read our [telemetry doc](/reference-sheets/Telemetry.md).

### Button & Subsystem Bindings

From this point, you can actually see the widget in action in the sim GUI.

However, you'll notice it just... sitting there. Which makes sense... we haven't given it any commands.

Like you've done before, create your subsystem objects with `create()`, and use the operator `CommandXboxController` in `Robot.java` to run your subsystem commands with it.

They might look something like this:

```java
    operator.x().onTrue(arm.moveTo(your-setpoint-here.in(unit-of-choice)));
```

Don't forget to add your [default command](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html#default-commands)!

### The payoff

Open up the [sim GUI](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/simulation-gui.html).

[Display the widget]((https://docs.wpilib.org/en/stable/docs/software/dashboards/glass/mech2d-widget.html#viewing-the-mechanism2d-in-glass)) on your screen. Make sure your [joystick inputs](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/simulation-gui.html#adding-a-system-joystick-to-joysticks) are correct, keyboard and the actual selection.

Hit one of the button axes (you'll know when the yellow square lights up) and that should run your command. Boom! Your arm should be moving. If you find it isn't, review review review (make sure your kP constant is >0)!

Congrats! You've successfully simulated an arm. Play around with it, set it to different angles, have fun with it!

Of course, this isn't the end.

### Unit Testing & Systems Checks

On the SciBorgs, we like to emphasize [unit tests](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/unit-testing.html) and systems checks to make sure all code works and performs as intended. To these ends, we've created libraries to simplify the process. Please review our [Unit Tests and Systems Checks reference sheets]() to understand how they work.

[comment]: # (add sheet link when completed)

In the initial differential drive project, unit tests and systems check commands were made separately. However, our testing libraries allow for a single `Test` routine to be used both as a unit test or systems check.

Take our arm, for example. We'll create a `Test` that will be run as either of the tests when required.

Before doing anything, think about what we want to test about the arm. We want it to operate properly, which means the arm moves where we want to. With a trapezoid profile as well, we want to see

- if the arm's position ultimately reaches its goal
- if the arm's velocity reaches its velocity setpoints

We first define our test factory; call it anything, but ensure it is distinguished as a `Test`:

```java
    public Test moveToTest() {}
```

Tests comprise a test command and related assertions (things that should / should not be true). Otherwise, there would be nothing to test!

Since we want to test movement, let's make the test command move to a certain position:

```java
    Measure<Angle> angle = Degrees.of(45);
    Command testCommand = moveTo(angle);
```

Then, let's create the checks for those tests. For the sake of example, we'll create one `EqualityAssertion` testing position and one `TruthAssertion` testing velocity setpoint.

We like to use the `tAssert()` and `eAssert()` factories in `Assertions.java` to actually instantiate these tests. They accept a string name, as well as functions for the expected and real values (with a tolerance for the equality assertion):

```java
    EqualityAssertion velocityCheck =
        Assertion.eAssert(
            "Arm Position Check: expected 0 rad/s, actually " + hardware.velocity() + " rad/s",
            () -> 0,
            hardware::position,
            0.5);
    TruthAssertion atPositionCheck =
        Assertion.tAssert(
            pid::atGoal,
            "Arm At Goal Check",
            "expected " + angle.in(Radians) + " rad, actually " + hardware.position() + " rad");
```

And finally, let's return the created test:

```java
    return new Test(testCommand, Set.of(velocityCheck, atPositionCheck));
```

### Tuning your simulated arm

You might have noticed that your arm does not consistently reach its setpoint, especially if the arm's goal is in a different quadrant.

This is the result of those constants being poorly tuned for that range of motion; it'll be up to you to tune the closed-loop control system.

Current sim behavior[^2] dictates that values changed in code will only be seen in simulation after a restart, which is non-ideal and will take a while.

[^2]: As of the 24-25 school year.

One way we can make this job much easier is with the use of our `Tuning.java` utility class, which uses WPILib's `DoubleEntry`.

```java
  private final DoubleEntry p = Tuning.entry("/Robot/arm/P", kP);
  private final DoubleEntry i = Tuning.entry("/Robot/arm/I", kI);
  private final DoubleEntry d = Tuning.entry("/Robot/arm/D", kD);
  // feel free to copy the above into Arm.java
```

These values can be modified during runtime, allowing for code modification and tuning without needing to redeploy code to test each new value.

In your `periodic()` method, update your PID constants using the values above with the `DoubleEntry.get()` method.

```java
    @Override
    public void periodic() {
        pid.setP(p.get());
        // include the rest
    }
```

In the sim GUI, you can click on the values of the DoubleEntry above to set new values.

In AdvantageScope, tuning mode can be turned on [like so](https://github.com/Mechanical-Advantage/AdvantageScope/blob/main/docs/OPEN-LIVE.md#tuning-mode).

Note that the constants themselves will not change in code, only for the simulation. Be sure to note down what values worked and update your constants with those correctly tuned values!

For guidance on tuning your arm control, consult the [WPILib docs](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/tuning-vertical-arm.html).

## Continuance

If you're interested in coding a project similar to this one, we recommned our [basic shooting project](https://github.wpilib.org/allwpilib/docs/release/java/edu/wpi/first/wpilibj/DutyCycleEncoder.html)! It introduces the same concepts as this tutorial, and is a great choice if you want to test the skills learned from this guide.

If you're feeling exceptionally confident, you can try creating a more advanced arm or shooting project.

[comment]: # (add links to projects above when created)

  public Command systemsCheck() {
    return Test.toCommand(
            shooter.goToTest(RadiansPerSecond.of(100)),
            Test.fromCommand(
                intake
                    .intake()
                    .asProxy()
                    .deadlineWith(feeder.forward(), shooter.runShooter(100))
                    .withTimeout(1)),
            pivot.goToTest(Radians.of(0)),
            pivot.goToTest(STARTING_ANGLE),
            drive.systemsCheck())
        .withName("Test Mechanisms");
  }