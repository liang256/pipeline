import pipeline_repository
import subprocess
import argparse
import os


def subprocess_run_instruction(
    pipeline_ref: str,
    pipeline_repo: pipeline_repository.AbstractPipelineRepository,
) -> None:
    pipeline = pipeline_repo.get(pipeline_ref)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_dir, "execute_pipeline_by_index.py")
    for index, task in enumerate(pipeline):
        interpreter = task["interpreter"]
        try:
            result = subprocess.run(
                [interpreter, script_path, pipeline_ref, str(index)],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            print(f"Error executing task {index} in pipeline {pipeline_ref}")
            return

    print(f"Pipeline {pipeline_ref} executed successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    args = parser.parse_args()
    pipeline_repository = pipeline_repository.JsonPipelineRepository()
    subprocess_run_instruction(args.file, pipeline_repository)
