# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "db_snapshot"
app_title = "DB Snapshot"
app_publisher = "Viet Pham"
app_description = "Utility app for database snapshot taking and restoring."
app_icon = "octicon octicon-database"
app_color = "green"
app_email = "viet@webonyx.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/db_snapshot/css/db_snapshot.css"
# app_include_js = "/assets/db_snapshot/js/db_snapshot.js"

# include js, css files in header of web template
# web_include_css = "/assets/db_snapshot/css/db_snapshot.css"
# web_include_js = "/assets/db_snapshot/js/db_snapshot.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "db_snapshot.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "db_snapshot.install.before_install"
# after_install = "db_snapshot.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "db_snapshot.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"db_snapshot.tasks.all"
# 	],
# 	"daily": [
# 		"db_snapshot.tasks.daily"
# 	],
# 	"hourly": [
# 		"db_snapshot.tasks.hourly"
# 	],
# 	"weekly": [
# 		"db_snapshot.tasks.weekly"
# 	]
# 	"monthly": [
# 		"db_snapshot.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "db_snapshot.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "db_snapshot.event.get_events"
# }

