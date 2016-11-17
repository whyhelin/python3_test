#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。

# 获取当前datetime:
from datetime import datetime, timezone, timedelta

now = datetime.now()
print('now =', now)
print('type(now) =', type(now))

# 用指定日期时间创建datetime:
dt = datetime(1970, 1, 1, 8, 00)
print('dt =', dt)

# 把datetime转换为timestamp:
print('datetime -> timestamp:', dt.timestamp())

# 把timestamp转换为datetime:
t = dt.timestamp()
print('timestamp -> datetime:', datetime.fromtimestamp(t))
print('timestamp -> datetime as UTC+0:', datetime.utcfromtimestamp(t))

# 从str读取datetime:
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print('strptime:', cday)

# 把datetime格式化输出:
print('strftime:', cday.strftime('%a, %b %d %H:%M'))

# 对日期进行加减:
print('current datetime =', cday)
print('current + 10 hours =', cday + timedelta(hours=10))
print('current - 1 day =', cday - timedelta(days=1))
print('current + 2.5 days =', cday + timedelta(days=2, hours=12))

# 把时间从UTC+0时区转换为UTC+9:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc9_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('UTC+0:00 now =', utc_dt)
print('UTC+8:00 now =', utc9_dt)
print(utc_dt.timestamp())
print(utc9_dt.timestamp())


print('----------------------------------------------')
now = datetime.now()
print(now)
# 如果系统时区恰好是UTC+8:00，那么下面代码就是正确的，否则，就把UTC+8:00时区的时间强制变成UTC+9:00时区的时间
now = datetime.now().replace(tzinfo=timezone(timedelta(hours=9)))
print(now)
print('-------------------------------------------------')


def to_timestamp(dt_str, tz_str):
    utc_num = int(tz_str[3:-3])
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone(timedelta(hours=utc_num)))
    return dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1


t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')

