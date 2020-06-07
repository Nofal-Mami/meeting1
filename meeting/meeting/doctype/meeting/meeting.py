# -*- coding: utf-8 -*-
# Copyright (c) 2020, Nofal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Meeting(Document):
	def validate(self):
		found=[]
		for v_attendee in self.attendees:
			#if not v_attendee.full_name:
				#v_attendee.full_name = get_full_name(v_attendee.attendee)
			
			if v_attendee.attendee in found:
				frappe.throw(_("Attendee {0} entred twice").format(v_attendee.attendee))
			found.append(v_attendee.attendee)



@frappe.whitelist()
def get_full_name(attendee):
	user = frappe.get_doc("User",attendee)
	return " ".join(filter(None,[user.first_name,user.middle_name, user.last_name]))
