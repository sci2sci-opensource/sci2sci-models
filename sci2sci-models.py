import datetime
from dataclasses import dataclass
from enum import StrEnum
from typing import List
from typing import Optional


"""These classes are the base models"""


@dataclass()
class FileTypes(StrEnum):
    Spreadsheet = 'spreadsheet'
    Archive = 'archive'
    StructuredText = 'structured_text'
    Unknown = 'unknown'

    def __str__(self):
        return str(self.value)

    __repr__ = __str__


@dataclass
class Author:
    display_name: str
    orcid: Optional[str] = None
    first_name: str = ""
    last_name: str = ""


@dataclass
class License:
    name: str
    url: str


@dataclass
class Tag:
    name: str


@dataclass()
class ConnectionTypes(StrEnum):
    References = 'references'
    Referenced_in = 'referenced_in'
    Mentions = 'mentions'
    Mentioned_in = 'mentioned_in'

    def __str__(self):
        return str(self.value)

    __repr__ = __str__


@dataclass
class Connection:
    url: str
    connection_type: ConnectionTypes

@dataclass
class Source:
    name: str
    url: str


@dataclass
class Doi:
    doi: str
    url: str = ""


@dataclass
class Project:
    title: str
    description: str
    authors: List[Author]
    tags: List[Tag]
    connections: List[Connection]
    project_license: License
    project_source: Source
    doi: Doi
    project_source_link: str
    latest_update_date: Optional[datetime.datetime] = None
    organization: Optional[str] = None
    parent_project: Optional['Project'] = None


@dataclass
class File:
    data_file: str
    file_name: str
    subclass: FileTypes
    file_license: License
    file_source: Source
    parent_project: Project
    file_source_link: str
    # Optionals
    title: Optional[str] = None
    description: Optional[str] = None
    authors: Optional[List[Author]] = None
    tags: Optional[List[Tag]] = None
    connections: Optional[List[Connection]] = None
    doi: Optional[Doi] = None
    organization: Optional[str] = None
    latest_update_date: Optional[datetime.datetime] = None


@dataclass()
class ProjectWithFiles:
    parentProject: Project
    files: List[File]



