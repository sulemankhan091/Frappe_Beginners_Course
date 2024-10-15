# Copyright (c) 2024, Muhammad Suleman and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe import frappe
from frappe import _


class ServerSideScripting(Document):
  
	def validate(self):
		self.get_value()

	def get_value(self):
		first_name, age = frappe.db.get_value('Clientside Scripting','PRE0005',['firstname','age'])
		frappe.msgprint(_("The Parent Firstname is {0} and age is {1}").format(first_name,age))

	
		
