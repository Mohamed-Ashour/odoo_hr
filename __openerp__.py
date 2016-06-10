{
    'name':'ITI HR',
    'version': '1.0',
    'depends':['hr','hr_attendance', 'hr_contract', 'hr_payroll', 'resource'],
    'description': """
ITI HR
==========================
Adding Egyptian rules to HR module
    """,
    'data': [
        'odoo_hr_view.xml',
        'odoo_hr_contarct_view.xml',
        'hr_salary_structure_data.xml',
        'odoo_hr_attendence_view.xml'
    ],
}