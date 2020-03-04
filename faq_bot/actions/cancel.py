# !/bin/env python
# -*- coding: utf-8 -*-
"""
Deal cancel ask a person
"""

__all__ = ['cancel']

import tornado.web
import tornado.gen
from faq_bot.model.i18n_data import make_i18n_text
from faq_bot.externals.send_message import push_message
from faq_bot.model.cachehandle import get_user_status, clean_user_status
import gettext
_ = gettext.gettext

@tornado.gen.coroutine
def cancel(account_id, __, ___):
    """
    This function handles user cancellation inquiry.

    :param account_id: user account id.
    """
    status, ____, __, ___ = get_user_status(account_id)
    if status != "done":
        # todo add error prompt
        raise HTTPError(500, "user status error. status error")

    fmt = _("You have canceled your question. "
            "Please re-select the task from the menu below.")
    content = make_i18n_text("You have canceled your question. "
                             "Please re-select the task from the menu below.",
                             "cancel", fmt)
    clean_user_status(account_id)
    yield push_message(account_id, content)