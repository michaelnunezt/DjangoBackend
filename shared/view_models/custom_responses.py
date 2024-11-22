from typing import Union, Any
import json

from shared.Enums import StatusEnum, ProjectEnum


class APIResponse:
    def __init__(self, status: StatusEnum, project: ProjectEnum, data: Union[str, list, tuple, dict, None] = None,
                 message: str = None, **kwargs):
        if not isinstance(status, StatusEnum):
            raise ValueError(f"Invalid status: {status}. Must be a member of StatusEnum.")
        if not isinstance(project, ProjectEnum):
            raise ValueError(f"Invalid project: {project}. Must be a member of ProjectEnum.")

        self.status: StatusEnum = status.value  # Use the value of the Enum
        self.data: Union[str, list, tuple, dict, Any] = data
        self.project: ProjectEnum = project.value  # Use the value of the Enum
        self.message: str | None = message
        self.extra = kwargs

    def to_dict(self):
        response = {"status": self.status, "project": self.project}
        if self.data:
            response["data"] = self.data
        if self.message:
            response["message"] = self.message
        response.update(self.extra)
        return response

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def success(cls, project: ProjectEnum, data=None, message=None, **kwargs):
        return cls(StatusEnum.SUCCESS, project, data, message, **kwargs)

    @classmethod
    def error(cls, message, project: ProjectEnum, data=None, **kwargs):
        return cls(StatusEnum.ERROR, project, data, message, **kwargs)
