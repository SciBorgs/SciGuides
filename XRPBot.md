# XRP
The [XRP (Experimental Robotics Platform)](https://docs.wpilib.org/en/stable/docs/xrp-robot/index.html) is a small robot that can handle WPILib Java code. You will be learning how to implement differential drive, and other very basic mechanisms, with the benefit that you will be able to test it on the physical XRP.

Beforehand, you should know what differential drive is, and Java concepts.

## Hardware
XRP hardware is slightly different from FRC hardware. There are two [driving motors](https://www.sparkfun.com/products/24053), one on each side, and they each have a built-in encoder with a resolution of 585, and a gear ratio of 1:48. These will be preset in the code, so you won't need to worry about them for now. In addition, there is a [servo motor](https://www.sparkfun.com/products/9065) on the back that controls a small arm. It's probably broken on the XRPs :(

There are also a few sensors:
* IMU sensor, which takes both gyroscope and accelerometer readings. The gyroscope is not very reliable, and it may drift ~0.5 deg/sec. 
* [Ultrasonic sensor](https://www.sparkfun.com/products/24049), located at the front of the robot, which measures the distance between the sensor and the nearest object in its scope. 
* [Line follower sensor](https://www.sparkfun.com/products/24048), located under the ultrasonic sensor, which detects changes in color. 

## Set Up
*This tutorial will adhere to the generic XRP format (no have hardware abstraction, simulations, etc.).*

1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#use-someone-elses-project-as-a-starting-point-for-your-own-idea) this [repository](https://github.com/stacyc2449/xrp-suffer-part-2-rookie.git). It's slightly modified so that you can follow this tutorial.
<!---
should change the repo link to be from the official robotics githubs later
-->
2. In VS Code, clone your forked project. You will be working with this base.

## Constants
Create a `Ports` file in src/main/java/frc/robot, and create a `DrivetrainPorts` class within the `Ports` class.
These are the relevant ports:
```java
public static final int LEFT_MOTOR = 0
public static final int RIGHT_MOTOR = 1
public static final int LEFT_ENCODER_A = 4
public static final int LEFT_ENCODER_B = 5
public static final int RIGHT_ENCODER_A = 6
public static final int RIGHT_ENCODER_B = 7
```
## Drivetrain
In src/main/java/frc/robot/subsystems, there is a Drivetrain file, which will contain the main code for the drivetrain functions.

Instantiate the following in their respective sections (indicated by comments in the file):

```java
private final XRPMotor leftMotor = new XRPMotor(DrivetrainPorts.LEFT_MOTOR);
private final XRPMotor rightMotor = new XRPMotor(DrivetrainPorts.RIGHT_MOTOR);

private final Encoder leftEncoder = new Encoder(DrivetrainPorts.LEFT_ENCODER_A, DrivetrainPorts.LEFT_ENCODER_B);
private final Encoder rightEncoder = new Encoder(DrivetrainPorts.RIGHT_ENCODER_A, DrivetrainPorts.RIGHT_ENCODER_B);

private final XRPGyro gyro = new XRPGyro();

private final BuiltInAccelerometer accelerometer = new BuiltInAccelerometer();
```
Note that all of these instantiations can be found in [the documentation](https://docs.wpilib.org/en/stable/docs/xrp-robot/hardware-support.html). 

Because the right motor is flipped 180 degrees, the positive direction of the motor is opposite that of the left. In order to account for this, we add this in the constructor:

```java
rightMotor.setInverted(true);
```

In addition, the code is not aware of the distance that the robot travels each "tick". We set this through `setDistancePerPulse()`, also in the constructor:
```java
leftEncoder.setDistancePerPulse((Math.PI * kWheelDiameterInch) / kCountsPerRevolution);
rightEncoder.setDistancePerPulse((Math.PI * kWheelDiameterInch) / kCountsPerRevolution);
resetEncoders();
```
In order to conveniently access the yaw, pitch, and roll from the gyro, create three separate methods:
```java
 /**
   * Current angle of the XRP around the X-axis.
   *
   * @return The current angle of the XRP in degrees
   */
  public double getGyroAngleX() {
    return gyro.getAngleX();
  }

  /**
   * Current angle of the XRP around the Y-axis.
   *
   * @return The current angle of the XRP in degrees
   */
  public double getGyroAngleY() {
    return gyro.getAngleY();
  }

  /**
   * Current angle of the XRP around the Z-axis.
   *
   * @return The current angle of the XRP in degrees
   */
  public double getGyroAngleZ() {
    return gyro.getAngleZ();
  }

  /** Reset the gyro. */
  public void resetGyro() {
    gyro.reset();
  }
```

Create a [differential drive controller](https://github.wpilib.org/allwpilib/docs/release/java/edu/wpi/first/wpilibj/drive/DifferentialDrive.html): (if you are unfamiliar with [differential drive](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/motors/wpi-drive-classes.html#using-the-differentialdrive-class-to-control-differential-drive-robots))

```java
private final DifferentialDrive diffDrive = new DifferentialDrive(leftMotor::set, rightMotor::set);
```
`set()` is built in to the motor, and controls the speed, from a scale of -1 to 1. Negative numbers indicate a negative direction.

The differential drive controller is able to control motor speeds based on the type of drive. Below is an example of arcade drive:
```java
public Command arcadeDrive(DoubleSupplier xaxisSpeed, DoubleSupplier zaxisRotate) {
    return new RunCommand(() -> m_diffDrive.arcadeDrive(xaxisSpeed.getAsDouble(), zaxisRotate.getAsDouble()), this);
}
```
You can also add `DifferentialDriveOdometry`, which would be more useful in your autos for now.
```java
// Declaration
private final DifferentialDriveOdometry odometry;
```
```java
// Initialization in the constructor, after configuring the encoders.
odometry = new DifferentialDriveOdometry(new Rotation2d(), m_leftEncoder.getDistance(), m_rightEncoder.getDistance());
```
```java
// Updates the position & angle of the robot, in periodic()
odometry.update(new Rotation2d().fromDegrees(m_gyro.getAngleZ()), m_leftEncoder.getDistance(), m_rightEncoder.getDistance());
```
## Robot Container
The robot container will contain the joystick, and bind the buttons on the joystick to specific actions

1. Instantiate a `Drivetrain` subsystem inside `RobotContainer`
2. Create a `Joystick`, with `kDriverControllerPort` in `OperatorConstants` as the ID
3. Optional for now, but you can also create a `SendableChooser`, which allows you to choose the autos to execute.
```java
private final SendableChooser<Command> m_chooser = new SendableChooser<>();
```
4. Set the default command for the drivetrain as the arcadeDrive command from the subsystem
5. To fill the parameters, get the raw axis from your joystick controller (axes 1 and 3)
6. If you want, you can also bind buttons of the joystick to set various arm angles (for this, you should write a method for this in a new `Arm` subsystem, with the servo being `XRPServo` with an ID of `4`)

## Deploying
[Only for a completely new XRP](https://docs.wpilib.org/en/stable/docs/xrp-robot/hardware-and-imaging.html)

1. `Build` the code, to make sure it's working.
2. In order to deploy code, you must connect to the XRP's wifi. (Ex. Username: XRP-8381-a82d)
3. Then `Simulate Robot Code`. This opens the Sim GUI.
4. Drag `Keyboard 0` to `Joystick [0]`
5. Right clicking on `Keyboard 0` will display all the keys that correspond to the buttons and axes

# More Advanced
Incorporating PID and FF control to the XRP. The driving might be worse, *especially* with bad constants, which is kinda unavoidable because SysID and tuning is not very doable on the XRP. This is more of a demo to show how it can fit into the XRP.

## Drivetrain
We will use `DifferentialDriveKinematics` because it can output wheel speeds, which will be our setpoints for PID and FF.
```java
private final DifferentialDriveKinematics diffKinematics = new DifferentialDriveKinematics(DrivetrainConstants.trackWidthMeters);

private final PIDController leftController = new PIDController(PIDConstants.kP, PIDConstants.kI, PIDConstants.kD);
private final PIDController rightController = new PIDController(PIDConstants.kP, PIDConstants.kI, PIDConstants.kD);

private final SimpleMotorFeedforward motorFeedforward = new SimpleMotorFeedforward(FeedforwardConstants.kS, FeedforwardConstants.kV);
```
Note: `trackwidth` must be in meters, and `PIDConstants` are constants that should be at low values for now. These constants go in the `Constants` file.

Refer to the PID and FF reference sheet if needed. 
<!---
link later
-->
The driving method should calculate a voltage based on the desired speed: 
```java
public void setSpeed(DifferentialDriveWheelSpeeds speeds){
    double leftFeedforward = m_motorFeedforward.calculate(speeds.leftMetersPerSecond);
    double rightFeedforward = m_motorFeedforward.calculate(speeds.rightMetersPerSecond);

    double leftDifference = m_leftController.calculate(m_leftEncoder.getRate(), speeds.leftMetersPerSecond);
    double rightDifference = m_rightController.calculate(m_rightEncoder.getRate(), speeds.rightMetersPerSecond);

    m_leftMotor.setVoltage((leftFeedforward + leftDifference));
    m_rightMotor.setVoltage((rightFeedforward + rightDifference));
}
```
Then create a separate method that can take `speed` and `rotation` as inputs from the joystick, and return a command:
```java
public Command drive(DoubleSupplier speed, DoubleSupplier rot){
    return new RunCommand(() -> setSpeed(diffKinematics.toWheelSpeeds(new ChassisSpeeds(speed.getAsDouble(), 0, rot.getAsDouble()))), this);
}
```
Afterwards, `drive()` can replace `arcadeDrive()` in `RobotContainer`, and the same steps can be followed for [deployment](#deploying)

## Tuning
For reference, previously, `kS = -0.5`, `kV = 6`, `kA = 2`, `kP = 0.2`, `kI = 1`, `kD = 1`. These are not the best constants, just ones that barely worked.
