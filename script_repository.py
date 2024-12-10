import importlib


class AbstractScript:
    def run(self):
        raise NotImplementedError


class AbstractScriptRepository:
    def get(self, interpreter: str, script_id: str) -> AbstractScript:
        raise NotImplementedError


class FileSystemScriptRepository(AbstractScriptRepository):
    def get(self, interpreter: str, script_id: str) -> AbstractScript:
        module_name = f"scripts.{interpreter}.{script_id}"
        script_module = importlib.import_module(module_name)
        return script_module
