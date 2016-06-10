from openerp import models, fields, api

class odooAttendenceInherit(models.Model):
    _inherit ="hr.attendance"

    @api.multi
    def _late_compute(self):
        for record in self:
            if record.action == 'sign_in':
                record.late = record.time - record.start_time
        return True

    @api.multi
    def _overtime_compute(self):
        for record in self:
            end_of_time = 2 + record.end_time
            if record.action == 'sign_out':
                record.overtime = record.time - end_of_time
            if record.overtime <0:
                record.overtime = 0
            return True

    @api.model
    def create(self, values):
        contacts1 = self.env['hr.employee'].search([('id','=',values['employee_id'])])
        contract = self.env['hr.contract'].search([('employee_id','=',values['employee_id'])])
        values['image']=contacts1.image
        values['start_time']=contract.working_from
        values['end_time']=contract.working_to
        return super(odooAttendenceInherit,self).create(values)

    @api.multi
    def write(self, values):
        contacts1 = self.env['hr.employee'].search([('id','=',values['employee_id'])])
        contract = self.env['hr.contract'].search([('employee_id','=',values['employee_id'])])
        values['image']=contacts1.image
        values['start_time']=contract.working_from
        values['end_time']=contract.working_to
        return super(odooAttendenceInherit,self).write(values)


    image=fields.Binary()
    time=fields.Float(string="time", required=True)
    late=fields.Float(compute=_late_compute)
    overtime=fields.Float(compute=_overtime_compute)
    start_time=fields.Float(string="start_time")
    end_time=fields.Float(string="end_time")










