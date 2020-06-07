import frappe
from frappe import _
from frappe.utils import nowdate,add_days


@frappe.whitelist()
def send_invitation_emails(meeting):
    meeting = frappe.get_doc("Meeting",meeting)
    meeting.check_permission('email')

    #if meeting.status =="Planned":
    for v_attendee in meeting.attendees:
        frappe.sendmail(
            recipients=v_attendee.attendee,
            sender=frappe.session.user,
            subject=meeting.subject,
            message=meeting.invitation_message,
            reference_doctype=meeting.doctype,
            reference_name=meeting.name
        )
    meeting.status = "Invitation Sent"
    meeting.save()
    frappe.msgprint(_("Invitation sent"))


    #else:
        #frappe.msgprint(_("Meeting status must be 'Planned'"))

@frappe.whitelist()
def get_meetings(start,end):
    if not frappe.has_permission("Meeting","read"):
        raise frappe.PermissionError
    
    return frappe.db.sql("""select
        timestamp(`date`,from_time) as start,
        timestamp(`date`,to_time) as end,
        name,
        subject,
        status,
        0 as all_day
        from `tabMeeting`
        where `date` between %(start)s and %(end)s""",{
            "start":start,
            "end":end
        },as_dict=True)

def make_orientation_meeting(doc,method):
    meeting = frappe.get_doc({
        "doctype":"Meeting",
        "subject":"Orientation for {0}".format(doc.first_name),
        "date": add_days(nowdate(),1),
        "from_time":"09:00",
        "to_time": "09:30",
        "status":"Planned",
        "attendees":[{
            "attendee":doc.name
        }]
    })
    meeting.flags.ignore_permissions = True
    meeting.insert()
    frappe.msgprint(_("Orientation meeting created"))
