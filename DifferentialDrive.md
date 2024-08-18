# DIFFERENTIAL DRIVE

![alt text](ezgif.com-video-to-gif-converter.gif)
This project is going to cover how to make both a basic and an advanced differential drive. 

Prereqs: A good understanding of java, command-based programming, and how to use git in vscode. 

Goals: Get an understanding of how to create a differential drive with advance controls. 

---

## Initial Setup

### Robot Code Structure

Robot code is structured using **subsystems** and **commands** within the **Command-Based Framework**. This architecture simplifies robot programming by breaking down complex tasks into smaller, manageable pieces:

- **Subsystems**: These represent individual components or systems on the robot, like the drivetrain or arm mechanism. They encapsulate the hardware and related functionalities. [Learn more about subsystems here](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html).

- **Commands**: Commands are actions that the robot can perform, such as driving forward or rotating. These actions often involve multiple subsystems working together. [Learn more about commands here](https://docs.wpilib.org/en/stable/docs/software/commandbased/commands.html).

For a deeper dive into command-based programming, check out [this guide](https://docs.wpilib.org/en/stable/docs/software/commandbased/what-is-command-based.html).

### Setting up VScode

After making a new branch for this project and opening up wpilib vscode, start by making a drive folder. Which then will have a drive.java file and a driveConstants.java file. 

Make sure you have the [REVlib vendor library](https://software-metadata.revrobotics.com/REVLib-2024.json) installed. Do this by searching up manage vendor libraries, then clicking on install online, and pasting the link. It will ask to build your code, click yes and it's fine if it fails. 

Make sure to practice good git habits when working on this and any other project. See this [reference sheet]() to learn how. 


## Basic Drivetrain

A differential drive is a type of robot drivetrain where two separately driven wheels are used to move the robot. By varying the speed of each wheel, the robot can move forward, backward, and turn. This setup is widely used due to its simplicity and effectiveness in controlling the robot’s movement.

#### How Differential Drive Works:
- **Forward/Backward Movement:** Both wheels move at the same speed in the same direction.
- **Turning:** The wheels move at different speeds or in opposite directions, causing the robot to turn.


### Implementation

### 1. Setting Up the Drivetrain

##### Motor Controllers
For this guide, we’ll be using CANsparkMAX motor controllers paired with NEO motors.

- **CANsparkMAX:** A motor controller developed by REV Robotics designed specifically for controlling brushless motors like the NEO.
- **NEO Motor:** A brushless motor designed by REV Robotics.

#### Drivetrain Motor Setup
<img src="https://docs.wpilib.org/en/stable/_images/layout.jpg">

- Here you can see that there are 2 motors assinged to both sides of the drive. 
### 2. Creating the Drive Subsystem

We’ll create a Drive subsystem that extends `SubsystemBase` and contains the logic to control the motors and the drivetrain.

#### DriveConstants.java
In `DriveConstants.java`, we will define all the constants needed for our drivetrain, such as physical values of the drive.

#### Drive.java
This is where the main drivetrain logic will reside. We'll use the DifferentialDrive class from WPILib to handle the driving logic.
```java
package org.sciborgs1155.robot.drive;

import static frc.robot.Ports.Drive.*;

import com.revrobotics.CANSparkMax;
import com.revrobotics.CANSparkLowLevel.MotorType;
import edu.wpi.first.wpilibj.drive.DifferentialDrive;
import edu.wpi.first.wpilibj2.command.SubsystemBase;


public class Drive extends SubsystemBase{  
    private DifferentialDrive drive;
  
    private final CANSparkMax leftLeader = new CANSparkMax(leftMotor1Port, MotorType.kBrushless);
    private final CANSparkMax leftfollower = new CANSparkMax(leftMotor2Port, MotorType.kBrushless);
    
    private final CANSparkMax rightLeader = new CANSparkMax(rightMotor1Port, MotorType.kBrushless);
    private final CANSparkMax rightfollower = new CANSparkMax(rightMotor2Port, MotorType.kBrushless);
}
```
We're going to start by making all of our 4 motors using `CANSparkMax` and assigning a port value which is stored in the ports file. Make sure to make the motor type brushless as the neos we are using are brushless. 

Notice how we named the motors leaders and followers relative to their side. This is because instead of constantly calling all four of the motors, we can have one motor follow another on both sides. Meaning we now only have to call 2 motors, one from each side. This is done by using the `.follow` method as seen below. 
```java
 public Drive() {
        rightfollower.follow(rightLeader);
        leftfollower.follow(leftLeader);

        leftLeader.setInverted(true);

        drive = new DifferentialDrive(leftLeader::set, rightLeader::set);
    }
```
`setInverted` Allows motors on opposite sides of the drivetrain to spin in opposite directions to move the robot forward or backward. By default, if both motors are given the same positive value, they will spin in the same direction. However, for the robot to move forward, the motors need to spin in opposite directions.

`leftLeader::set` passes the `set` method of the `leftLeader` motor as a method reference. This is done so it can be called later by the `DifferentialDrive` class.

Now to actually make a drive method that will allow the motors to run, we will use the `tankDrive` method from the differentialDrive class. The `leftSpeed` and `rightSpeed` are specific values that tell the motors how fast to go. These will be provided through the driver's controller.
```java
public void drive(double leftSpeed, double rightSpeed){
        drive.tankDrive(leftSpeed, rightSpeed);
    }
```
#### Controlling the drivetrain
Start off by making a driver xBoxController. This will require a port value which we also store in ports.
```java
private final CommandXboxController driver = new CommandXboxController(OI.DRIVER);
```
- It is a standard convention to have operator as port 0 and driver as 1

Then to make sure we can drive throughout the entire game, we add a default command to the drive subsystem. A defualt comannd is a command that is called when no other command requires the subsystem, lasting for the whole match.
```java
private void configureBindings() {
    drive.setDefaultCommand(drive.run(() -> drive.drive(driver.getLeftY(), driver.getRightY())));
}
```
### Wheel Odometry Integration

Brush up on the [sensors guide]() if you're uncertain what encoders and gyros are.
#### Adding Encoders

Our motors have built in encoders and we will be using those for this project. 

Let’s add encoders to the existing drive.java file:
```java
  private final RelativeEncoder leftEncoder = leftLeader.getEncoder();
  private final RelativeEncoder rightEncoder = rightLeader.getEncoder();
```
#### Conversion factors
We need to convert the rotation of the encoder to a measurable distance based on our wheel radius. To get started we need to set up our `driveConstants.java` file with the neccesary measurements.
```java
public static final double WHEEL_RADIUS = Units.inchesToMeters(3);
public static final Measure<Distance> CIRCUMFERENCE = Meters.of(2.0 * Math.PI * WHEEL_RADIUS);
public static final double GEARING =  8;

public static final Measure<Distance> POSITION_FACTOR = CIRCUMFERENCE.times(GEARING);
public static final Measure<Velocity<Distance>> VELOCITY_FACTOR = POSITION_FACTOR.per(Minute);
```
Now we just need to use the conversion method from the encoder class in `drive.java`
```java 
leftEncoder.setPositionConversionFactor(POSITION_FACTOR.in(Meters));
rightEncoder.setPositionConversionFactor(POSITION_FACTOR.in(Meters));

leftEncoder.setVelocityConversionFactor(VELOCITY_FACTOR.in(MetersPerSecond));
rightEncoder.setVelocityConversionFactor(VELOCITY_FACTOR.in(MetersPerSecond));
```
#### Resetting the Encoders

At the start of the match (or any time you need to reset the robot's position), it's important to reset the encoder values to zero. This ensures that your distance calculations start from a known point.

We'll reset the encoders during the subsystem initialization:
```java 
leftEncoder.setPosition(0);
rightEncoder.setPosition(0);
```
#### adding a gyroscope 
`AnalogGyro` requires a channel port which we store it in the ports file. 

Let’s add the AnalogGyro to the existing drive.java file:
```java 
private final AnalogGyro gyro = new AnalogGyro(gyroChannel);
```
#### Resetting the Gyro

At the start of the match (or anytime you need to ensure accurate heading data), it's important to reset the gyro. This removes any bias or drift in the sensor, ensuring that your heading starts from a value of 0.
```java
gyro.reset();
```
#### Introducing Odometry
Position Tracking: Odometry continuously updates the robot's position, which is crucial for autonomous navigation.

Orientation Awareness: It tracks the robot’s heading, allowing for more precise maneuvers.
```java
private final DifferentialDriveOdometry odometry;
```
#### Initializing Odometry

Odometry needs an initial orientation for the robot. We can use the `getRotation2d()` method from our gyro for the current orientation.

Here’s how we initialize the odometry in the constructor:
```java
odometry = new DifferentialDriveOdometry(
        gyro.getRotation2d(), 
        leftEncoder.getPosition(), 
        rightEncoder.getPosition(), 
        new Pose2d(new Translation2d(), new Rotation2d()));
```
`new Rotation2d()` and `new Translation2d()` simply returns a value of 0. Which both give the starting position of the robot. This can be configured based on how and where you're robot will be starting each match.
#### Periodically Updating Odometry

To keep track of the robot’s position in real-time, we need to update the odometry regularly with the latest encoder readings. This will typically happen in the periodic() method, ensuring that position data is always up-to-date.

Here's how you might update odometry :
```java
public void updateOdometry(){
    odometry.update(
        gyro.getRotation2d(),             
        leftEncoder.getPosition(),        
        rightEncoder.getPosition()        
    );
}
```
Aside from updating our odometry, on some cases we might need to reset it. I will leave this up to you to figure out how to do. (Hint: `odometry` has a method called resetOdometry). We won't need it for this project but if you're using the drive for autos example, it is good to reset your odometry whenever autos start. 
#### Using `periodic()`
To ensure that our odometry is constantly updating as the robot moves, we run the update odometry method periodically. Which is basically every tick (0.02 seconds). This will go in the `periodic()`method that our drive class obtains from inherting the `subsystemBase` class.

```java
@Override 
public void periodic(){
  updateOdometry();
}
```
Last thing to finish up our basic drive will be to getting our pose based on the odometry. This is very simple as it just requires calling the `getPoseMeters` method from our odometry. Keep in mind this returns a pose2d.

```java
public Pose2d pose() {
    return odometry.getPoseMeters();
}
```
### Control Theory
Before we get started, please make sure you have read the [Control Theory reference sheet](https://github.com/SciBorgs/SciGuides/blob/main/Controls.md) as we are going to assume you are aware of what PID and FeedForward generally do. 

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
Next, we incorporate feedforward control. While PID handles errors after they occur, feedforward anticipates what the motor speed should be and helps get us there faster.
```java
private final SimpleMotorFeedforward feedforward = new SimpleMotorFeedforward(FF.kS, FF.kV);
```
- The PID and FF values are stored in `driveConstants` and statically imported. Keep in mind these are just basic values to get you started with the project. 
```java
public static final class PID {
    public static final double P = 8.5;
    public static final double I = 0.0;
    public static final double D = 0.0;
  }

  public static final class FF {
    public static final double kS = 1;
    public static final double kV = 3;
  }
```
#### Integrating PID and Feedforward
Now, let’s see how these two control mechanisms work together. We’ll look at the setSpeeds method, which is responsible for controlling the motor voltages.
```java
public void setSpeeds(DifferentialDriveWheelSpeeds lSpeed, DifferentialDriveWheelSpeeds rSpeed) {
    final double leftFeedforward = feedforward.calculate(lSpeed.leftMetersPerSecond);
    final double rightFeedforward = feedforward.calculate(rSpeed.rightMetersPerSecond);
}
```
Here, we’re calculating the feedforward voltage for each wheel based on the target speed. This helps to ensure that the motors get an initial boost that’s closer to what they need.

Next, we add the PID control:
```java
final double leftOutput = leftPIDController.calculate(leftEncoder.getVelocity(), lSpeed.leftMetersPerSecond);
final double rightOutput = rightPIDController.calculate(rightEncoder.getVelocity(), rSpeed.rightMetersPerSecond);
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

#### Introducing Kinematics
To make sure our robot’s movements translate correctly into individual wheel speeds, we’re going to use the `DifferentialDriveKinematics` class. This class helps us convert our desired chassis speeds (like forward movement or turning) into specific speeds for the left and right wheels.
```java
private final DifferentialDriveKinematics kinematics =
    new DifferentialDriveKinematics(TRACK_WIDTH);
```
The kinematics object is initialized with the `TRACK_WIDTH` (0.7112 meters for our case), which is the distance between the left and right wheels. This helps ensure that when the robot needs to turn, both wheels adjust their speeds correctly to make that turn smooth.

#### Integrating PID, Feedforward, and Kinematics
Now, let’s see how these control mechanisms work together. We’ll look at the drive method, which is responsible for taking the inputs and converting them into specific wheel speeds, which are then controlled by the motors.
```java
public void drive(double lInput, double rInput) {
    var lSpeed = kinematics.toWheelSpeeds(
        new ChassisSpeeds(-lInput * MAX_SPEED, 0.0, 0));
    var rSpeed = kinematics.toWheelSpeeds(
        new ChassisSpeeds(-rInput * MAX_SPEED, 0.0, 0));
    setSpeeds(lSpeed, rSpeed);
}
```
We convert the linear input into wheel speeds for the left and right sides using the robot’s kinematics. Next we pass these wheel speeds to the `setSpeeds` method we just discussed. This method handles the actual motor control. The inputs are going to be the driver inputs from the controller. 

### Unit Testing & System Checks
#### Unit Tests

Think of unit tests as a way to check that each small piece of your code—like a single motor or a sensor—is functioning properly on its own before you start putting them all together. It's much easier to fix problems when they’re isolated to a single component than when they’re all tangled up in the full system.
##### MAKE SURE TO CHECK OUT THIS [GUIDE](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/unit-testing.html) FROM WPILIB ON HOW TO SETUP UNIT TESTS.

Let’s talk about the tests for our drivetrain. We'll start it by creating a driveTest.java file in the robot folder of the tests folder. 

First, we need to set things up before we run any tests. This is done in the setup() method:
```java
Drive drive;
CANSparkMax spark;

  @BeforeEach
  public void setup() {
    setupTests();
    drive = new Drive();
    spark = drive.getSpark();
  }
```
- ```getSpark()``` is a simple method in drive.java that lets us use one of the motors: 
    - ``` public CANSparkMax getSpark(){return leftLeader;}```

Next, we will need to reset our drive between every tests so we are able to experiment different things at once. 
```java
  @AfterEach
  void destroy() throws Exception {
    reset(drive);
  }
```

Once everything is set up, you can make tests with the `@Test` annotation. Here's a quick example of testing if our motors are getting voltage:
```java
   @Test
  public void testSparks() {
    drive.drive(1, 0);

    assert spark.getBusVoltage() > 3;
  }
  ```
  - 3 is a random number here, but it is small on purpose. The motor will need more voltage than 3 in order to properly run.

  Another example: Here we are testing to see if our pose is changing as we drive: 
```java
  @Test
  public void testPose(){
    drive.drive(0.8, 0.8);
    fastForward();

    assertNotEquals(new Pose2d(), drive.getPose());
  }
```
  #### Running the tests
To actually see if the tests are valid, open the wpilib command palette(ctrl + shift + p) and search ```Test Robot Code``` and press enter. After a bit, it will show you the results of all your tests in the terminal. 

![alt text](image-3.png)

Unit tests should be made for most of your subsystems and are a great way to see if the logic behind the code actually makes sense and works. You should also try to test all parts of the subsystems to cover everything. 

Here's another simple test but for LEDs. 
```
@Test
  public void testRainbowTheme() {
    var rainbow1 = LedStrip.getBufferDataString(led.rainbowAddressableLEDBuffer());
    fastForward(2);
    var rainbow2 = LedStrip.getBufferDataString(led.rainbowAddressableLEDBuffer());
    assertNotEquals(rainbow1, rainbow2);
  }
  ```
  If you just scan through the code, its easy to tell what the process is and what we're testing. Setting up the leds to a pattern, forwarding in time so that its a different color than before, and testing to make sure that the two colors are indeed different from each other. 

  The last type of assert most commonly used in tests is the `assertEqual`. This simply tests if two values are the same. Both in assertEqual and assertNotEqual, you can pass in a tolerance value that will pass the test if the two different values are within the tolarence. 
  
#### System Checks
In addition to unit tests, it’s equally important to perform system checks to ensure the entire drivetrain is operating as expected in real-world conditions. Think of system checks as a quick health check for your robot before it hits the field. You want to make sure that everything is working as it should—motors, sensors, and all. This is usually done in real life and it's a good habit to run full robot system checks before your matches. 

Here is a quick simple example of what a part of a drive system check might look like. The logic is similar to unit tests as we will run a part of the drive, and then check to see if it worked. Remember to import the Sciborg's Test Library and not the wpilib built in one. 

Step 1: Define the command to run the system check
``` 
public Test systemsCheck() {
    
    Command testCommand = run(() -> drive(-0.8, -0.8)).withTimeout(0.5);
}
```
Step 2: Define the assertions
```
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

Step 3: Combine the command and assertions into a Test
```
Set<Assertion> assertions = Set.of(leftMotorCheck, rightMotorCheck);
return new Test(testCommand, assertions);
```
#### Running systems check
To run the systems check, we use the `test` mode of the robot and declare this in robot.java. To get started, we need to make a command that's going to run whenever we enable `test` mode.
```java 
  public Command systemsCheck(){
    return Test.toCommand(drive.systemsCheck());
  }
```
To actually run this in test, we tell it to run the previous command whenever test mode is enable. (This is done in configureBindings):
```java
test().whileTrue(systemsCheck());
```
#### Viewing results 
This is probably the most important part of systems check, checking if our tests passed. Using `FaultLogger` we are able to pass the results of our checks into networkTables and see them in both sim and `Elastic`. 
- Elastic is a dashboard that's great use for drive team as it lets you see a bunch of robot data on a nice layout. You don't necessarily need this app for the project and can view this in sim. 

Make sure you are periodically updating FaultLogger in `robot.java`. (Done in the robot constructor)
```java
addPeriodic(FaultLogger::update, 2); 
```
Now launch the sim window (ctrl + shift + p) -> ```simulate robot code```.
Once it's loaded, click the `Test` mode and then open NetworkTables info.
![](image-1.png)
In Faults and Total Faults, we can see that we have indeed ran our checks and since there are no warnings, it is safe to assume that in this case the checks have passed. 
- To see this in Elastic, click `Test` and then head to Elastic. Right click, click add widgets, click `Faults` and drag and drop `Total Faults` and `Active Faults` onto the layout. You should see the following if the tests have passed. 

![](image-2.png)

Same with Unit Tests, it's good to have system checks for all runnable parts of the robot to ensure the robot is fully ready for the game. As a notice, please make sure to run system checks while the robot is ON the robot cart. 
### Simulation and Logging
To finish our project up, we are going to simlute the drive we've made. Please read the [Simulation reference sheet](https://github.com/SciBorgs/SciGuides/blob/main/Simulation.md) before continuing on with this. 

Setting Up the Simulation
To simulate the drivetrain, we’re going to use the DifferentialDrivetrainSim class. This simulation will model the physical characteristics of our robot—like the motors, mass, and wheel dimensions—so we can see how the code will affect the robot in a virtual environment.

Here’s how we set it up in our constructor:
```java
private final DifferentialDrivetrainSim driveSim;
...
driveSim =
    new DifferentialDrivetrainSim(
        DCMotor.getMiniCIM(2),
        GEARING,
        MOI,
        DRIVE_MASS.in(Kilograms),
        WHEEL_RADIUS,
        TRACK_WIDTH,
        STD_DEVS);
```
- Remember that all of these values would be stored in `driveConstants`:
  ```
  public static final double TRACK_WIDTH = 0.7112;
  public static final double WHEEL_RADIUS = Units.inchesToMeters(3);
  public static final double GEARING =  8;
  public static final double MOI = 7.5;
  public static final Measure<Mass> DRIVE_MASS = Kilograms.of(60.0);
  public static final Matrix<N7, N1> STD_DEVS = VecBuilder.fill(0, 0, 0, 0, 0, 0, 0);
  ```
By setting up the simulation this way, we’re creating a virtual model of our robot that behaves similarly to how it would in real life.

Before we start periodically updating our sim values, make sure to set the voltage to our sim drive in the `setSpeed` method: 
```java
driveSim.setInputs(leftVoltage, rightVoltage);
```

#### Simulation in Action: `simulationPeriodic`
The `simulationPeriodic` method is where we update the simulation. This method is called regularly during the robot’s operation to keep the simulated sensors and drivetrain in sync with the rest of the code. We must put a `@Override` annotation above the method as it is inherited from extending to `subsystemBase`.
```java
@Override
public void simulationPeriodic(){
  driveSim.update(0.02);  // Update the drivetrain simulation every 20ms
  leftEncoder.setPosition(driveSim.getLeftPositionMeters());
  rightEncoder.setPosition(driveSim.getRightPositionMeters());
  gyroSim.setAngle(-driveSim.getHeading().getDegrees());
}
```
- `leftEncoder.setPosition` and `rightEncoder.setPosition`: These update the simulated encoder positions to match the simulated robot’s movement.
- `gyroSim.setAngle`: Updates the simulated gyro angle based on the robot’s simulated heading.

This method ensures that our simulated sensors provide accurate feedback as the robot "moves" in the simulation, allowing us to test and tweak our code.

#### Logging: Capturing Important Data
Now let’s talk about logging. Logging is crucial for understanding how our robot behaves over time, diagnosing issues, and improving performance. We’re going to use Monologue for logging, which gives us a structured way to record and analyze data from the robot’s systems.

Here’s how we set up Monologue:
```java
private void configureGameBehavior() {
  Monologue.setupMonologue(this, "/Robot", false, true);
  addPeriodic(Monologue::updateAll, kDefaultPeriod);
  addPeriodic(FaultLogger::update, 1);
}
```
This initializes Monologue with our robot, setting up the logging system to capture data as the robot runs and makes sure Monologue logs data at regular intervals, which we’ve defined with kDefaultPeriod. By logging data regularly, we can later review how the robot performed and make informed adjustments to our code.

#### Using @Log.NT for NetworkTables Logging
We use NetworkTables to make logging specific variables or objects easier. We’re going to use the `@Log.NT` annotation as it allows us to log key metrics in real-time while the robot is running, which we can then view on dashboards like Shuffleboard or SmartDashboard.

Lets get started by making a field:
```java
@Log.NT private final Field2d field2d = new Field2d();
```
Read up on the Sim. reference sheet to see when and what we should be logging through network tables. 

One other thing we're going to log is going to be our position on the field. Simply use the annotation on the `getPose` method:
```java
@Log.NT
public Pose2d getPose() {
  return odometry.getPoseMeters();
}
```
Another quick little thing we're going to log is to see if our motors are reaching their setpoints. This is done by returning the `atSetpoint` from both of the pid controllers and log the data:
```java
@Log.NT
public boolean atSetpoint() {
  return leftPIDController.atSetpoint() && rightPIDController.atSetpoint();
}
```
By logging these values, we can gain real-time insights into our robot’s performance, which is essential for making data-driven decisions and quickly diagnosing issues.

#### Updating the Robot: periodic
Finally, the periodic method is where we update various elements of the robot regularly during operation. It’s like the heartbeat of our subsystems. Specifically, we are going to update the field display with the robot’s current position, which helps us visualize its movement.
```java
field2d.setRobotPose(getPose());
```

#### Seeing the result
Start by launching sim and opening up NetworkTables. In which you will see a Robot field, which will contain all of the things we've logged.
![alt text](image-4.png)

Since our driver port is 1, make sure your joystick is also on the same port value in sim or else it will not get any inputs. Lastly, to control the differential drive properly, the joystick will require to have 6 total `axis` as shown below. You can add more and change the bindings by going to `DS` then cliking on the settings of which ever keyboard you are using. 

![alt text](image-5.png)

And now, have fun. Experiment by moving the robot around, I suggest to keep the NetworkTables up so you can see your pose values change as you drive and confirming if the motors are reaching the setpoints. 

### Continuing on
Next up after finishing this project will be to get started on an ArmBot. This is going to have a different code structure than we discussed however a lot of the ideas still remain. You can get started [here]().