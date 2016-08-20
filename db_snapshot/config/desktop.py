# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "DB Snapshot",
			"color": "green",
			"icon": "octicon octicon-database",
			"type": "module",
			"label": _("DB Snapshot")
		}
	]
