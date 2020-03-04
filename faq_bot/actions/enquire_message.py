# !/bin/env python
# -*- coding: utf-8 -*-
"""
Prompt user for enquire message
"""

__all__ = ['enquire_message']

import tornado.web
import tornado.gen
import asyncio
from faq_bot.model.i18n_data import make_i18n_text
from faq_bot.constant import TYPES
from faq_bot.model.cachehandle import set_replace_user_info, \
    get_user_status, set_user_status
from faq_bot.externals.send_message import push_messages
import gettext
_ = gettext.gettext


@tornado.gen.coroutine
def enquire_message(account_id, callback, __):
    """
    This function prompts the user for a message.

    :param account_id: user account id.
    :param callback: Callback corresponding to business type.
    """

    status, __, ___, ____ = get_user_status(account_id)
    if status == 'wait_in':
        set_user_status(account_id, status="none")

    fmt = _("You have selected {type}. Please write to me your question.")
    content1 = make_i18n_text("You have selected {type}. "
                              "Please write to me your question.".format(
        type=TYPES[callback]), "enquire_message", fmt, type=callback)

    fmt = _("Only one message can be delivered. "
            "Please write your question at one go.")
    content2 = make_i18n_text("Only one message can be delivered. "
                              "Please write your question at one go.",
                              "enquire_message", fmt)

    yield asyncio.sleep(0.5)

    set_replace_user_info(account_id, 'wait_in', 'doing', callback)

    yield push_messages(account_id, [content1, content2])

