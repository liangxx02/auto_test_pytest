# -*- coding:utf-8 -*-

tob_project_name = ''


class UriEnums:
    """
    TOB_信审URI汇总
    """
    FETCH_ORDER = '/' + tob_project_name + + '/audit/fetchOrder'\
        if tob_project_name else tob_project_name + '/audit/fetchOrder'
