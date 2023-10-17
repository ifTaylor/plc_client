from typing import Dict
from tag_models.tag_data import (
    TagData,
    get_all_tags,
    TestTagData
)


class FirstClient:
    def __init__(
        self,
        plc_interface
    ):
        self.plc_interface = plc_interface

    def modify_tags(
        self,
        read_values: TestTagData,
        tags_to_modify: dict[str, TagData]
    ) -> dict[str, TagData]:
        for tag_name in tags_to_modify:
            if tag_name in dir(read_values):
                tag_value = getattr(read_values, tag_name)
                tags_to_modify[tag_name].Value = tag_value

        return tags_to_modify

    def write(
        self,
        tag_data: dict[str, TagData]
    ):
        self.plc_interface.write_tags(tag_data)

    def run(self):
        # Read
        read_values = TestTagData()

        # Modify
        all_tags = get_all_tags()
        all_tags = self.modify_tags(
            read_values,
            all_tags
        )

        # Write
        self.write(all_tags)