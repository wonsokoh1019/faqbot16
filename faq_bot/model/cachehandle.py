#!/bin/env python
# -*- coding: utf-8 -*-
"""
cacheout for save bot status .
"""

__all__ = ['set_replace_user_info', 'set_user_status',
           'get_user_status', 'clean_user_status']

from cacheout import Cache
import time

cache = Cache(maxsize=20000, ttl=60*60*60, timer=time.time)

def set_replace_user_info(account, status, process, type):
    """
    insert or update user's status.
    :param account: user account.
    :param status: user text input status.
    :param process: processing progress.
    :param type: business type.
    :return: Return false when status is None Else, Return None
    """
    info = cache.get(account, {})

    info["account"] = account
    info["status"] = status
    info["process"] = process
    info["type"] = type

    cache.set(account, info)


def set_user_status(account, status=None, process=None, type=None, message=None):
    """
    update user's status.
    :param account: user account
    :param type: business type.
    :param status: user text input status.
    :param process: processing progress.
    :param message: user input message.
    :return: no
    """
    info = cache.get(account, {})

    if status is not None:
        info["status"] = status
    if message is not None:
        info["message"] = message
    if process is not None:
        info["process"] = process
    if type is not None:
        info["type"] = type

    cache.set(account, info)


def get_user_status(account):
    """
    select user's status.
    :param account: user account
    :return: status info
    """
    info = cache.get(account, {})
    status = info.get("status", None)
    process = info.get("process", None)
    type = info.get("type", None)
    message = info.get("message", None)
    return status, process, type, message


def clean_user_status(account):
    """
    delete a item.
    :param account: user account
    """
    return cache.delete(account)

