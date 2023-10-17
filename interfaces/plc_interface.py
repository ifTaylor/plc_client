from pylogix import PLC
import logging


client_logger = logging.getLogger(__name__)


class PLCInterface:
    def __init__(
        self,
        ip: str = '0.0.0.0',
        slot: int = 0,
        timeout: int = 5,
        tags: dict = {}
    ) -> None:
        self.ip = ip
        self.slot = slot
        self.timeout = timeout
        self.tags = tags
        self.PLC = None
        self.max_string_length = 82
        self.results = []

        if self.ip != '':
            self.PLC = PLC(self.ip, self.slot, self.timeout)

    def read_tags(self, tag_enum):
        tag_names = []
        for key in tag_enum:
            tag_name, _, data_type = tag_enum[key]
            tag_names.append(tag_name)

        try:
            responses = self.PLC.Read(
                tag_names,
                len(tag_names),
                None
            )
        except Exception as e:
            print(e)
            responses = []

        for i, key in enumerate(tag_enum):
            tag_name, _, data_type = tag_enum[key]
            new_value = responses[i].Value
            tag_enum[key] = (tag_name, new_value, data_type)

        return tag_enum

    def write_tags(self, tag_enum):
        write_data = []
        for key in tag_enum:
            tag_name, tag_value, data_type = tag_enum[key]

            if data_type == 'str':
                truncated_tag_value = tag_value[:self.max_string_length]
                write_data.append((tag_name, str(truncated_tag_value)))
            elif data_type == 'float':
                try:
                    write_data.append((tag_name, float(tag_value)))
                except ValueError:
                    write_data.append((tag_name, -1))
            elif data_type == 'int':
                try:
                    write_data.append((tag_name, int(tag_value)))
                except ValueError:
                    write_data.append((tag_name, -1))

        if write_data:
            ret = self.PLC.Write(write_data)

            for r in ret:
                client_logger.info(f'{r.Value} to {r.TagName}: {r.Status}')

    def update_tag_in_label_tag(self, label_tag, tag_value):
        for key in label_tag:
            tag_name, _, data_type = label_tag[key]
            modified_tuple = (tag_name, tag_value, data_type)
            label_tag[key] = modified_tuple
        return label_tag
