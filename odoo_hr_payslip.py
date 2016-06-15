from openerp import models, fields, api


class odooPayslipInherit(models.Model):
    _inherit = "hr.payslip"
    extra_working_hours = fields.Float()

    @api.model
    def create(self,vals):
        period_attendance = self.env["hr.attendance"].search([('employee_id','=',vals['employee_id']),('check_date','>=',vals['date_from']),('check_date','<=',vals['date_to'])])
        late_time = 0
        extra_time = 0
        for day in period_attendance:
            late_time += day.late
            extra_time += day.over_time
        late_time -= 2
        if late_time < 0:
            late_time = 0
        vals['extra_working_hours'] = (extra_time * 2) - late_time
        return super(odooPayslipInherit,self).create(vals)






