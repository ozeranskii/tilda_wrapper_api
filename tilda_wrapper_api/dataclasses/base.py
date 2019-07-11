# Standard libraries
from dataclasses import dataclass
from typing import Any

# Third party libraries
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True)
class BaseObject:
    status: str
    result: Any
