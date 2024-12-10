import instruction_repository
import subprocess


def subprocess_run_instruction(
    instruction_ref: str,
    instruction_repository: instruction_repository.AbstractInstructionRepository,
):
    instructions = instruction_repository.get(instruction_ref)
    for index, instruction in enumerate(instructions):
        interpreter = instruction["interpreter"]
        subprocess.run([interpreter, "execute_scripts.py", instruction_ref, str(index)])


if __name__ == "__main__":
    instruction_repository = instruction_repository.JsonInstructionRepository()
    subprocess_run_instruction("instruction.json", instruction_repository)
