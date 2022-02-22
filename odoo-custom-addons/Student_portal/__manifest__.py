{
    'name' : 'Student portal',
    'version' : '1.1',
    'summary': 'Student details',
    'sequence': -9,
    'description': """fetching student details""" ,
    'author': 'Sushant Shankar',

    'category': 'education',
    'depends' : [],
    'data': ['views/student_view.xml','security/ir.model.access.csv'],



    'installable': True,
    'application': True,
    'auto_install': False,
    
    'license': 'LGPL-3',
}
