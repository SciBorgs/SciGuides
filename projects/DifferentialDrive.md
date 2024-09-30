# Differential Drive Project

![driveSim](https://cdn.discordapp.com/attachments/1008564537328414730/1285003832782356531/ezgif.com-video-to-gif-converter.gif?ex=66e8b093&is=66e75f13&hm=ebee0cc4ed98182fd0b570a606cddd2b9e6810812489e4aca268f5bf798b6995&)

This project is going to cover how to make both a basic and an advanced differential drive.

Prereqs: A good understanding of java, command-based programming, and how to use git in vscode.

Goals: Get an understanding of how to create a differential drive with advance controls.

---

## Initial Setup

### Robot Code Structure

Robot code is structured using **subsystems** and **commands** within FRC's **command-based framework**. This architecture simplifies robot programming by breaking down complex tasks into smaller, manageable pieces:

- **Subsystems**: These represent individual components or systems on the robot, like the drivetrain or arm mechanism. The main thing to keep in mind is that all of your subsystem classes should extend `SubsystemBase`. Learn more about [subsystems](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html) here.

- **Commands**: Commands are actions that the robot can perform, such as driving forward or rotating. These actions often involve multiple subsystems working together. Learn more about [commands](https://docs.wpilib.org/en/stable/docs/software/commandbased/commands.html) here.

For a deeper dive into command-based programming, check out [this guide](https://docs.wpilib.org/en/stable/docs/software/commandbased/what-is-command-based.html).

### Setting up the environment

Refer to the [environment setup](https://github.com/SciBorgs/SciGuides/blob/env-setup/reference-sheets/EnvironmentSetup.md) reference sheet to check that all neccessary components are setup before starting this project. Feel free to ignore the normal vscode section as that won't be needed for this project.

Make sure to practice good git habits when working on this and any other project. See this [reference sheet]() to learn how.

## Basic Drivetrain

A differential drive is a type of robot drivetrain where two separately-driven groups of wheels are used to move the robot. By varying the speed of each wheel, the robot can move forward, backward, or turn. This setup is widely used due to its simplicity and high degree of control over the robot’s movement.

#### How Differential Drive Works

- **Forward/Backward Movement:** Both wheels move at the same speed in the same direction.
- **Turning:** The wheels move at different speeds or in opposite directions, causing the robot to turn.

### Implementation

### 1. Setting Up the Drivetrain

##### Motor Controllers

For this guide, we’ll be using CANSparkMax motor controllers paired with NEO motors.

- **CANSparkMax:** A motor controller developed by REV Robotics designed specifically for controlling brushless motors like the NEO.
- **NEO Motor:** A brushless motor designed by REV Robotics.

#### Drivetrain Motor Setup

<img src="https://docs.wpilib.org/en/stable/_images/layout.jpg">

- Here, we can see that there are 2 motors plugged into each side of the drivetrain.

### 2. Creating the Drive Subsystem

We’ll create a drive folder with a Drive subsystem that extends `SubsystemBase` and contains the logic to control the motors and the drivetrain.

#### DriveConstants.java

In `DriveConstants.java`, we will define all the constants needed for our drivetrain, such as physical values of the drive.

Your files should look something like this:

![file order](https://cdn.discordapp.com/attachments/1008564537328414730/1285009894944276530/image.png?ex=66e8b639&is=66e764b9&hm=2ee8be3b293f941755284c54b334e8cdca86d99c400580b4a95d88c2b7075630&)

#### Drive.java

This is where the main drivetrain logic will reside. We're going to start by making all of our 4 motors using [`CANSparkMax`](https://codedocs.revrobotics.com/java/com/revrobotics/cansparkmax) and assigning a port value which is stored in the `Ports.java` file. For now, you can assign any value to these ports. However, if you want to test your drive in real life, you'd need to make sure each motor is assigned to its actual port value. Make sure to make the motor type brushless as all sparks are brushless.

```java
public class Drive extends SubsystemBase{  
  
  private final CANSparkMax leftLeader = new CANSparkMax(Drivetrain.leftMotor1Port, MotorType.kBrushless);
  private final CANSparkMax leftFollower = new CANSparkMax(Drivetrain.leftMotor2Port, MotorType.kBrushless);
  
  private final CANSparkMax rightLeader = new CANSparkMax(Drivetrain.rightMotor1Port, MotorType.kBrushless);
  private final CANSparkMax rightFollower = new CANSparkMax(Drivetrain.rightMotor2Port, MotorType.kBrushless);
}
```

Notice how we named the motors leaders and followers relative to their side. This is because instead of constantly calling all four of the motors, we can have one motor follow another on both sides. Meaning we now only have to call 2 motors, one from each side. This is done by using the `follow` method as seen below.

```java
 public Drive() {
        rightfollower.follow(rightLeader);
        leftfollower.follow(leftLeader);

        leftLeader.setInverted(true);
    }
```

`setInverted` allows motors on opposite sides of the drivetrain to spin in opposite directions to move the robot forward or backward. By default, if both motors are given the same positive value, they will spin in the same direction. However, for the robot to move forward, the motors need to spin in opposite directions.

Now to actually make a drive method that will allow the motors to run, we will pass in our speeds to the motors. The `leftSpeed` and `rightSpeed` are specific values that tell the motors how fast to go. These will be provided through the driver's controller.

```java
public void drive(double leftSpeed, double rightSpeed){
    leftLeader.set(leftSpeed);
    rightLeader.set(rightSpeed);
}
```

#### Controlling the drivetrain

Start off by making a CommandXboxController for driving. This will require a port value which we also store in ports.

```java
private final CommandXboxController driver = new CommandXboxController(OI.DRIVER);
```

- It is standard convention to have operator as port 0 and driver as 1.

Then, to make sure we can drive throughout the entire game, we add a default command to the drive subsystem. A default command is a command that is scheduled when no other command requires the subsystem.

```java
private void configureBindings() {
    drive.setDefaultCommand(drive.run(() -> drive.drive(driver.getLeftY(), driver.getRightY())));
}
```

`run()` is a simple subsystem command that runs the given action until interrupted.

### Wheel Odometry Integration

Brush up on the [sensors guide]() if you're uncertain what encoders and gyros are.

#### Adding Encoders

Our motors have built in encoders that we will be using for this project.

Let’s add encoders to the existing `Drive.java` file:

```java
  private final RelativeEncoder leftEncoder = leftLeader.getEncoder();
  private final RelativeEncoder rightEncoder = rightLeader.getEncoder();
```

#### Conversion factors

We need to convert the rotation of the encoder to a measurable distance based on our wheel radius. To get started we need to set up our `DriveConstants.java` file with the neccesary measurements.

```java
public static final double WHEEL_RADIUS = 0.08; //Meters
public static final double CIRCUMFERENCE = 2.0 * Math.PI * WHEEL_RADIUS;
public static final double GEARING =  8;

public static final double POSITION_FACTOR = CIRCUMFERENCE * GEARING;
public static final double VELOCITY_FACTOR = POSITION_FACTOR / 60;
```

Now we just need to use the conversion method from the encoder class in `Drive.java`.

```java
leftEncoder.setPositionConversionFactor(DriveConstants.POSITION_FACTOR);
rightEncoder.setPositionConversionFactor(DriveConstants.POSITION_FACTOR);

leftEncoder.setVelocityConversionFactor(DriveConstants.VELOCITY_FACTOR);
rightEncoder.setVelocityConversionFactor(DriveConstants.VELOCITY_FACTOR);
```

#### Resetting the Encoders

At the start of the match (or any time you need to reset the robot's position), it's important to reset the encoder values to zero. This ensures that your distance calculations start from a known point.

We'll reset the encoders during the subsystem initialization:

```java
leftEncoder.setPosition(0);
rightEncoder.setPosition(0);
```

#### Adding a gyroscope

`AnalogGyro` requires a channel port which we store in the ports file.

Let’s add the AnalogGyro to the existing ``Drive.java`` file:

```java
private final AnalogGyro gyro = new AnalogGyro(gyroChannel);
```

#### Resetting the Gyro

At the start of the match (or anytime you need to ensure accurate heading data), it's important to reset the gyro. This removes any bias or drift in the sensor, ensuring that your heading starts from a value of 0.

```java
gyro.reset();
```

#### Introducing Odometry

Using the encoders and gyro we just made, we can incorporate odometry into our project. Odometry allows us to estimate the robot's position and angle on the field. This is done by constantly updating our encoder and gyro values. Here's the wpilib doc on [Diff. Drive Odometry](https://docs.wpilib.org/en/stable/docs/software/kinematics-and-odometry/differential-drive-odometry.html) for more specifics.

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

`new Rotation2d()` and `new Translation2d()` simply return a value of 0 for each. Translation2d represents the x and y location of your robot on the field. Rotation2d is the angle of rotation of the robot. Explained in depth [here](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/geometry/pose.html). This can be configured based on how and where your robot will be starting each match.

#### Periodically updating odometry

To keep track of the robot’s position in real-time, we need to update the odometry regularly with the latest encoder readings. This will typically happen in the `periodic()` method, ensuring that position data is always up-to-date.

Here's how you might update odometry:

```java
public void updateOdometry(Rotation2d rotation){
    odometry.update(
        rotation,             
        leftEncoder.getPosition(),        
        rightEncoder.getPosition()        
    );
}
```

- We are passing in rotation as a parameter because once we want to simulate our robot, it'll be easier to distinguish between our real and sim rotation.

Aside from updating our odometry, we might need to reset it. I will leave this up to you to figure out how to do. (Hint: `odometry` has a method called `resetOdometry`). We won't need it for this project but if you're using the drive for autos example, it is good to reset your odometry whenever autos start.

#### Periodic

To ensure that our odometry is constantly updating as the robot moves, we run the `updateOdometry()` method periodically every tick (0.02 seconds by default). This will go in the `periodic()` method that all subsystems inherit from `SubsystemBase`, including our `Drive` class.

```java
@Override 
public void periodic(){
  updateOdometry(gyro.getRotation2d());
}
```

Keep in mind, this will be changed in the simulation section to account for sim rotation.

Last thing to finish up our basic drive will be to get our pose based on the odometry. This is very simple as it just requires calling the `getPoseMeters` method from our odometry. Keep in mind this returns a Pose2d.

A `Pose2d` contains both the Translation2d and Rotation2d of your robot. Hence, we pass in our odometry which we defined to have our translation and rotation.

```java
public Pose2d pose() {
    return odometry.getPoseMeters();
}
```

### Control Theory

Before we get started, please make sure you have read the [Control Theory reference sheet](https://github.com/SciBorgs/SciGuides/blob/main/Controls.md) as we are going to assume you are aware of what PID and Feedforward generally do.

#### Why Control Theory Matters for Driving

Before we dive into the code, let’s touch on why control theory is essential. For a robot to move precisely and respond accurately to commands, simply sending raw motor commands isn’t enough. We need to ensure that the robot can handle changes in conditions, like different terrains or obstacles, while still following the desired path. Control theory helps us achieve this by using techniques like PID and feedforward control to manage motor responses.

#### Setting Up PID Controllers

Let’s start by setting up the PID controllers. These controllers will help keep the motor speeds on track by constantly adjusting based on the difference between the desired and actual speeds. [PID](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/controllers/pidcontroller.html) doc

```java
private final PIDController leftPIDController =
    new PIDController(PID.P, PID.I, PID.D);
private final PIDController rightPIDController =
    new PIDController(PID.P, PID.I, PID.D);
```

#### Adding Feedforward Control

Next, we incorporate feedforward control. While PID handles errors after they occur, feedforward focuses on already known phyiscal disturbances like friction of a system to manipulate its inputs. [Feedforward](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/controllers/feedforward.html#simplemotorfeedforward) doc.

```java
private final SimpleMotorFeedforward feedforward = new SimpleMotorFeedforward(FF.kS, FF.kV);
```

- The PID and FF values are stored in `driveConstants` and are imported. Keep in mind these are just basic values to get you started with the project.

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

Now, let’s see how these two control mechanisms work together. We’ll look at the drive method, which is responsible for controlling the motor voltages. Here's a doc that explains more of the specifics on [combining PID and Ff](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/controllers/combining-feedforward-feedback.html).

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

### Unit Testing & System Checks

#### Unit Tests

Think of unit tests as a way to check that each small piece of your code—like a motor or sensor—is functioning properly on its own before you start putting them all together. It's much easier to fix problems when they’re isolated to a single component than when they’re all tangled up in the full system.

**Make sure to check out this [guide](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/unit-testing.html) from wpilib on how to setup unit tests.**

Let’s talk about the tests for our drivetrain. We'll start it by creating a `DriveTest.java` file in the robot folder of the tests folder.

First, we need to set things up before we run any tests. This is done in the `setup()` method:

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

- `getSpark()` is a simple method in `Drive.java` that lets us use one of the motors:  
  - `public CANSparkMax getSpark() { return leftLeader; }`

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

  Another example: here, we test to see if our pose is changing as we drive. The `fastForward` allows time to pass to give our drive time to move. Then we call our `getPose()` method and compare it to a new Pose2d, which returns a value of 0. So this test ensures that whenever our drive method is called, the robot doesn't stay at the Pose2d but actually moves.

```java
  @Test
  public void testPose(){
    drive.drive(0.8, 0.8);
    fastForward();

    assertNotEquals(new Pose2d(), drive.getPose());
  }
```

#### Running the tests

Again, make sure to check out the WPILib [guide](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/unit-testing.html) on this as it also talks about writing and running tests. To actually see if the tests are valid, open the WPILib command palette (top right corner logo) and search `Test Robot Code` and press enter. After it runs, it will show you the results of all your tests in the terminal.  

![test pass](https://cdn.discordapp.com/attachments/1008564537328414730/1285003833725943839/image-3.png?ex=66e8b094&is=66e75f14&hm=dc7fac40b87284913ef974690abd28598133d6437acd832a9195f00ded35d9d5&)

Unit tests should be made for all key subsystems and are a great way to see if the logic behind the code actually makes sense and works. You should also try to test all parts of the subsystems to cover everything.  

Here's another simple test but for LEDs.

```java
@Test
  public void testRainbowTheme() {
    var rainbow1 = LedStrip.getBufferDataString(led.rainbowAddressableLEDBuffer());
    fastForward(2);
    var rainbow2 = LedStrip.getBufferDataString(led.rainbowAddressableLEDBuffer());
    assertNotEquals(rainbow1, rainbow2);
  }
  ```

If you just scan through the code, it's easy to tell what the process is and what we're testing. We are setting up the LEDs to display a rainbow pattern, fast forwarding in time so that it's a different color than before, and testing to make sure that the two colors are indeed different from each other.  

The last type of assert most commonly used in tests is the `assertEqual`. This simply tests if two values are the same. Both in assertEqual and assertNotEqual, you can pass in a tolerance value that will pass the test if the two different values are within the tolarence. This is usually done by having a `DELTA` value set to your prefered tolarence.
  
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

Step 3: Combine the command and assertions into a Test

```java
Set<Assertion> assertions = Set.of(leftMotorCheck, rightMotorCheck);
return new Test(testCommand, assertions);
```

#### Running systems check

To run the systems check, we use the `Test` mode of the robot. To get started, we need to make a command that's going to run whenever we enable `Test` mode using the built-in test() trigger. All of this is done in `Robot.java`. Keep in mind that this method would be responsible for the systems checks of all your subsystems, not just drive.

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

This is probably the most important part of systems check, checking if our tests passed. Using `FaultLogger`, we are able to pass the results of our checks into NetworkTables and see them in both sim and `Elastic`.  

- Elastic is a dashboard that's great use for drive team as it lets you see a bunch of robot data on a nice layout. You don't necessarily need this app for the project and can view this in sim.

Make sure you are periodically updating FaultLogger in `Robot.java`.

```java
addPeriodic(FaultLogger::update, 2); 
```

Now launch the sim window (ctrl + shift + p) -> ```simulate robot code```.
Once it's loaded, click the `Test` mode and then open NetworkTables info.

![NT faults](https://cdn.discordapp.com/attachments/1008564537328414730/1285003833231020113/image-1.png?ex=66e8b094&is=66e75f14&hm=221304b3997be3f1370ff3bb5872a26988cd5be1b9bf9f77f9cb0742a47ad45f&)

In Faults and Total Faults, we can see that we have indeed ran our checks and since there are no warnings, it is safe to assume that in this case the checks have passed.

- To see this in Elastic, click `Test` and then head to Elastic. Right click, click add widgets, click `Faults` and drag and drop `Total Faults` and `Active Faults` onto the layout. You should see the following if the tests have passed.

![elastic faults](https://cdn.discordapp.com/attachments/1008564537328414730/1285003833512165427/image-2.png?ex=66e8b094&is=66e75f14&hm=96158dc445f4fbde17a7bcbc68c195a2a90e77cabc9849a2a21ef0f33e5e4016&)

Same with Unit Tests, it's good to have system checks for all runnable parts of the robot to ensure the robot is fully ready for the game. As a notice, please make sure to run system checks while the robot is ON the robot cart.

### Simulation and Logging

To finish our project up, we are going to simlute the drive we've made. Please read the [Simulation reference sheet](https://github.com/SciBorgs/SciGuides/blob/main/Simulation.md) before continuing on with this.

#### Setting Up the Simulation

To simulate the drivetrain, we’re going to use the `DifferentialDrivetrainSim` class. This simulation will model the physical characteristics of our robot—like the motors, mass, and wheel dimensions—so we can see how the code will affect the robot in a virtual environment. Here's the whole section on [Diff. Drive Sim](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/drivesim-tutorial/index.html) from wpilib.

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

- Remember that all of these values would be stored in `DriveConstants.java`:

  ```java
  public static final double TRACK_WIDTH = 0.7112; // Meters
  public static final double WHEEL_RADIUS = 0.08; //Meters
  public static final double GEARING =  8;
  public static final double MOI = 7.5;
  public static final double DRIVE_MASS = 60.0; //kg
  public static final Matrix<N7, N1> STD_DEVS = VecBuilder.fill(0, 0, 0, 0, 0, 0, 0);
  ```

By setting up the simulation with these constants, we’re creating a physics model of our robot that behaves similarly to how it would in real life.

Before we start periodically updating our sim values, make sure to set the voltage to our sim drive in the `drive` method:

```java
driveSim.setInputs(leftVoltage, rightVoltage);
```

Last thing to set up will be our sim rotation that was previously mentioned. We'll start by making a new Rotation2d:

```java
private Rotation2d simRotation = new Rotation2d();
```

Then simply change our `updateOdometry` method in `periodic()` to account for our new rotation.

```java
public void periodic(){
    updateOdometry(Robot.isReal() ? gyro.getRotation2d() : simRotation);
}
```

- The "?" and " : " are a simple way of saying, is the condition on the left of "?" true? If so, do the thing after the "?". If not, do the thing after " : ". This is also known as a ternary operator and used to make the code simpler.
- We will update our `simRotation` value in `simulationPeriodic` as seen below.

#### Simulation in Action

The `simulationPeriodic` method is where we update the simulation. This method is called regularly during the robot’s operation to keep the simulated sensors and drivetrain in sync with the rest of the code. The `@Override` annotation above the method is there so that the compiler knows it's the inherited method from `SubsystemBase`. However, it isn't neccessary to include.

```java
@Override
public void simulationPeriodic(){
  driveSim.update(0.02);  // Update the drivetrain simulation every 20ms
  leftEncoder.setPosition(driveSim.getLeftPositionMeters());
  rightEncoder.setPosition(driveSim.getRightPositionMeters());
  simRotation = driveSim.getHeading();
}
```

- `leftEncoder.setPosition` and `rightEncoder.setPosition`  update the simulated encoder positions to match the simulated robot’s movement.
- `simRotation`: Updates the simulated Rotation2d based on the robot’s simulated heading.

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

#### Using Monologue for NetworkTables Logging

We use NetworkTables (NT) to make logging specific variables or objects easier. Read the [Telemetry doc]() for specifics on logging with NT. We’re going to use the `@Log.NT` annotation as it allows us to log key metrics in real-time while the robot is running, which we can then view on dashboards like Shuffleboard or SmartDashboard.

Let's get started by making a field:

```java
@Log.NT private final Field2d field2d = new Field2d();
```

Read up on the [sim reference sheet]() to see when and what we should be logging through network tables.

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

Start by launching sim and opening up NetworkTables. use this [sim gui guide](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/simulation-gui.html) to help you navigate around. To see our Field2d widget, go to NetworkTables, then SmartDashboard, and click "field". Next, to see our logged data, click NetworkTables and the first option. You should see something similar to the image below.

![drive NT](https://cdn.discordapp.com/attachments/1008564537328414730/1285003833935790120/image-4.png?ex=66e8b094&is=66e75f14&hm=4aae908061d3982b780cc21be8c7a97916fa18b6db51de3315fcca3966d40928&)

Since our driver port is 1, make sure your joystick is also on the same port value in sim or else it will not get any inputs. Lastly, to control the differential drive properly, the joystick will require to have 6 total `axis` as shown below. You can add more and change the bindings by going to `DS` then cliking on the settings of which ever keyboard you are using.

![drive joystick](https://cdn.discordapp.com/attachments/1008564537328414730/1285003834170540174/image-5.png?ex=66e8b094&is=66e75f14&hm=95637e84b02619178619d0b9269b94940273868a555d428d53b4690e9ab206a0&)

Move the robot around in sim and have fun. If you don't like the two handed control of a differential drive, take a shot at an arcade drive. Use the `DifferentialDrive` class from wpilib and make use of its `arcadeDrive` methods. An arcade drive functions such that you can move forward/backward and sideways while only using 1 joystick.

### Continuing on

Once you feel ready for the next step, get started on an ArmBot project. It's going to have a different code structure than we discussed, but many of the ideas still remain. You can get started [here]().

Sneak peek:

![arm gif](https://camo.githubusercontent.com/0fa588f2e99bfd0489a858dbc10bfddb918ae57cbf9987017c9c4af91863edd9/68747470733a2f2f692e6779617a6f2e636f6d2f63623631383964306335386333633238663835353863663838616638323766662e676966)
