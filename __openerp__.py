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

        'security/odoo_hr_security.xml',
        'security/ir.model.access.csv',

        'odoo_hr_attendence_view.xml',
        'odoo_hr_payslip_view.xml',
        'odoo_hr_devorce.xml',
        
        'views/leaves_report.xml',
        'odoo_hr_report.xml',
        'wizard/hr_holidays_summary_employee_view.xml',
        'wizard/hr_employee_salary.xml',

    ],
}