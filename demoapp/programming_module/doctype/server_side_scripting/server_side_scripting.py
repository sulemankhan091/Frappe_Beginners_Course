# Copyright (c) 2024, Muhammad Suleman and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe import frappe
from frappe import _


class ServerSideScripting(Document):
  

### Getting Values from document ###

	# def validate(self):
		# self.get_value()

	# def get_value(self):
		# first_name, age = frappe.db.get_value('Clientside Scripting','PRE0005',['firstname','age'])
		# frappe.msgprint(_("The Parent Firstname is {0} and age is {1}").format(first_name,age))

		
		### Setting Values of a doctype ###
		# def validate(self):
		# 	self.set_value()

		# def set_value(self):	
		# 	frappe.db.set_value('Clientside Scripting','PRE0005','age',25)
		# 	first_name, age = frappe.db.get_value('Clientside Scripting','PRE0005',['firstname','age'])
		# 	frappe.msgprint(_("The Parent Firstname is {0} and age is {1}").format(first_name,age))


					### frappe db.exists method ###

		# def validate(slef):
		# 	if frappe.db.exists('Clientside Scripting','PRE0005'):
		# 		frappe.msgprint('This document exists in database')
		# 	else:
		# 		frappe.msgprint('The document does not exist')
    
					### frappe db.count method method ###
	# def validate(self):
	# 	doc_count = frappe.db.count('Clientside Scripting',{'enable':1})
	# 	frappe.msgprint(_("The Enable document count is {0}").format(doc_count))
  

					### frappe SQL Queries method ###
  
# 	def validate(self):
# 				self.sql()    
	
# 	def sql(self):
# 				data = frappe.db.sql("""
# SELECT firstname,age FROM `tabClientside Scripting` Where enable = 1
# """, as_dict=1)
# 				for d in data:
# 					frappe.msgprint(_("The Parent Firstname is {0} and age is {1}").format(d.firstname,d.age))

				