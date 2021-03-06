{
	'name': 'Ideas Emp',
	'description': 'This module allow employees in the company to raise and create ideas and after approval of ideas other employees in departments can vote for that idea',
	'author': 'A3 - Proyek 4',
	'depends': ['base', 'mail', 'hr'],
	'application': True,
	'data': [
		'views/ideas_view.xml', 
		'views/employee_ideas_menu.xml', 
		'views/ideas_types.xml',
		'views/wizard_view.xml',
		'security/ir.model.access.csv',
		'reports/todo_report.xml',
	],
}