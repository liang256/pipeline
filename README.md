# Pipeline Framework Documentation

This framework is designed to execute workflows across various interpreters (e.g., mayapy, hython, nuke, blender). It organizes tasks into pipelines, where each task is associated with a specific interpreter and a sequence of steps.

## Structure Overview

### Pipeline

A pipeline represents the overall execution unit that contains one or more tasks. Each task is executed independently by its respective interpreter.

### Task

A task is associated with a specific interpreter and consists of a list of steps. These steps define the operations to be executed sequentially.

### Step

A step specifies an individual operation within a task. It includes the script ID to identify the operation and any arguments required to execute it.

## Get Started

To get started with the pipeline framework, follow these steps:

1. **Install Python**: Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Clone the Repository**: Clone the project repository to your local machine.
    ```sh
    git clone https://github.com/liang256/pipeline.git
    cd pipeline
    ```

3. **Run the Pipeline**: Execute the pipeline using the following command:
    ```sh
    python3 pipeline.py example_pipeline.json
    ```

4. **Monitor the Execution**: The framework will execute each task in the pipeline sequentially, using the specified interpreters and steps. Monitor the output for any errors or completion messages.

By following these steps, you can set up and run your own workflows using the pipeline framework.
