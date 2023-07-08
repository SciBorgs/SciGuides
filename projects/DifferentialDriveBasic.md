# Basic Differential Drive

This is a fun project to control a differential drive. We will go from a simple implementation to full auto path following and smooth driving. This should be a good introduction to usage of WPILib classes, command framework, controls, and autos.

Note that the code shown here will not be specific to your implementation, and you may need to use different hardware classes (eg. REVLib's `CANSparkMax` and `RelativeEncoder`, rather than WPILib's `PWMSparkMax` and `Encoder`). Also, the shown code is not suitable for copy pasting, please implement it on your own from the docs, using the example code as reference.

## The most basic differential drive implementation possible

All motor classes you'll interact with implement WPILib's `MotorController` interface. For more usage details, see [here](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/motors/using-motor-controllers.html#).

```java
private final PWMSparkMax left = new PWMSparkMax(0);
private final PWMSparkMax right = new PWMSparkMax(1);
private final XboxController controller = new XboxController(0);
```

```java
left.setInverted(true);
```

Make sure to invert one side of the drivetrain, so that it drives straight forwards instead of turning in place.

```java
left.set(xbox.getLeftX()); // sets the left motor to the xbox's left input
right.set(xbox.getRightX()); // sets the right motor to the xbox's right input
```

This drive code works because xbox/joystick inputs are scaled from -1 to 1, and the `MotorController.set()` method takes a [duty cycle](https://en.wikipedia.org/wiki/Duty_cycle) input.

## Using WPILib's drive classes

WPILib provides classes to simplify the process of getting a drive up and running. This section is based off [this documentation article](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/motors/wpi-drive-classes.html).

```java
DifferentialDrive drive = new DifferentialDrive(left, right);
```

This creates a `DifferentialDrive` instance from two MotorControllers, which will be used to control a differential drive robot, such as our tank drive.

```java
PWMSparkMax leftBack = new PWMSparkMax(0);
PWMSparkMax leftMiddle = new PWMSparkMax(1);
PWMSparkMax leftFront = new PWMSparkMax(2);

MotorControllerGroup left = new MotorControllerGroup(leftBack, leftMiddle, leftFront);
```

`left` is now a collection of the three left motors, and can be treated as one becuase `MotorControllerGroup` implements `MotorController`.

```java
// tank drive is the simplest control scheme to implement, and is what you already did in the previous section
drive.tankDrive(xbox.getLeftX(), xbox.getRightX());

// in arcade drive, the left stick controls speed and the right stick controls direction
drive.arcadeDrive(xbox.getLeftY(), xbox.getRightX());

// in curvature drive, the robot moves similarly to arcade, but curves towards the desired direction as if it were a car
drive.curvatureDrive(xbox.getLeftY(), xbox.getRightX(), true);
```

## Further

Congratulations! You've programmed a very simple differentrial drive robot that can be manually controlled. For more features, such as auto routines and localization, see the [Advanced Differential Drive Project](./DifferentialDriveAdvanced.md).
