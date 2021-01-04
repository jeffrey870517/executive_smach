SMACH
=====

SMACH is a task-level python execution framework for rapidly composing complex
robot behaviors.

![travis](https://travis-ci.org/jbohren/executive_smach.svg?branch=master)

## Neuron APP of SMACH
Add an example of Neuron APP with SMACH. This example works with [Neuronbot2](https://github.com/Adlink-ROS/neuronbot2) simulator of ADLINK. 

### Usage:
1. Install the [Neuronbot2](https://github.com/Adlink-ROS/neuronbot2) simulator and run the navigation using the mememan map.
2. Run the SMACH-FSM to navigate around the world.
```bash
ros2 run smach_napp smach_nav2_client 
```