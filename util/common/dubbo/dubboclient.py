# -*- coding:utf-8 -*-
# Power by godaipl 2018-11-27 11:02:35
# 摘自网络，修改了部分代码 data = json.loads(data[0].decode(self.__encoding, 'ignore'),
# encoding=self.__encoding)
# https://tw.saowen.com/a/c7085d77c8efae501fcbd454079a53f77d54f1001d5830b0e70e990985987a5e

import json
import socket
import telnetlib


class dubbo:
    # 定義私有屬性
    __init = False
    __encoding = "gbk"
    __finish = b'dubbo>'  # 基於python3修改
    __connect_timeout = 10
    __read_timeout = 10

    # 定義構造方法
    def __init__(self, host, port):
        self.host = host
        self.port = port
        if host is not None and port is not None:
            self.__init = True

    def set_finish(self, finish):
        '''
        defualt is ``dubbo>``
        '''
        self.__finish = finish

    def set_encoding(self, encoding):
        '''
        If ``result retured by dubbo`` is a ``str`` instance and is encoded
         with an ASCII based encoding
        other than utf-8 (e.g. latin-1) then an appropriate ``encoding`` name
        must be specified. Encodings that are not ASCII based (such as UCS-2)
        are not allowed and should be decoded to ``unicode`` first.
        '''
        self.__encoding = encoding

    def get_encoding(self):
        return self.__encoding

    def set_connect_timeout(self, timeout):
        '''
        Defines a timeout for establishing a connection with a dubbo server.
        It should be noted that this timeout cannot usually exceed 75 seconds.

        defualt is ``10``
        '''
        self.__connect_timeout = timeout

    def set_read_timeout(self, timeout):
        '''
        Defines a timeout for reading
        a response expected from the dubbo server.

        defualt is ``10``
        '''
        self.__read_timeout = timeout

    def do(self, command):
        # 連線Telnet伺服器
        try:
            tn = telnetlib.Telnet(
                host=self.host, port=self.port, timeout=self.__connect_timeout)
        except socket.error as err:
            print("[host:%s port:%s] %s" % (self.host, self.port, err))
            return

        # 觸發doubble提示符
        tn.write(b'\n')  # 基於python3修改

        # 執行命令
        tn.read_until(self.__finish, timeout=self.__read_timeout)
        # command=command.encode()
        # print("command",command,type(command.encode()))
        tn.write(b'%s\n' % command.encode())  # 基於python3修改
        # tn.write(b'%s\n' % bytes(command))      #基於python3修改

        # 獲取結果
        data = b''
        while data.find(self.__finish) == -1:
            data = tn.read_very_eager()

        try:
            data = data.split(b"\n")  # 基於python3修改
            data = json.loads(
                data[0].decode(self.__encoding, 'ignore'),
                encoding=self.__encoding)
        except Exception as ValueError:
            print('error ', ValueError)
            data = data[0]
        # data = json.loads(data[0], encoding=self.__encoding)

        tn.close()  # tn.write('exit\n')

        return data

    def invoke(self, interface, method, param):
        cmd = "%s %s.%s(%s)" % ('invoke', interface, method, param)
        return self.do(cmd)
