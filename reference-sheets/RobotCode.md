- [Deciding on your code structure](#deciding-on-your-code-structure)
	- [Picking your Subsystems](#picking-your-subsystems)
	- [Picking your Commands](#picking-your-commands)
- [Organizing your files and folders](#organizing-your-files-and-folders)
	- [Subsystem folders](#subsystem-folders)
- [Writing your subsystem files](#writing-your-subsystem-files)
	- [Constants file](#constants-file)
	- [IO Interface](#io-interface)
	- [IO Classes](#io-classes)
	- [Control File](#control-file)
- [Writing Command Files](#writing-command-files)


## Deciding on your code structure
Before you write any code, the first thing you need to do is decide how your code will be structured. File structure is important to decide before you start coding because then you can figure out how to divide the work between your programmers and will stop future confusion between the team members.

### Picking your Subsystems
The first thing to do in any robot code project is to pick what subsystems your code will be based around. The subsystems you pick should be moving parts of the robot that will act independently of one another. For example, the rollers on a roller intake will move as one, even if the rollers on either side of the intake will move in opposite directions, so it should be one subsystem, but an arm attached to an elevator will act independently of the elevator it's attached to, so they should be two different subsystems even though they're attached. 

Here is an image of our 2025 robot's first KrayonCAD draft, with the subsystems circled:
![](cad-diagram-circle-subsystems.png)
### Picking your Commands
Now that you have your subsystems decided, you should figure out how you'll structure your [commands](reference-sheets/CommandBased). Commands should be used mainly when two subsystems will be moving in a coordinated motion. For example, if you have a wristed intake, the wrist should move down and the rollers should start intaking, which are two different subsystems that you'd like to use in coordination. So, you can organize those subsystems into command files and call those commands to achieve this.

## Organizing your files and folders
When we make our code, we have a very specific [file structure](/reference-sheets/FileStructure.md), with subsystems each having their own folder, and commands all placed in one folder together. 

### Subsystem folders
Each subsystem will have its own folder where its hardware, control and constants are all handled and worked with. 

In each subsystem folder, there is:
- the subsystem control file (Subsystem.java),
- the constants file (SubsystemConstants.java),
- the IO interface (SubsystemIO.java),
- IO files (RealSubsystem.java, NoSubsystem.java, SimSubsystem.java)
(replace "Subsystem" with your subsystem name, e.g. Drive.java, IntakeIO.java)

## Writing your subsystem files
### Constants file
The constants file is very simple. It should store constants required for your subsystem, such as maximum height for an elevator, starting angle for an arm or configurations for a motor. Any constant that will be used in robot code for this subsystem should be stored in this file. Since they are constants, all fields should look like this: 
```
public static final CONSTANT_FIELD = ...;
```
Keep in mind that they should be static, since the fields will be accessed directly from the class, and final since they're... constant constants.

Use cases for methods in constant files are limited but methods are sometimes useful when constants may vary based on the use case (e.g. positions of field elements based on alliance).
For now, though, you can ignore using methods in constants files.

### IO Interface
Depending on the situation, your subsystem at any setup of the robot can be real, or it can be simulated. In order to be able to use the same control despite the difference in hardware, we use inheritance. An IO interface will allow you to give instructions and receive information regardless of the hardware being used. 

In the interface, you'll declare which methods the IO classes (all of which will be implementing the interface) will have to contain. This is the only way that the control file can give instructions to and receive information from the hardware.

Here, you'll have to decide if your subsystem will require feedback. Something like an arm or an elevator will want to know the position of the hardware at any time so it can use feedback for more precise and controlled movements, however something like an intake roller doesn't care, since all it needs to know is "go" or "stop", making it a simple motor subsystem rather than a feedback subsystem.

If your subsystem wants feedback, make methods as such:
``` 
/** Docs!!! Making javadoc in IO interfaces is REQUIRED!!! */
public double position();

/** @return The velocity, in [units], of the subsystem */
public double velocity();
```

If your subsystem is a simple motor, these methods are unnecessary and should be omitted. However, all subsystem IO interfaces need a way of giving instructions, such as either setting the voltage (in feedback mechanisms) or setting the power, a number from -1 to 1 (in simple motor mechanisms). 

Any other methods that would be helpful, such as methods to set current limits of motors should also be included in the IO interface, as the control file can only interact with the hardware through the methods in the interface. This also means that if your subsystem has sensors such as a beam break, a method to access the value of the sensor is necessary and should be included.

An IO interface should also extend AutoCloseable, allowing every subsystem to be closed at once for unit testing purposes (there will be more about unit testing later).

### IO Classes
Now that you have a way of interacting with the IO classes, you have to make the IO classes themselves. As many subsystems as possible should be able to be simulated, since that allows you to test them even when the robot is not present. However, you'll find that you'll only be able to do this with feedback mechanisms, since with simple motor mechanisms there's nothing to simulate, it's just a motor. There's also no way to get information from the simulation, since the IO interface doesn't have the methods required to get such information, rendering simulation completely useless. Therefore, feedback subsystems should have the following IO files:
- RealSubsystem.java
- SimSubsystem.java
- NoSubsystem.java
where SimSubsystem.java can be omitted for simple motor subsystems.

The reason NoSubsystem exists is mostly for competition purposes, as if one of our subsystems break down it's better to not use it at all than to continue to give it commands and waste power.

##### RealSubsystem
RealSubsystem should have motors, and any other part involved with control, such as [sensors](reference-sheets/Sensors) or pneumatics (don't use pneumatics). You'll declare these parts in the fields, then instantiate and configure the motors in the constructor. Make sure to register the motor\[s] in FaultLogger and add the motor\[s] to SparkUtils! 

Parts will take in an integer value representing the port they will take on the electronics. So, make a subclass for your subsystem in Ports.java, and for each part you use in the subsystem, add a constant to the subclass in Ports.java. Then, make a static import for Ports.Subsystem in your RealSubsystem.java to make  
##### SimSubsystem
SimSubsystem should revolve mainly around a [simulated version](reference-sheets/Simulation.md) of the mechanism, for example a SingleJointedArmSim for a simulated arm/wrist/pivot and an ElevatorSim for a simulated elevator. Remember to update the sim regularly, either periodically or whenever you get information from it.
##### NoSubsystem
This one's super easy. All you need is a constructor and the interface methods. The constructor should do nothing. All interface methods that don't return anything should have no method body, and all interface methods that return a double should return 0. That's about all you need.


Now, for Real and Sim, add all methods required by the interface to the class and complete the method bodies. 

Over each inherited method, place an `@Override` to tell java that it is an inherited method (though java will probably do this for you).
There's no need to add javadoc to inherited methods, because the javadoc from the interface file will be passed down to the implementations.

### Control File
Now that all of your hardware stuff is worked out, you need to effectively control it. 
The control file is the main subsystem file, and will contain all the code needed to control it, including subsystem-specific commands that will only control the one subsystem. 

Control files should extend SubsystemBase\*, as well as implementing Logged and AutoCloseable. 

\*SubsystemBase is a class and the "Subsystem" does not change to *your* subsystem, unlike other classes mentioned in this guide.

#### Factory Methods
The control file should have a field of type SubsystemIO. This will act as the hardware. The field is not actually a SubsystemIO, it is one of the IO classes, but since they all will inherit the methods in the interface, those methods can be called regardless of the type of the hardware. The control methods will act on the hardware and use the interface methods to do this. 

Rather than using a public constructor to make our subsystems in Robot.java, it's better to form static factory methods inside the class, and make the constructor private, since the constructor takes in a SubsystemIO and we can make those in Subsystem.java, and then use a different IO class based on if the robot is real or not.

Essentially, we want to make two different public static methods that take in nothing and return a Subsystem. They'll look something like this (with the constructor at the bottom):
```
private SubsystemIO hardware;

/** Creates a real Subsystem if the robot is real and a sim if it isn't. */
public static Subsystem create() {
 return new Subsystem(Robot.isReal() ? new RealSubsystem() : new SimSubsystem());
}

/** Creates a Subsystem without any hardware. */
public static Subsystem none() {
	return new Subsystem(new NoSubsystem);
}

/** Constructor */
private Subsystem(SubsystemIO hardware) {
	this.hardware = hardware;

	// other constructor stuff goes here (if there's more)

}
```
Note the use of a ternary operator (a fancy if statement) in the create() method. 

If the subsystem is a simple motor subsystem, meaning there is no SimSubsystem file, it can be replaced with a NoSubsystem constructor.
These factory methods greatly simplify the process of instantiating subsystems when in the central Robot.java file. 

#### Fields and Control
If the subsystem is a simple motor, all you'll need to do is make commands out of setting the power of the motor. However, if it's a feedback subsystem it'll be a bit more complicated.

The best way to control one of these is to use [control theory](reference-sheets/ControlTheory.md) to our advantage. It's best to use both a feedforward controller and a feedback controller. These should be two private final fields. Feedback controllers and feedforward controllers use PID constants and SysID constants respectively, so they should be present in your SubsystemConstants file. 

Your feedforward controller should be based on the subsystem it's controlling, such as an ArmFeedForward for an arm/wrist/pivot and an ElevatorFeedForward for an elevator. 

Now, you need to decide whether you want to directly control the **velocity** of the subsystem or the **position** of the subsystem. If you're controlling shooting rollers, you want to be able to precisely control the velocity of the rollers but you don't really care about the position. However, if you're controlling an arm or an elevator, usually you'll care more about the position of it much more than the velocity. (usually.)

If you care more about position than velocity then you should use a ProfiledPIDController as your feedback, but if you care more about the velocity than the position, then for your feedback you should use a PIDController as your feedback.
```
// Keep in mind "Subsystem" is a placeholder for your subsystem
private SubsystemFeedForward feedforward = new SubsystemFeedForward( ... );

// Position-controlling case
private ProfiledPIDController feedback = new ProfiledPIDController( ... );

// Velocity-controlling case (only choose one)
private PIDController feedback = new PIDController( ... );
```

You can use these controllers through the `calculate()` method on both of them. They'll return the next voltage you'll want to pass into your hardware. When you want to use this, just sum the two controllers' voltages and set the voltage of your hardware. The method body for using the subsystem should look something like this:
``` 
/** This case is when the method has a void return type */
private void update(double goal) {
	double ff = feedforward.calculate( ... );
	double fb = feedback.calculate( ... );
	hardware.setVoltage(ff + fb);
}
```
The two methods are named differently, but either name works.
```
/** This case is when the method returns a Command */
public Command goTo(double goal) {
	return run(() -> {
		double ff = feedforward.calculate( ... );
		double fb = feedback.calculate( ... );
		hardware.setVoltage(ff + fb);
});}
```
These methods calculate the desired next velocity, then set it. One returns nothing, while the other returns a Command. They're both completely acceptable ways of going about it, but if you use the void method you'll have to run() the method in your Command methods later.
(Author's note: I personally prefer using the Command method. it's cooler :) )

#### Getters for Logging
Both when we use sim and when we test our robot in real life, [logging](reference-sheets/Telemetry) everything is very helpful for gleaning information on things. However, the only place that uses Logged is Subsystem.java, meaning that we need to log values in this subsystem. So, for each information-returning method in the IO interface, we need to write a method that returns the output of the interface method, and log the outside method. 
```
@Log
/** @return The velocity, in [units] per second. */
public double velocity() {
return hardware.velocity();
}

@Log
/** @return The position, in [units] */
public double position() {
return hardware.position();
}

// repeat this for other information-returning methods
```

Also, although this wasn't done in the previous code, logging everything is extremely useful. 
controller fields, the hardware field, and control methods should all be logged.
The main things that shouldn't be logged are subsystem-specific commands, which will be covered in two sentences.

Although not covered in this document, if making SysID routines, those should be logged, and if you're making a visualizer for sim, these field should be logged as well.

#### Subsystem-specific Commands
In your control file, you'll be able to make commands whose only subsystem requirements are the subsystem you're working on. These commands will typically do basic, repeatable movements such as going to a pre-designated state (where a "state" is just a certain position/velocity depending on the subsystem) while intaking nothing, whereas the control method we made earlier intakes a goal state and goes to that.

The commands made inside this subsystem class will typically use the control method we made earlier and simply use a state from SubsystemConstants as its input for the control method. It'll simply return a command to go to a specific, pre-designated state.

```
/** Does thing. This example uses the Command version of the control method. */
public Command doThing() {
	return goTo(SubsystemConstants.THING_STATE);
}
```
Here, THING_STATE is a constant state, and doThing() will try to go to that state every single time it's called. Also, your Subsystem.java should have a static import for SubsystemConstants.java, meaning there should be no need for the `SubsystemConstants.` before the `THING_STATE`.

#### Finishing Touches to the Subsystem folder
Make sure to javadoc EVERYTHING. There shouldn't be a single undocumented method or field in your entire branch. Try to keep method names short and simple, since the function and use case of the method should be either outlined or implied by the javadoc. 

#### Writing Unit Tests
Everyone's favorite activity! Writing unit tests!!
For each feedback subsystem, it's imperative that you write unit tests. Writing unit tests helps weed out possible errors, not only in the commands but also in the rest of the subsystem, before it becomes a massive issue. That's why it's best to write them as you go, so you can catch errors before they propagate and get out of hand. 

A way to make this simple is to make a method that returns a Test in the subsystem file, and uses the control method as well as the state of the sim to determine if the control method is working. This makes it simple to write a repeatable test for your subsystem, which is useful especially when dealing with something as important as the control command, where something not working will break the entire subsystem.

## Writing Command Files
Now that you have all of your subsystems written and completed, you can use those subsystems in commands. Each command class will have fields for each of the subsystems that it requires, take in those subsystems in the constructor, and set the subsystem fields to the inputted subsystems. The command files should go under the commands folder, and the name should somewhat represent what the commands inside will do. 

Now, you can use commands from those subsystems and compile them in such a way that they coordinate in their motions. You can use [this](reference-sheets/CommandBased) as a guide for making commands. Make sure to write it in a way that the command finishes, and does everything it is supposed to, and when it's supposed to.

Make sure to always javadoc your commands. They can be quite confusing to onlookers.

Lastly, add names to your commands using .withName("name"). It's not mandatory, but it's nice.

Make sure to also write unit tests for these! They're a great way of figuring out whether your commands work, end, and schedule correctly.

