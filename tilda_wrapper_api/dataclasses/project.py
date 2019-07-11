# Standard libraries
from dataclasses import dataclass, field
from typing import List, Optional

# Third party libraries
from dataclasses_json import dataclass_json

# Project
from tilda_wrapper_api.dataclasses.base import BaseObject


@dataclass_json
@dataclass(frozen=True)
class Project:
    id: int
    title: str
    descr: str
    export_csspath: Optional[str] = ""
    export_jspath: Optional[str] = ""
    export_imgpath: Optional[str] = ""
    indexpageid: Optional[int] = None
    htaccess: Optional[str] = ""
    customdomain: Optional[str] = ""
    images: List[str] = field(default_factory=list)
    css: List[str] = field(default_factory=list)
    js: List[str] = field(default_factory=list)


@dataclass_json
@dataclass(frozen=True)
class SingleProject(BaseObject):
    result: Project


@dataclass_json
@dataclass(frozen=True)
class Projects(BaseObject):
    result: List[Project] = field(default_factory=list)
