
from openerp import models,fields,api

class odooHrInhired(models.Model):
    _inherit ="hr.attendance"
    image=fields.Binary()
   # test=fields.Text()
    @api.onchange('employee_id','image')
    @api.model
    def create(self, values):
        contacts1 = self.env['hr.employee'].search([('id','=',values['employee_id'])])
        values['image']=contacts1.image
        return super(odooHrInhired,self).create(values)


    #
    @api.onchange('employee_id')
    def _onchange_nameEmployee(self):
        print self
         # set auto-changing field
        #self.price = self.amount * self.unit_price
        # Can optionally return a warning and domains
        #contacts1 = self.env['hr.employee'].search([('id','=',values['employee_id'])])
        #values['image']=contacts1.image
        return {
            'warning': {
                'title': "Something bad happened",
                'message': "It was very bad indeed",
            }
        }