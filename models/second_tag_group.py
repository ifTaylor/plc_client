<<<<<<< HEAD
from tag_data import TagData


class SecondTagNames:
    tag1 = 'tag1'
    tag2 = 'tag2'
    tag3 = 'tag3'


def second_tag_group() -> dict:
    second_tags = {}
    tag_names = SecondTagNames

    second_tags[tag_names.tag1] = TagData(
        name=tag_names.tag1,
        value=1,
        data_type='int',
        status='Default'
    )
    second_tags[tag_names.tag2] = TagData(
        name=tag_names.tag2,
        value='Hello',
        data_type='str',
        status='Default'
    )
    second_tags[tag_names.tag3] = TagData(
        name=tag_names.tag3,
        value=3.14,
        data_type='float',
        status='Default'
    )

    return second_tags
=======
from tag_data import TagData


class SecondTagNames:
    tag1 = 'tag1'
    tag2 = 'tag2'
    tag3 = 'tag3'


def second_tag_group() -> dict:
    second_tags = {}
    tag_names = SecondTagNames

    second_tags[tag_names.tag1] = TagData(
        name=tag_names.tag1,
        value=1,
        data_type='int',
        status='Default'
    )
    second_tags[tag_names.tag2] = TagData(
        name=tag_names.tag2,
        value='Hello',
        data_type='str',
        status='Default'
    )
    second_tags[tag_names.tag3] = TagData(
        name=tag_names.tag3,
        value=3.14,
        data_type='float',
        status='Default'
    )

    return second_tags
>>>>>>> 8619df6771e2bb89d06a8d802c282bf417d56805
