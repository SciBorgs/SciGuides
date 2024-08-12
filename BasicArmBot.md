# Basic Arm Bot Tutorial

(insert image/gif of advantagescope visualizer here)

## Description & Prerequisites

In this tutorial, you will write code for a robot with a single-jointed arm and simulate its movement. The desired robot will have a single arm joint with an elevated axis of rotation, equipped with a static (non-pivoting) intake mechanism at the end of the arm.

You are expected to have completed some level of the [Differential Drive projects](/DifferentialDriveBasic.md), as this project will build upon that codebase.
You should also be familiar with the concepts and usage of interfaces, inheritance, and the command-based paradigm.

## Setting up your environment

Using your knowledge of Git, create a new branch for your arm bot. Name it something like `basic-arm-bot`. **Make sure to also move to that branch!**
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

We declare and instantiate our hardware components...

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

Now, create a simulated implementation of `ArmIO` called `SimArm`. It'll look very similar to the above, only that the motor and encoder will be simulated by WPILIB's `SingleJointedArmSim` class

## Repairing the file system

With the introduction of this IO system, notice the substantial number of files. Multiply that by the two more subsystems you have, and that makes for an unreadable file system. So, let's change that.

On the SciBorgs, subsystem files and their constants are put in one specific subsystem folder. This folder is located in a subsystems folder on the same level as the key robot files, defining the levels of contact each part of the robot should have with each other. In other words...

```
├── Autos.java
├── Constants.java
├── Main.java
├── Robot.java
└── subsystems
    └── arm
        └── ArmIO.java
        └── RealArm.java
        └── SimArm.java
    └── claw
        └── ...
    └── ...
```

This file system can be referenced at any time here, or in our [style sheet]().

## Making the claw

You've learned how to make an IO subsystem, and now's the time you put your skills to the test. Write IO subsystem code for the static claw at the end of the arm.

Think about the requirements of this claw. Here's a hint: how fast the claw runs is nearly irrelevant for what the claw should do. Its only goal is to intake, hold, and spit out whatever's in its grasp when told to. In the same vein, it won't be substantial to create a simulated version; we don't care about it.

Try to do this one by yourself before looking below!
