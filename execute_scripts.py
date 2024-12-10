import script_repository
import instruction_repository
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
    parser.add_argument("intruct_file", type=str)
    parser.add_argument("index", type=int)
    args = parser.parse_args()
    instructions = instruction_repository.JsonInstructionRepository().get(
        args.intruct_file
    )

    instruction = instructions[args.index]
    script_repository = script_repository.FileSystemScriptRepository()
    execute_scripts(
        instruction["interpreter"], instruction["scripts"], script_repository
    )
