# Simple Shooter 

## Introduction

This project is going to cover how to make a basic shooter subsystem, as well as the general structure of a standard subsystem. 

## Quick Notes

Some general reminders / self troubleshooting:

-> Use tab/autofill to automatically get imports when using certain methods.

-> Make sure to check your imports when something is not resolved.

-> Some methods have multiple variants. Make sure you're using the correct one.


## Shooter Subsystem

The shooter subsystem, as the name suggest, controls our shooter. It does this by sending a voltage to the motors, which then spin the rollers of the shooter which ultimately launch the gamepiece. This is what we'll essentially be writing methods for. 

## Ports

For our motors to actually work, we'll have to tell the robot what port they're connected to so it knows which motors to send voltage to. To do this, we'll just add a class in the Ports.java for our shooter and put some values representing what ports we're using.

```java
public final class Ports {
    ...
        public static final class Shooter { 

            public static final int leader = 10;
            public static final int follower = 11;

        }
    ...
}
```

These values will probably change as you actually finalize the robot, but we'll leave them as these for now.

## ShooterConstants // Constants

Lets get the boring bits out of the way first. There are a bunch of constants we'll need (most of which you'll get from your construction teammates) to put in a file for later use. For now, since we probably don't have most of them yet, we'll just declare the important ones we'll need.

(Note: All of these should be final since they're constants, as well as doubles unless explicitly stated)

In the ShooterConstants file, we'll declare:

Your robot constants:

- GEARING 
- RADIUS 
- CURRENT_LIMIT (Current)
- DEFAULT_VELOCITY (AngularVelocity)
- MAX_VELOCITY (AngularVelocity)
- PERIOD 
- MAX_VOLTAGE

Your PID and Feedforward constants:

- K_P
- K_I
- K_D
- K_S
- K_V
- K_A


We'll just leave these for later :>

## ShooterIO // IO File


Lets setup the IO file.

First, the file type should be changed from a class to an interface.

This file will serve as a blueprint for three other files (No, Real, and SimShooter) so it will need to contain the basic methods we need for a shooter.

To get a shooter to actually shoot <small>(waow)</small>, a voltage needs to be sent to the motors. This leads us to our first method: setVoltage. Since the method is just doing something (setting a voltage), it'll be of return type void and have a parameter double voltage.

Our second method will just return the velocity of the shooter motor as a double, hence we'll just call it getVelocity.

Your file should look something like this when you're done.


```java
public interface ShooterIO {
   public void setVoltage(double voltage);
   public double getVelocity();
}
```
<small> -> Note: whenever you make a file implement ShooterIO it might give you an error saying along the lines of "x method is missing". For now, just use quick fix to add those methods and delete their filler method bodies </small>

## NoShooter // Fake Instance

The NoShooter.java file, as mentioned previously, implements ShooterIO.java and has all methods within it either return zero or left empty.

<small>So, lets do that (・∀・)</small>

in NoShooter.java, implement the ShooterIO interface we just made, import its methods, and make sure all methods within it either return zero or left empty.

```java
public class NoShooter implements ShooterIO{
   public void setVoltage(double voltage) {}

   public double getVelocity() {
       return 0;
   }
}
```


## SimShooter // Sim Instance

The SimShooter.java file is, as the name suggests, responsible for creating our simulation. It will first require an object to be created, representing our simulated part. It will then use that object in its methods to affect things in the simulation. For our shooter, this will be a <i>FlywheelSim</i> (A WPILib class thats given to us through the WPILib extension).

First, lets declare our object.

```java
public class SimShooter implements ShooterIO {
   private final FlywheelSim shooter;
}
```

Next, write the constructor that will create our simulated shooter object.

```java
public class SimShooter implements ShooterIO {

    ...
    public SimShooter() {

        shooter = new FlywheelSim(LinearSystemId.identifyVelocitySystem(K_V, K_A), DCMotor.getNeoVortex(2), GEARING);

    }
}
```

The parameters for the FlywheelSim might look a bit confusing <small>(specifically the linear system stuff)</small>, but for us all you'll need to understand is that it uses some of the feedforward constants we declared earlier to set up how a shooter should behave.

After that, we'll also implement our methods from ShooterIO like we did in NoShooter. Unlike what we did in NoShooter, however, we'll actually have these methods interact with the simulation. To do that, we'll add some method bodies setting the voltage and getting the velocity of our simulation.

For setVoltage, it will use the method "setInputVoltage" on our shooter object to set it to our input voltage.

```java
    public void setVoltage(double voltage) {
        shooter.setInputVoltage(voltage);
    }
```

For getVelocity, it will use the method "getAngularVelocityRadPerSec" on our shooter object to get its angular velocity.

```java
    public void getVelocity() {
        shooter.getAngularVelocityRadPerSec();
    }
```

And that'll be our SimShooter :> We will actually be coming back here to add one more thing towards the end of this guide, but we'll cross that bridge when we get to it.

## RealShooter // Real Instance

The realShooter.java file is responsible for handling our code when connected to the physical robot. It requires an object to be made for each motor we use (the type should be either CANspark/SparkMax or TalonFX) and uses those objects to affect the physical motors on the robot. This also means that the number of motors will vary based on the design of your shooter so meaning that the number of motor objects in here will vary (we'll just use two).

As always, lets declare and construct our motors: one named leader and one named follower (for this guide, they will be SparkMax motors). We'll also make an encoder using our leading motor to get the velocity later.

```java
public class RealShooter implements ShooterIO {

   private final SparkMax leader;
   private final SparkMax follower;
   private final RelativeEncoder encoder;

   public RealShooter() {
       leader = new SparkMax(LEADER, MotorType.kBrushless);
       follower = new SparkMax(FOLLOWER, MotorType.kBrushless);
       encoder = leader.getEncoder();

   }
}
```

ok settings time

Next we need to configure our motors so they actually behave how we want them to. We'll do this using a SparkMaxConfig object, changing it, and then applying it to each of our motors.

First, make our config inside the constructor.

```java
public class RealShooter implements ShooterIO {

   ...
   public RealShooter() {
       leader = new SparkMax(LEADER, MotorType.kBrushless);
       follower = new SparkMax(FOLLOWER, MotorType.kBrushless);
       encoder = leader.getEncoder();

       SparkMaxConfig config = new SparkMaxConfig();

   }

}
```

Next, use Spark's methods on the config object to set our settings right under our config object.

```java
public class RealShooter implements ShooterIO {
   ...
   config
       .smartCurrentLimit(CURRENT_LIMIT)
       .idleMode(IdleMode.kBrake);
   ...
}
```


And then apply them using the configure method.


```java
public class RealShooter implements ShooterIO {
   ...
    leader.configure(config, SparkBase.ResetMode.kResetSafeParameters, PersistMode.kPersistParameters);
    follower.configure(config, SparkBase.ResetMode.kResetSafeParameters, PersistMode.kPersistParameters);

    //to make sure both motors spin the same way.
    follower.setInverted(true);
   ...
}
```

Ok, and back to our methods from ShooterIO. These will be similar to what we've seen previously, just using methods given by Spark to set the voltage of our motors and get the velocity of our encoder.

```java
public class RealShooter implements ShooterIO{

   public void setVoltage(double voltage) {
       leader.setVoltage(voltage);
       follower.setVoltage(voltage)
   }

   public double getVelocity() {
       return encoder.getVelocity();
   }

}
```

And that'll be our RealShooter :>

## Shooter // Main File

And finally, we'll need to write our "main" subsystem file that oversees the real, sim, and fake instances of our shooter as well as controlling the PID required to correctly send voltage to our motors. This file will be the one to <u>extend subsystem base</u>, and will contain several methods which return commands to integrate with our command based code structure. 

lets go :D

As always, our first step will involve us declaring our motor (this time called hardware) with type ShooterIO. We'll also add our PID and FF objects, which we'll use later.

```java
/// extend lets it essentially be part of the subsystem structure
/// it lets it use certain methods from SubsystemBase
public final class Shooter extends SubsystemBase {
    private final ShooterIO hardware;

    private final PIDController pid = new PIDController(P, I, D);
    private final SimpleMotorFeedforward ff = new SimpleMotorFeedforward(S, V, A, PERIOD.in(Seconds));
}
```

<small>-> Your P, I, D, S, V, A, and period constants should all come from your ShooterConstants file.</small>

Since our shooter.java file decides which instance (fake, real, sim) to use, it'll need to create those instances, so lets make a constructor to make those instances. 

We'll call it Shooter, and have it take in a ShooterIO parameter so it knows which one we want it to make. 

```java
public final class Shooter extends SubsystemBase {
    ...
    public Shooter(ShooterIO hardware) {

    this.hardware = hardware;

    }
    ...
}
```

There will be two constructors: one handling creating the real/sim instances called "create" and another handling the fake instance called "none". The first constructor, returning either a RealShooter subsystem or a SimShooter subsystem, will decide which one through an if statement checking if we are connected to a physical robot (literally Robot.isReal()), while the second one just always returns a NoShooter.

```java
public final class Shooter extends SubsystemBase {
    ...
    public static Shooter create() {
        return Robot.isReal() ? new Shooter(new RealShooter()) : new Shooter(new SimShooter());
    }

    public static Shooter none() {
        return new Shooter(NoShooter());
    }
    ...
}
```

This bit should look familiar now: a getVelocity method. It will be the exact same as we previously did in this guide, just using hardware as the object instead (Why is there no setVoltage? Wait and you'll see).

```java
public final class Shooter extends SubsystemBase {
    ...
    public double getVelocity() {
        return hardware.velocity();
    }
    ...
}
```

Next, we'll make an update method using the PID and FF systems we made earlier. This method will run every tick, allowing it to constantly update the velocity setpoint (velocity we want the motor to go to) so that the motor is always aiming to go to at correct speed. Essentially, it will constantly find the voltages to get to a desired speed, then set the voltage to that found voltage.

```java
public final class Shooter extends SubsystemBase {
    ...
    public void update(double velocitySetpoint) {

    //makes sure the velocity it tries to go to does not exceed the max/min
    double velocity =
        MathUtil.clamp(
            velocitySetpoint,
            -MAX_VELOCITY.in(RadiansPerSecond),
            MAX_VELOCITY.in(RadiansPerSecond));

    //calculated the needed voltages using PID and FF 
    double ffVolts = feedforward.calculate(velocity);
    double pidVolts = controller.calculate(getVelocity(), velocity);

    hardware.setVoltage(MathUtil.clamp(pidVolts + ffVolts, -MAX_VOLTAGE, MAX_VOLTAGE));

    }
    ...
}
```

<small>-> "Clamp" makes sure a value does not go beyond a set max/min.</small>

Lastly, we'll add our commands which will be used to control the shooter in our central control Robot.java file. This part might a bit unfamiliar, since its dealing with lambdas, but the rest should look relatively fine.

ok lets doig it

First, we'll make two methods, both named runShooter, which both return a command. Where these two will differ, however, is in their inputs: one will be take in a DoubleSupplier velocity, while the other will take in just a double velocity.

```java
    public Command runShooter(DoubleSupplier velocity) {}

    public Command runShooter(double velocity) {}
```

Lets make the DoubleSupplier-using method first. This one will be the one to actually return the command which runs the shooter (which is why it takes in a DoubleSupplier so the input can constantly update to the correct velocity instead of just staying stuck at one value) using the "run" and "update" method. 

Since we need to return a command (a type of action), we can't just return a method as that will just return one value. Instead, we will need to use two things: the "run" method and a lambda function. The lambda allows the update <i>method</i>, the action we want to perform, to essentially act as a "Runnable" <i>object</i>, allowing us to use "run" on it and return it as a command.

All in all, this method should:

- return a Command using the run method 
- with the parameter of run being a lambda calling our update method 
- and using the DoubleSupplier voltage as its input

<small>-> use getAsDouble of velocity since the update method only accepts doubles.</small>

```java

    public Command runShooter(DoubleSupplier velocity) {
        return run(() -> update(velocity.getAsDouble()))
    }

```

The second runShooter method (the "double" one) will just call the DoubleSupplier one with a lambda. This will be the one we want to actually want to call when we call "runShooter", since we can actually give it a double velocity.

```java
    public Command runShooter(double velocity) {
        return runShooter(() -> velocity)
    }

```

## Secret SimShooter jumpscare

Hopefully you still remember that I said we'd be coming back to SimShooter, because there was one thing we didn't understand previously that we'll add now. 

In your method body for setVoltage, add a second line calling the update method on our shooter object with "PERIOD" in seconds as our input.

```java
    ...
    public void setVoltage(double voltage) {
        shooter.setInputVoltage(voltage);
        shooter.update(PERIOD.in(Seconds));

    }
    ...
```

![thumbs up](./images/CUPTOASTTHUMBSUP.jpeg) Cogleruntiations! You made the code for a simple shooter.

