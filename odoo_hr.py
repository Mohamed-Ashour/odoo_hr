
from openerp import models,fields,api

class odooHrInhired(models.Model):
    _inherit ="hr.attendance"
    image=fields.Binary()
    test=fields.Text()
    @api.model
    def create(self, values):
        print values['employee_id']
        contacts1 = self.env['hr.employee'].search([('id','=',values['employee_id'])])
        values['image']=contacts1.image
        return super(odooHrInhired,self).create(values)
