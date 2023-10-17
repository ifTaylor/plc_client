from typing import Any, Dict
from first_tag_group import FirstTagNames, first_tag_group
from second_tag_group import SecondTagNames, second_tag_group


class TagData:
    def __init__(
        self,
        name: str = '',
        value: Any = None,
        data_type: str = '',
        status: str = '',
    ) -> None:
        self.Name = name
        self.Value = value
        self.DataType = data_type
        self.Status = status


def get_all_tags() -> Dict[str, TagData]:
    all_tags = {}

    all_tags.update(first_tag_group())
    all_tags.update(second_tag_group())

    return all_tags


class TestTagData:
    FirstTagNames.tag1 = 123
    FirstTagNames.tag2 = 456
    FirstTagNames.tag3 = 789
    SecondTagNames.tag1 = 123
    SecondTagNames.tag2 = 456
    SecondTagNames.tag3 = 789
