// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.views.calendar["Meeting"] = {
	field_map: {
		"start": "start",
		"end": "end",
		"id": "name",
		"title": "subject",
		"docstatus": 1
	},
	get_events_method: "meeting.meeting.api.get_meetings"
}