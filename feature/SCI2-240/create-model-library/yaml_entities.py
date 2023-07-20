import datetime
from dataclasses import dataclass
from typing import List, Optional

from models import Author, Tag, License, Source, Doi, FileTypes, Connection


@dataclass
class ProjectYaml:
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
    # pathToParentProject
    parent_project: Optional[str] = None


@dataclass
class FileYaml:
    data_file: str
    file_name: str
    subclass: FileTypes
    file_license: License
    file_source: Source
    file_source_link: str
    # path to parent project
    parent_project: str
    # Optionals
    title: Optional[str] = None
    description: Optional[str] = None
    authors: Optional[List[Author]] = None
    tags: Optional[List[Tag]] = None
    connections: Optional[List[Connection]] = None
    doi: Optional[Doi] = None
    organization: Optional[str] = None
    latest_update_date: Optional[datetime.datetime] = None


@dataclass
class YamlFileDescription:
    name: str
    content: str


@dataclass
class Result:
    name: str
    files: List[YamlFileDescription]
