# Introduction

Control theory focuses on guiding systems from their current state to a desired state by manipulating inputs to achieve specific outputs. This is done by using feedback and feedforward to correct errors and make mechanisms more accurate. This guide will introduce these basic ideas and point you to more detailed resources. Many of the projects you’ll work on will use these concepts, so it's important to understand how they work.

To get started, read [this](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/control-system-basics.html) document on control systems. It shows how control systems are used in everyday life and why they’re important. It also breaks down basic concepts and uses diagrams to explain how most systems work.
### Open vs. closed loop control

**Open-loop control**, commonly known as *feedforward*, functions by sending control signals based on predetermined estimates, not by adjusting for the system's current state. This means it operates without feedback, relying only on initial assumptions about how the mechanism should behave.

 There are two main types of feedforward: [plant inversion and unmodeled dynamics](https://file.tavsys.net/control/controls-engineering-in-frc.pdf). simply put, plant inversion uses the model to determine the control signals needed to reach the desired outcome. Whereas unmodeled dynamics handles factors not accounted for in the model. 
 
 As seen below, feedforward is usually depicted as a straight path regardless of the "loop" in its name.

![open](https://github.com/user-attachments/assets/1321a465-9b2d-4a4c-8f58-94f8705e3cb5)

**Closed-loop control**, on the other hand, incorporates *feedback* to adjust the system's output in real time. By constantly monitoring the actual performance and comparing it to the desired state, it can correct any discrepancies and respond to disturbances effectively. This dynamic process ensures greater accuracy and reliability in maintaining the intended performance.

![closed](https://github.com/user-attachments/assets/60c66396-76a8-4663-a94b-7cef06472dae)

Read [this](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/picking-control-strategy.html) document for specifics on both *feedforward* and *feedback*. Near the end, it also goes into specifics on tuning your constant values for feedforward and feedback. For more assistance with tuning, check out the [common tuning issues guide](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/common-control-issues.html).
### PID

A PID controller is an optimized `feedback` system that continuously adjusts output using three terms: **P**roportional for immediate error, **I**ntegral for accumulated error over time, and **D**erivative for predicting future error trends. This combination allows for precise correction and stable system performance as seen below. It's heavily suggested that you read [this document](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/introduction-to-pid.html) for more details.

![PID graph](https://github.com/user-attachments/assets/e17c59e9-327e-49e9-b2bf-9c360df42d1d)
### Implementation

Actually adding these complicated ideas into code may seem hard, but thankfully it's mostly done for us. Use the following links to add [PID](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/controllers/pidcontroller.html), [feedforward](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/controllers/feedforward.html), and how to [combine both the ideas](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/controllers/combining-feedforward-feedback.html) for a near perfect system setpoint following. Do keep in mind that the specific way in which these are implemented may vary depending on the mechanism being used on.  
## Summary

Only after you have read all of the linked documents, watch the following video. It acts as a great summary for this whole idea of control theory its used for FRC purposes. You should be able to recall and understand most of the important details mentioned!
[Video with everything + more](https://www.youtube.com/watch?v=UOuRx9Ujsog) (Watch until 9:00).

If you want to further indulge yourself into the art of control, there is an [amzaing textbook](https://file.tavsys.net/control/controls-engineering-in-frc.pdf) specifically for control theory and its applications for FRC.
