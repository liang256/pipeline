import pipeline_repository
import subprocess
import argparse


def subprocess_run_instruction(
    instruction_ref: str,
    instruction_repository: pipeline_repository.AbstractPipelineRepository,
):
    instructions = instruction_repository.get(instruction_ref)
    for index, instruction in enumerate(instructions):
        interpreter = instruction["interpreter"]
        subprocess.run(
            [interpreter, "execute_pipeline_by_index.py", instruction_ref, str(index)]
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    args = parser.parse_args()
    pipeline_repository = pipeline_repository.JsonPipelineRepository()
    subprocess_run_instruction(args.file, pipeline_repository)
