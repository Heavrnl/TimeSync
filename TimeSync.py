import ntplib
import time
from datetime import datetime, timezone
import win32api

ntp_servers = [
    'pool.ntp.org',
    'ntp.ntsc.ac.cn',
    'cn.ntp.org.cn',
    'edu.ntp.org.cn',
    'ntp1.aliyun.com',
    'ntp2.aliyun.com',
    'ntp3.aliyun.com',
    'ntp4.aliyun.com',
    'ntp5.aliyun.com',
    'ntp6.aliyun.com',
    'ntp7.aliyun.com',
    'ntp.tencent.com',
    'ntp1.tencent.com',
    'ntp2.tencent.com',
    'ntp3.tencent.com',
    'ntp4.tencent.com',
    'ntp5.tencent.com',
    'ntp.sjtu.edu.cn',
    'ntp.neu.edu.cn',
    'ntp.bupt.edu.cn',
    'ntp.shu.edu.cn',
    'ntp.tuna.tsinghua.edu.cn',
    'cn.pool.ntp.org',
    '0.cn.pool.ntp.org',
    '1.cn.pool.ntp.org',
    '2.cn.pool.ntp.org',
    '3.cn.pool.ntp.org'
]

def sync_time_with_ntp(servers):
    for server in servers:
        try:
            client = ntplib.NTPClient()
            response = client.request(server, version=3, timeout=5)
            utc_time = datetime.fromtimestamp(response.tx_time, timezone.utc)

            # 从微秒数计算毫秒数
            milliseconds = utc_time.microsecond // 1000

            win32api.SetSystemTime(utc_time.year, utc_time.month, utc_time.weekday(),
                                   utc_time.day, utc_time.hour, utc_time.minute,
                                   utc_time.second, milliseconds)
            return True
        except Exception:
            time.sleep(1)
    return False

if __name__ == "__main__":
    while True:
        success = sync_time_with_ntp(ntp_servers)
        if not success:
            print("同步时间失败，请检查网络连接或 NTP 服务器。")
        time.sleep(3600)
