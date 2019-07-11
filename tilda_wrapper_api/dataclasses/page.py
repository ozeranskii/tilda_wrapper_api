# Standard libraries
from dataclasses import dataclass, field
from typing import List, Optional

# Third party libraries
from dataclasses_json import dataclass_json

# Project
from tilda_wrapper_api.dataclasses.base import BaseObject


@dataclass_json
@dataclass(frozen=True)
class Page:
    id: int
    projectid: int
    title: str
    descr: str
    img: str
    featureimg: str
    alias: str
    date: str
    sort: int
    published: int
    filename: Optional[str] = ""
    html: Optional[str] = ""
    images: List[str] = field(default_factory=list)


@dataclass_json
@dataclass(frozen=True)
class SinglePage(BaseObject):
    result: Page


@dataclass_json
@dataclass(frozen=True)
class Pages(BaseObject):
    result: List[Page] = field(default_factory=list)
