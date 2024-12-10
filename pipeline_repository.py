import json


class AbstractPipelineRepository:
    def get(self, ref: str) -> list:
        raise NotImplementedError


class JsonPipelineRepository(AbstractPipelineRepository):
    def get(self, json_file_path: str) -> list:
        return json.load(open(json_file_path))
