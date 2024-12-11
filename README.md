# Cross-DCC Collaboration Framework

This framework is designed to enable seamless collaboration across multiple DCC (Digital Content Creation) tools by acting as a flexible script runner. It executes tasks based on user-defined JSON pipeline files, providing flexibility without enforcing strict rules about formats or workflows.

## Goal
To support workflows like creating a sphere in Maya, exporting it, and rendering it in Houdini, while preserving the unique strengths of each tool.

## Key Features
1. **Independent Script Runner**  
   - Operates independently and sends commands to DCC tools (e.g., Maya, Houdini) without embedding into any single tool.

2. **Respects Specialized Capabilities**  
   - Avoids over-abstraction, letting each tool excel in its strengths (e.g., lighting in Katana, effects in Houdini).

3. **User-Defined Pipelines**  
   - Users define their own workflows in JSON files, specifying scripts, interpreters, and arguments for each task. The framework executes these tasks sequentially as described in the pipeline.

4. **Ease of Adoption**  
   - Artists can continue using familiar tools and scripts without learning new workflows or dealing with unnecessary abstractions.

## Example Workflow
1. Create a sphere and export it in Maya.
2. Import and render the sphere in Houdini with added lights and cameras.

## How to Use
1. Prepare your pipeline JSON file (see `example_pipeline.json` for reference).
2. Run the pipeline using:
   ```bash
   python pipeline.py <pipeline_file>
   ```

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
    Example output:
    ```
    Created file poem.txt with text My poem: 
    Appended text roses are red, violets are blue to poem.txt
    My poem: roses are red, violets are blue
    Replaced violets with pills in poem.txt
    My poem: roses are red, pills are blue
    Removed file poem.txt
    Pipeline example_pipeline.json executed successfully
    ```
