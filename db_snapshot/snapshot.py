from __future__ import unicode_literals

import os, json
import frappe
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

	def update(self, ddict):
		self.data.update(ddict)
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
		self.data.update({self.name: snapshotname})
		save_snapshots_data(self.data)

	def restore(self):
		restore_from_file(self.get())


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


def restore_from_file(filename):
	args = {
		"filename": filename,
		"user": frappe.conf.db_name,
		"password": frappe.conf.db_password,
		"db_name": frappe.conf.db_name,
		"db_host": frappe.db.host,
	}

	cmd_string = """gunzip < %(filename)s | mysql -u %(user)s -p%(password)s %(db_name)s -h %(db_host)s""" % args
	frappe.utils.execute_in_shell(cmd_string)
	frappe.clear_cache()
