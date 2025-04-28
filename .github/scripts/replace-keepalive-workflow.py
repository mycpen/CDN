#!/usr/bin/python
# -*- coding: UTF-8 -*-

from datetime import datetime, timedelta, timezone

# 获取当前 UTC 时间
utc_now = datetime.now(timezone.utc)

# 创建东八区的时区
east_8 = timezone(timedelta(hours=8))

# 将当前 UTC 时间转换为东八区时间
east_8_now = utc_now.astimezone(east_8)

# 格式化时间 2025/04/28 00:00:00
east_8_now = east_8_now.strftime('%Y/%m/%d %H:%M:%S')

# 文本替换 当前时间
def replace(replace_file_name):
    with open(replace_file_name, "w", encoding = "UTF-8") as f1:
        f1.write(east_8_now)
    f1.close()

# 具体文件路径
file_name = './.keepalive'

# 替换 .keepalive 时间内容，达成 keepalive-workflow
if __name__ == '__main__':
    replace(file_name)
