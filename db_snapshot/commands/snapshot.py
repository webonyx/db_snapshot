from __future__ import unicode_literals
import click
import frappe
import os
from db_snapshot.snapshot import get_snapshots_data, SnapshotGenerator, restore_from_file
from frappe.commands import pass_context, get_site


@click.command('take')
@click.argument('name')
@pass_context
def take(context, name):
	site = get_site(context)
	frappe.init(site=site)
	frappe.connect()
	SnapshotGenerator(name).take()
	frappe.db.close()


@click.command('restore')
@click.argument('name')
@pass_context
def restore(context, name):
	site = get_site(context)
	frappe.init(site=site)
	frappe.connect()
	SnapshotGenerator(name).restore()
	frappe.db.close()
	print "Restored"


@click.command('restore-from-file')
@click.argument('filename')
@pass_context
def restore_from_file(context, filename):
	if not os.path.exists(filename):
		raise IOError('"{}" does not exists'.format(filename))

	site = get_site(context)
	frappe.init(site=site)
	frappe.connect()
	restore_from_file(filename)
	frappe.db.close()
	print "Restored"


@click.command('delete')
@click.argument('name')
@pass_context
def delete(context, name):
	site = get_site(context)
	frappe.init(site=site)
	SnapshotGenerator(name).delete()


@click.command('list')
@pass_context
def list(context):
	site = get_site(context)
	frappe.init(site=site)

	for name, filename in get_snapshots_data().items():
		print name


commands = [
	take,
	list,
	restore,
	restore_from_file,
	delete,
]
