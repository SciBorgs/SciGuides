# Basic Arm Bot Tutorial

(insert image/gif of advantagescope visualizer here)

## Description & Prerequisites

In this tutorial, you will write code for a robot with a single-jointed arm and simulate its movement. The desired robot will have a single arm joint with an elevated axis of rotation, equipped with a static (non-pivoting) intake mechanism at the end of the arm.

You are expected to have completed some level of the [Differential Drive projects](/DifferentialDriveBasic.md), as this project will build upon that codebase.
You should also be familiar with the concepts and usage of interfaces, inheritance, and the command-based paradigm.

## Setting up your environment

Using your knowledge of Git, create a new branch for your arm bot. Name it something like `basic-arm-bot`. *Make sure to also move to that branch!*
If unfamiliar, please check our [style sheet]() for ideal code and git practices.

In your robot folder of your project, create an [`Arm.java` subsystem]() and an associated `ArmConstants.java` file.

## Creating your arm

Before we start, we'll be abstracting the hardware components to streamline our code.

Moving hardware like motors and encoders to class implementations of an interface decouples them from subsystem code, enabling modularity that supports simulation and flexibility in using different hardware or none at all! For a deeper dive, you should look at our [hardware abstraction datasheet](/HardwareAbstraction.md).

Begin by creating your first IO interface in its Java file. Remember: this will act as an abstraction for a real and simulated set of hardware, so only include method headers that you think they will share.

It should look something like this:

```java
public interface ArmIO { // introduce logging later when it comes time to visualize
    void setVoltage(double voltage); // reminder: interfaces only have method headers;
    // explain why these methods
    double position(); // all method bodies are specified in classes that implement ArmIO!
} 
```

Now, create a real implementation of your `ArmIO` named `RealArm` in its own file. Following Java rules, it must implement the bodies of the three methods above. Try it on your own before looking at the snippets below, and remember your goal!

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

Now, create a [simulated implementation](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/physics-sim.html) of `ArmIO` called `SimArm`. WPILIB has lots of classes to simulate all different types of mechanisms, seen [here](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/physics-sim.html#wpilib-s-simulation-classes). It'll look very similar to the above, only that the motor and encoder will be simulated by WPILIB's `SingleJointedArmSim` class.

### Constants

Digging deep into the innards, you'll notice that the constructors are a bit... packed.

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

(might just include the ArmConstants file in the template)

They need physical information to be able to accurately simulate your system, and we obviously don't have a real robot.

All this information also requires lots of organization. In `ArmConstants`, you may copy-paste these relevant predetermined constants in:

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

    public static final Measure<Velocity<Angle>> MAX_VELOCITY = RadiansPerSecond.of(9.0);
    public static final Measure<Velocity<Velocity<Angle>>> MAX_ACCEL =
        RadiansPerSecond.per(Second).of(13.0);

    public static final Measure<Angle> STARTING_ANGLE = Degrees.of(63.3);

    public static final Measure<Angle> MIN_ANGLE = Degrees.of(-45.7);
    public static final Measure<Angle> MAX_ANGLE = STARTING_ANGLE.minus(Degrees.of(1.2));

    public static final double kP = 8.0;
    public static final double kI = 0.0;
    public static final double kD = 0.5;

    public static final double kS = 0.14296;
    public static final double kV = 1.7305;
    public static final double kA = 0.01;
    public static final double kG = 0.12055;
```

Cool thing we can do: static imports, to save a bit of space. At the top of `SimArm`, we can add

```java
import static org.sciborgs1155.robot.arm.ArmConstants.*;
```

to import all of the static objects in `ArmConstants` and turn `ArmConstants.MAX_VELOCITY` to just `MAX_VELOCITY`.

Only use static imports for constants and when it makes sense stylistically and syntactically.

### Finishing up

Initialize your arm simulator like below...

```java
  private final SingleJointedArmSim sim =
      new SingleJointedArmSim(
          LinearSystemId.createSingleJointedArmSystem(
              DCMotor.getNEO(4),
              MOI.in((Meters).mult(Meters).mult(Kilograms)),
              1.0 / MOTOR_GEARING),
          DCMotor.getNEO(4),
          1.0 / MOTOR_GEARING,
          -LENGTH.in(Meters),
          MIN_ANGLE.in(Radians),
          MAX_ANGLE.in(Radians),
          true,
          STARTING_ANGLE.in(Radians));
```

and implement the ArmIO methods using the methods provided by the sim. Make sure to update the sim periodically in your input methods with its `update(double dtSeconds)` method.

To complete this IO subsystem, create the last implementation called `NoArm`. It should describe a non-existent arm, without any hardware but with methods returning 0 / doing nothing.

This class is useful for when a mechanism is broken or is not on the robot, allowing us to run the rest of the robot without major errors.

### Subsystem Integration

Now, it's time to work with the actual subsystem. `Arm.java` should include a few things:

- IO implementations of the hardware (that we just created!)
- any control run on the RoboRIO (versus a motor or other hardware)
- all [commands & command factories]()

Think about how exactly we want our arm to act, and what kinds of control would suit that.

For a long and heavy arm (relative to other mechanisms), it's dangerous to use a regular PID controller, causing the arm to straight down at high speeds. Of course, we still want the arm to reach the setpoint quickly.

A smoother alternative to the regular PID would be the addition of a trapezoid profile. Velocity and acceleration will increase, coast, and then decrease over time to reach a goal smoothly, plotting a graph in the shape of a trapezoid. WPILIB has [its own implementation of this](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/controllers/profiled-pidcontroller.html) in `ProfiledPIDController`. **Read the docs**.

Considering that the mechanism is an arm, it should be intuitive that gravity will have a much greater effect on it than other mechanisms. To account for this, we can use [WPILIB's `ArmFeedForward`](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/controllers/feedforward.html#armfeedforward), which incorporates a G term for output.

Declare all of your components...

```java
public class Arm extends SubsystemBase implements Logged {
    private final ArmIO hardware;
    private final ProfiledPIDController pid;
    private final ArmFeedforward ff;

    public Arm(ArmIO hardware) {
        this.hardware = hardware;
        pid = new ProfiledPIDController(0, 0, 0, null);
        ff = new ArmFeedforward(0, 0, 0);
  }
  // ...
```

## Repairing the file system

With the introduction of this IO system, notice the substantial number of files. Multiply that by the two additional subsystems, and that makes for an unreadable file system. So, let's change that.

On the SciBorgs, subsystem files and their constants are put in one specific subsystem folder. This folder is located in a subsystems folder on the same level as the key robot files, defining the levels of contact each part of the robot should have with each other. In other words...

```
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

This file system structure can be referenced at any time here, or in our [style sheet]().

## Making the claw

Congrats! We've learned how to make an IO subsystem, and now's the time you put your skills to the test. Write IO subsystem code for the static claw at the end of the arm.

Think about the requirements of this claw. Here's a hint: how fast the claw runs is nearly irrelevant for what the claw should do. Its only goal is to intake, hold, and spit out whatever's in its grasp when told to. In the same vein, it won't be substantial to create a simulated version; we don't care about simulating it, unless we want to make a full-fledged game relying on intaking (maybe an idea)?

Try to do this one by yourself before looking below!

## Converting the drivetrain

Here's your final challenge! Turn your basic drivetrain subsystem to a subsystem implementation. For simulation, you can use [WPILIB's `DifferentialDrivetrainSim`](https://github.wpilib.org/allwpilib/docs/release/java/edu/wpi/first/wpilibj/simulation/DifferentialDrivetrainSim.html). Good luck!

## The Simulation GUI

Now that you've completed all of your subsystems and mechanisms, it's time for the fun part. Piecing it all together!

You should begin your exploration [here](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html). Continuing, open up the sim gui and explore it. More specific details on it can be found in the [next entry](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/simulation-gui.html).
