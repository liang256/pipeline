import importlib
import json

class AbstractScript:
    def run(self):
        raise NotImplementedError

class AbstractScriptRepository:
    def get(self, interpreter: str, script_id: str) -> AbstractScript:
        raise NotImplementedError
    
class AbstractInstructionRepository:
    def get(self, ref: str) -> list:
        raise NotImplementedError
    
class FileSystemScriptRepository(AbstractScriptRepository):
    def get(self, interpreter: str, script_id: str) -> AbstractScript:
        module_name = f"scripts.{interpreter}.{script_id}"
        script_module = importlib.import_module(module_name)
        return script_module
    
class JsonInstructionRepository(AbstractInstructionRepository):
    def get(self, json_file_path: str) -> list:
        return json.load(open(json_file_path))
    
def execute_instruction(instruction: list, script_repository: AbstractScriptRepository):
    for step in instruction:
        interpreter = step["interpreter"]
        for script in step["scripts"]:
            script_id = script["script_id"]
            args = script["args"]
            script_instance = script_repository.get(interpreter, script_id)
            script_instance.run(**args)

if __name__ == "__main__":
    instruction = JsonInstructionRepository().get("instruction.json")
    script_repository = FileSystemScriptRepository()
    execute_instruction(instruction, script_repository)