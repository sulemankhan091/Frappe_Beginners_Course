// Copyright (c) 2024, Muhammad Suleman and contributors
// For license information, please see license.txt

frappe.query_reports["Server Side Script Report"] = {
	filters: [
		{
			"fieldname": "name",
			"label": __("Server Side Scripting"),
			"fieldtype": "Link",
			"options":"Server Side Scripting",
			"reqd": 1,
		},
		{
			"fieldname": "dob",
			"label": __("DOB"),
			"fieldtype": "Date",
			// "options":"Serverside Scripting",
			// "reqd": 1,
		},{
			"fieldname": "age",
			"label": __("Age"),
			"fieldtype": "Data",
			// "options":"Serverside Scripting",
			// "reqd": 1,
		},
	],
};
