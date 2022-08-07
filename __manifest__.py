# -*- coding: utf-8 -*-
{
    'name': "ach_expense_supplier",
    'summary': """
        Supplir in invoice funtion expense""",
    'description': """
        Supplir in invoice funtion expense
    """,
    'author': "ACH",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['hr_expense', 'hr_expense_invoice'],
    'data': [
        'views/hr_expense.xml',
    ]
}
