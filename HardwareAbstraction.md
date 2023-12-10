# Hardware Abstraction

In robot projects, subsystem files for a robot will typically group core <u>subsystem logic</u> and <u>hardware logic</u> within the same file. This guide aims to explain a different way of structuring subsystems, called **hardware abstraction**, which separates general subsystem commands from the hardware it relies on.

## Implementation

With this system, a subsystem separates all its hardware methods into a separate interface called an **IO interface**.
This can include methods like returning the current state of a mechanism, or actuating it towards a given state.

With this, we can create several **IO implementations** of a subsystem that implement the IO interface. Each implementation will provide the same input and output methods defined in the IO interface, but will have varying implementations of those methods **depending on the hardware being used.**

In our main subsystem class, we can instantiate whichever IO implementation makes the most sense (i.e. instantiating an implementation of a mechanism that uses CANSparkMax motor controllers as opposed to an implementation that uses TalonSRXs) and interact with whatever hardware we're using through this implementation.

Below is an example diagram of creating a subsystem for an Arm.

![Diagram of subsystem structure](https://i.imgur.com/FPie7cR.png)

In the diagram above, we make an IO interface that represents a joint on a single-jointed arm mechanism, and make 3 different implementations of this interface that
* interacts with real hardware on the robot (`RealJoint.java`)
* uses an arm simulation to estimate states when voltages are inputted (`SimJoint.java`)
* doesn't interact with hardware at all, and renders a mechanism unuseable, in case of mechanical/electrical faults during competition (`NoJoint.java`)

Since all of these classes implement `JointIO.java`, we can instantiate different implementations depending on what we want (i.e. between real life and simulation), quickly changing the hardware our mechanism depends on without altering any of the higher level commands that are defined in the subsystem itself.

## An example

Let's say we're working on a simple elevator subsystem powered by a single motor. Without hardware abstraction, your subsystem may look something like:


```java
public class Elevator extends SubsystemBase {
    private final CANSparkMax motor;

    private final Encoder encoder;

    private final PIDController pid;
    private final ElevatorFeedforward ff;

    public Elevator() {
        ...
    }

    /** Returns height of the elevator from the floor, in meters */
    public double getHeight() {
        return encoder.getDistance();
    }

    /**
     * Moves elevator to a specified setpoint.
     *
     * @param setpoint The desired state, in [meters, meters / second]
     * @return A command that updates the elevator setpoint to the desired state
     */
    public Command goTo(State setpoint) {
        return run(() -> updateSetpoint(setpoint));
    }

    /** Sets the setpoint of the elevator to a desired state in [meters, meters / second] */
    public void updateSetpoint(State setpoint) {
        double ffOutput = ff.calculate(setpoint.velocity);
        double pidOutput = pid.calculate(getHeight(), setpoint.position);

        motor.setVoltage(ffOutput + pidOutput);
    }
}
```

Instead of this, we can separate all the logic that handles the hardware on the robot into an `ElevatorIO` interface...
```java
public interface ElevatorIO {
    /** Returns height of the elevator from the floor, in meters */
    public double getHeight();

    /** Sets the setpoint of the elevator to a desired state in [meters, meters / second] */
    public void updateSetpoint(State setpoint);
}
```
...and create an IO implementation that extends this interface with hardware we'd use on the real robot:

```java
public class RealElevator implements ElevatorIO {
    private final CANSparkMax motor;

    private final Encoder encoder;

    private final PIDController pid;
    private final ElevatorFeedforward ff;

    public RealElevator() {
        ...
    }

    public double getHeight() {
        return encoder.getDistance();
    }

    public void updateSetpoint(State setpoint) {
        double ffOutput = ff.calculate(setpoint.velocity);
        double pidOutput = pid.calculate(getHeight(), setpoint.position);

        motor.setVoltage(ffOutput + pidOutput);
    }
}
```

Our main Elevator subsystem class will now look something like...
```java
public class Elevator extends SubsystemBase {
    private final ElevatorIO elevator;

    public Elevator(ElevatorIO elevator) {
        this.elevator = elevator;
    }

    /**
     * Moves elevator to a specified setpoint.
     *
     * @param setpoint The desired state, in [meters, meters / second]
     * @return A command that updates the elevator setpoint to the desired state
     */
    public Command goTo(State setpoint) {
        return run(() -> elevator.updateSetpoint(setpoint));
    }
}
```
...where we instantiate the IO implementation we want and pass it into the subsystem's constructor.

Fundamentally, the overall implementation of our Elevator subsystem has not changed significantly. We simply just separated methods that handle closed loop control and hardware into an IO implementation, which the main subsystem calls *through* `elevator` in commands such as `goTo`. We can also make a simulated elevator implementation...
```java
public class SimElevator implements ElevatorIO {
    private final ElevatorSim sim;

    private final PIDController pid;
    private final ElevatorFeedforward ff;

    public SimElevator() {
        ...
    }

    public double getHeight() {
        return sim.getPositionMeters();
    }

    public void updateSetpoint(State setpoint) {
        double ffOutput = ff.calculate(setpoint.velocity);
        double pidOutput = pid.calculate(getHeight(), setpoint.position);

        sim.setInputVoltage(ffOuput + pidOutput);
        sim.update(Constants.PERIOD); // Updates the simulation at a tick rate of 20ms
    }
}
```

...and pass an instantiation of this into the subsystem constructor whenever we are in robot simulation mode:
```java
private final Elevator elevator = new Elevator(Robot.isReal() ? new RealElevator() : new SimElevator());
```

In the long run, this subsystem structure will save a lot of time throughout the season and during competitions, by letting you be extremely flexible with the different ways you can actually implement your subsystem.

## Links and other examples

* This structure was inspired by FRC Team 6328 and their data logging/replay tool [AdvantageKit](https://github.com/Mechanical-Advantage/AdvantageKit), which works best when following this type of subsystem structure.
* Our code for [Charged Up 2023](https://github.com/SciBorgs/ChargedUp-2023) also follows this structure.
