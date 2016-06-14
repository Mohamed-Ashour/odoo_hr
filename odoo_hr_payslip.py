from openerp import models, fields, api


class odooPayslipInherit(models.Model):
    _inherit = "hr.payslip"
    total_late = fields.Float()

    @api.model
    def create(self,vals):
        period_attendance = self.env["hr.attendance"].search([('employee_id','=',vals['employee_id']),('check_date','>=',vals['date_from']),('check_date','<=',vals['date_to'])])
        result = 0
        for day in period_attendance:
            result += day.late
        vals['total_late'] = result
        return super(odooPayslipInherit,self).create(vals)






