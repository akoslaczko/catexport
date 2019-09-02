# -*- coding: utf-8 -*-
{
	'name': 'Macskaexport Professional',
	'version': '0.1',
	'summary': 'Manage Cats and Partners',
	'category': 'Tools',
	'author': 'Akos Laczko',
	'maintainer': 'HRYou',
	'company': 'HRYou',
	'depends': ['base'],
	'data': [
		'security/ir.model.access.csv',
        'views/cat_view.xml'
	],
	'images': [
		'static/description/icon.png'
	],
	'license': 'MIT',
	'installable': True,
	'application': True,
	'auto_install': False,
}