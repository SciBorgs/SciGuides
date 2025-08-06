# Notes from 2025

2025 was cool. But it would've been cooler if we went to Worlds (reminder, as of this season, our last time was 2019.)

So here's a few things that went wrong on our end.

## The Off-season

We planned to get proper vision and path following. We did not invest the proper time into it. Autos decided the game this year (and usually does each year). 

We did not have proper vision or path following by the end of it :(

## Outdated/No Longer Supported Libraries

In the middle of our season, we wanted to update PhotonVision to experiment with the newest pose estimation algorithm aimed at localization from singular tags. We could not. Instead, we faced [this](https://github.com/PhotonVision/photonvision/blob/923f9564dc6d1f47c02fd7e1c2bab6ab150e91b1/photon-lib/src/main/java/org/photonvision/PhotonCamera.java#L184) on build :

![Photonvision does not support older OpenCV version](/images/photon-unsupported-ver-death.png)
###### mb gang couldn't recreate it without a robot lolol

After too much time spent digging, we found that [Monologue](https://github.com/shueja/Monologue), which had run unsupported from 2024, was holding back the OpenCV update. This wasn't great. Staying with the current Monologue would prevent us from updating to any future versions of PhotonVision.

Thus, in the middle of the season, we moved away from Monologue to update to [Epilogue](). It worked out, but it was a decent amount of change, especially for the time.

Consider each of the libraries you're using before the season begins, and find possible alternatives.

## Loop Overruns

<!-- ### Too many things; too little time (to test); too inefficient

2025 was the first year we had tried many, many advanced programming things at the same time. This includes:

- on-the-fly pathing (with Repulsor)
- acceleration limiting
- 250hz wheel odometry
- More -->

### Deferred Commands (my opp)

Use deferred commands **sparingly**, especially for larger, beefier commands.

One reason why commands are so efficient is that they are effectively pre-loaded when built and deployed. This makes them very quick to schedule.

Deferred commands do away with this benefit; instead, commands will be scheduled with the arguments given when *it is called*, spiking runtimes for that loop.

### Garbage Collection

Java sucks. Observe the attached picture:

See those periodic spikes?

### VisualVM

So how can you identify these problems?

See the WPILib docs. They are accurate. They work (unless they don't).

### Other minor optimizations

- Mutablity (dangerous!)
- Knowing the difference between method calls that ping immediate retrieval from a sensor vs a cached value
- Loop timing

###### Note: the new 2027 control system will have much faster specs, and thus, loop timings. This, hopefully, should be less of an issue then.

## Cameras

### Placement

### Optimizations and what things mean

## Replace batteries when they are less than 60% charged

When batteries are low on charge, they will 

We've actually faced many issues here and in the past with this. Here goes:
- on SciDuck, our elevator was inconsistent in reaching its target due to a mix of mechanical shenanigans. Sometimes, voltage would randomly spike and overmax the elevator, causing terrible, horrible, bad, and terrible screeching sounds.
- on TFC (Crescendo)