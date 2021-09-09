import time
import base64
from Crypto.Cipher import AES

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)
    
def pad(text):
    """
    #填充函数，使被加密数据的字节码长度是block_size的整数倍
    """
    length = AES.block_size
    count = len(text.encode('utf-8'))
    add = length - (count % length)
    entext = text + (chr(add) * add)
    return entext


def get_encrypt(text):
    """
    获取token时请求数据加密
    """
    key = 'szewecszewecszew'
    aes = AES.new(key.encode('utf-8'),AES.MODE_ECB)
    res = aes.encrypt(pad(str(text)).encode("utf8"))
    msg = str(base64.b64encode(res), encoding="utf8")
    return msg


# class EncryptDate:
#     def __init__(self, key):
#         self.key = key  # 初始化密钥
#         self.length = AES.block_size  # 初始化数据块大小
#         self.aes = AES.new(self.key.encode("utf8"), AES.MODE_ECB)  # 初始化AES,ECB模式的实例
#         # 截断函数，去除填充的字符
#         self.unpad = lambda date: date[0:-ord(date[-1])]
#
#     def pad(self, text):
#         """
#         #填充函数，使被加密数据的字节码长度是block_size的整数倍
#         """
#         count = len(text.encode('utf-8'))
#         add = self.length - (count % self.length)
#         entext = text + (chr(add) * add)
#         return entext
#
#     def encrypt(self, encrData):  # 加密函数
#         res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
#         msg = str(base64.b64encode(res), encoding="utf8")
#         return msg
#
#     def decrypt(self, decrData):  # 解密函数
#         res = base64.decodebytes(decrData.encode("utf8"))
#         msg = self.aes.decrypt(res).decode("utf8")
#         return self.unpad(msg)
    
def get_time():
    return int(round(time.time()*1000))