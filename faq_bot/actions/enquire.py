# !/bin/env python
# -*- coding: utf-8 -*-
"""
Handle user selection ask a person
"""

__all__ = ['enquire']

import tornado.web
import tornado.gen
from faq_bot.model.i18n_data import make_i18n_text
from faq_bot.actions.message import create_quick_replay
from faq_bot.externals.send_message import push_message
from faq_bot.model.cachehandle import set_replace_user_info
import gettext
_ = gettext.gettext

@tornado.gen.coroutine
def enquire(account_id, __, ___):
    """
    This function handles the user's selection of ask a person

    :param account_id: user account id.
    """
    set_replace_user_info(account_id, "none", "doing", "none")
    fmt = _("Select a task related to your question.")
    content = make_i18n_text("Select a task related to your question.",
                             "enquire", fmt)

    content["quickReply"] = create_quick_replay()

    yield push_message(account_id, content)
