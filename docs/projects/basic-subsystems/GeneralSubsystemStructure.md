# Introduction

This project is going to cover the general structure of a standard subsystem.

## Standard subsystem structure

Generally, a subsystem folder consists of:

- a constants file.
- an IO file
- a "fake" version of the subsystem
- a simulated version of the subsystem
- a real version of the subsystem
- the main subsystem file

[cool picture of example folder here]

Different subsystems may differ in the amount of files they contain (Drive being a good example).

## Constants

The constants file, as the name suggests, contains constants specific to the subsystem.

In the file:

- Subsystem specific constants are defined.

## Subsystem IO

The IO file (Input/Output) is a interface that the fake, sim, and real files implement. It contains the core methods necessary for the subsystem.

In the file:

- Methods are instantiated

## Fake File

The fake file is a file which implements the IO file, but all methods within it either return zero or have a empty body (does nothing).
It serves as both a way to test the robot without needing to load a specific subsystem or as an "emergency stop" in the case of some kind of failure to prevent damage.

In the file:

- Methods from IO file are added.
- All methods from the IO file return zero / are left empty.

## Sim File

The sim file is a file which implements the IO file, and sets up a simulated version of the subsystem.nIt serves as a way to test the subsystem virtually, without connecting to the physical robot. (very useful because physical robot testing time is very small)

In the file:

- An object representing the simulated subsystem is created (with proper parameters).
- Methods use the simulated object to affect the simulation.

## Real File

The real file is a file which implements the IO file, and sets up a real version of the subsystem. It serves as the file which is used when connected to a physical robot, and is the file responsible for setting up motors and such.

In the file:

- Objects representing the physical parts of the robot are created.
- Settings for parts of subsystem used are configured.

## "Main" Subsystem File

The "Main" Subsystem file is a file which extends SubsystemBase, and is responsible for deciding which of the three files that extend the IO (fake, sim, real) is used. It is the file which controls the hardware of the subsystem.

In this file:

- An object representing hardware of the robot is created.
- Fake, sim, and real factory methods are written
- Commands are written
- x







