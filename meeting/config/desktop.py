from __future__ import unicode_literals
import frappe
from frappe import _

def get_data():
	return [
		# Meeting
		{
			"module_name": "meeting",
			"category": "Modules",
			"label": _("Meeting"),
			"color": "#3498db",
			"icon": "octicon octicon-repo",
			"type": "module",
			"description": "Meeting"
		},
	]
