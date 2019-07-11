
# Standard libraries
from dataclasses import dataclass

# Third party libraries
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True)
class TildaError(Exception):
    status: str
    message: str
    errorside: str

    def __str__(self):
        return str(self.message)
