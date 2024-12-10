import json


class AbstractInstructionRepository:
    def get(self, ref: str) -> list:
        raise NotImplementedError


class JsonInstructionRepository(AbstractInstructionRepository):
    def get(self, json_file_path: str) -> list:
        return json.load(open(json_file_path))
