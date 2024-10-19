frappe.pages['programming-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'My Page',
		single_column: true
	});
}

// page.set_title="My Page";
// page.set_indicator('green','done')

$(frappe.render_template('programming_page',{})).appendTo(page.body);