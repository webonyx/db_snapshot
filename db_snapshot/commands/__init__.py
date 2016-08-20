# Copyright (c) 2015, Web Notes Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals, absolute_import
import click

click.disable_unicode_literals_warning = True

def call_command(cmd, context):
	return click.Context(cmd, obj=context).forward(cmd)

def get_commands():
	# prevent circular imports
	from .snapshot import commands as snapshot_commands

	return list(set(snapshot_commands))

commands = get_commands()
