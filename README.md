# Pipeline Framework Documentation

This framework is designed to execute workflows across various interpreters (e.g., mayapy, hython, nuke, blender). It organizes tasks into pipelines, where each task is associated with a specific interpreter and a sequence of steps.

## Structure Overview

### Pipeline

A pipeline represents the overall execution unit that contains one or more tasks. Each task is executed independently by its respective interpreter.

### Task

A task is associated with a specific interpreter and consists of a list of steps. These steps define the operations to be executed sequentially.

### Step

A step specifies an individual operation within a task. It includes the script ID to identify the operation and any arguments required to execute it.