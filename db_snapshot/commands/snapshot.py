from __future__ import unicode_literals
import click
import frappe
from db_snapshot.snapshot import get_snapshots_data, SnapshotGenerator
from frappe.commands import pass_context, get_site


@click.command('take')
@click.argument('name')
@pass_context
def take(context, name):
	from db_snapshot.snapshot import take_snapshot as _take_snapshot

	site = get_site(context)
	frappe.init(site=site)
	frappe.connect()
	_take_snapshot(name)

	frappe.db.close()


@click.command('restore')
@click.argument('name')
@pass_context
def restore(context, name):
	from db_snapshot.snapshot import restore_snapshot

	site = get_site(context)
	frappe.init(site=site)
	frappe.connect()
	restore_snapshot(name)

	frappe.db.close()


@click.command('remove')
@click.argument('name')
@pass_context
def remove(context, name):
	site = get_site(context)
	frappe.init(site=site)
	sn = SnapshotGenerator(name)
	sn.remove()


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
	remove,
]
