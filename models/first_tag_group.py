from tag_data import TagData


class FirstTagNames:
    tag1 = 'tag1'
    tag2 = 'tag2'
    tag3 = 'tag3'


def first_tag_group() -> dict:
    first_tags = {}
    tag_names = FirstTagNames

    first_tags[tag_names.tag1] = TagData(
        name=tag_names.tag1,
        value=1,
        data_type='int',
        status='Default'
    )
    first_tags[tag_names.tag2] = TagData(
        name=tag_names.tag2,
        value='Hello',
        data_type='str',
        status='Default'
    )
    first_tags[tag_names.tag3] = TagData(
        name=tag_names.tag3,
        value=3.14,
        data_type='float',
        status='Default'
    )

    return first_tags
