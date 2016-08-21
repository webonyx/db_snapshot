from __future__ import unicode_literals

import os, json
import frappe
from frappe.installer import extract_sql_gzip, import_db_from_sql
from frappe.utils import get_site_path, get_site_base_path, get_backups_path
from frappe.utils.backups import new_backup


class SnapshotGenerator:
	def __init__(self, name):
		self.name = name
		self.data = {}

	def get(self):
		return self.list()[self.name] or None

	def exists(self):
		return self.name in self.list()

	def list(self):
		if not self.data:
			self.data = get_snapshots_data()

		return self.data

	def delete(self):
		data = get_snapshots_data()

		for key in list(data):
			if key == self.name:
				os.unlink(data[key])
				del data[key]

		self.data = data
		save_snapshots_data(data)

	def update_path(self, path):
		self.data.update({self.name: path})
		save_snapshots_data(self.data)

	def take(self):
		if self.exists():
			return self.get()

		backup = new_backup(ignore_files=True)
		snapshot_path = get_snapshots_path()
		filename = os.path.join(get_backups_path(), os.path.basename(backup.backup_path_db))
		snapshotname = os.path.join(snapshot_path, os.path.basename(backup.backup_path_db))

		if not os.path.exists(snapshot_path):
			os.mkdir(snapshot_path)

		os.rename(filename, snapshotname)
		self.update_path(snapshotname)

	def restore(self):
		path = str(self.get())
		restore_from_file(path)
		if path.endswith('sql.gz'):
			self.update_path(path[:-3])


def get_snapshots_path():
	return get_site_path("private", "snapshots")


def get_snapshots_config_path():
	return os.path.join(get_site_base_path(), "snapshots.json")


def save_snapshots_data(data):
	with open(get_snapshots_config_path(), 'w') as f:
		json.dump(data, f, indent=1, sort_keys=True)


def get_snapshots_data():
	config_path = get_snapshots_config_path()
	if not os.path.exists(config_path):
		return {}

	else:
		with open(config_path, 'r') as f:
			return json.load(f)


def restore_from_file(sql_file_path):
	frappe.flags.in_install_db = True

	if sql_file_path.endswith('sql.gz'):
		sql_file_path = extract_sql_gzip(os.path.abspath(sql_file_path))

	import_db_from_sql(sql_file_path, True)

	frappe.flags.in_install_db = False
	frappe.clear_cache()
