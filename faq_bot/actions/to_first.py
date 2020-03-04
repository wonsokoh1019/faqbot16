# !/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import tornado.gen
import logging
from faq_bot.model.i18n_data import make_i18n_text
from faq_bot.externals.send_message import push_message
from faq_bot.model.cachehandle import get_user_status, clean_user_status
import gettext
_ = gettext.gettext


@tornado.gen.coroutine
def to_first(account_id, __, ___):
    process_flag = False
    if not clean_user_status(account_id):
        process_flag = True

    if process_flag:
        fmt = _("Cannot be selected since you are currently in Initial Menu. \n\n"
                "Select it if you want to find FAQ or go back to Initial Menu "
                "while the person in charge is checking your question.")
        content = make_i18n_text("Cannot be selected since you are currently "
                            "in Initial Menu. \n\n"
                            "Select it if you want to find FAQ or go back to "
                            "Initial Menu while the person in charge is "
                            "checking your question.", "to_first", fmt)
    else:
        fmt = _("Moved to FAQ Initial Menu.\n\nPlease select an item from the menu below.")
        content = make_i18n_text(
            "Moved to FAQ Initial Menu.\n\nPlease select an item from the menu below.",
            "to_first", fmt)

    yield push_message(account_id, content)