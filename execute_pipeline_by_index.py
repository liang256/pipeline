import script_repository
import pipeline_repository
import argparse


def execute_scripts(
    interpreter: str,
    scripts: list,
    script_repository: script_repository.AbstractScriptRepository,
):
    for script in scripts:
        script_id = script["script_id"]
        args = script["args"]
        script_instance = script_repository.get(interpreter, script_id)
        script_instance.run(**args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pipeline_json_file", type=str)
    parser.add_argument("index", type=int)
    args = parser.parse_args()
    pipeline = pipeline_repository.JsonPipelineRepository().get(args.pipeline_json_file)

    task = pipeline[args.index]
    script_repository = script_repository.FileSystemScriptRepository()
    execute_scripts(task["interpreter"], task["steps"], script_repository)
