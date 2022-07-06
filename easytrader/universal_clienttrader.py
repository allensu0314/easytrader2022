# -*- coding: utf-8 -*-

import pywinauto
import pywinauto.clipboard

from easytrader import grid_strategies
from . import clienttrader
from contextlib import redirect_stdout


class UniversalClientTrader(clienttrader.BaseLoginClientTrader):
    grid_strategy = grid_strategies.Xls

    @property
    def broker_type(self):
        return "universal"

    def login(self, user, password, exe_path, comm_password=None, **kwargs):
        """
        :param user: 用户名
        :param password: 密码
        :param exe_path: 客户端路径, 类似
        :param comm_password:
        :param kwargs:
        :return:
        """
        self._editor_need_type_keys = False
        self._app = pywinauto.Application(backend="uia").connect(path=exe_path, timeout=10)
        dlg = self._app.window(title='同花顺远航版')
        # dlg.Button5.click()
        # dlg['交易Dialog'].menu_select("模拟炒股 - UI**57")
        # dlg = dlg.window(title="网上股票交易系统5.0")    
        self._main = dlg.window(title="网上股票交易系统5.0")