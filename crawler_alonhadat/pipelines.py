# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlerAlonhadatPipeline:
    def process_item(self, item, spider):
        # Thực hiện xử lý dữ liệu cho mỗi item ở đây
        self.convert_item_values(item)
        return item

    def convert_item_values(self, item):
        def convert_value(value):
            if value == "/publish/img/check.gif":
                return 1
            elif value is None or value == "_" or value == "---":
                return 0
            else:
                return value

        for key in item:
            item[key] = convert_value(item[key])



