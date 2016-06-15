from openerp import models,fields,api,exceptions

class getMaxSalary(models.Model):
    _inherit = "hr.contract"

    is_max_salary=fields.Binary()


    def salaryMaxFiveHundred(self):
        for rec in self:
            if rec.wage >5000:
                print self
                pass
            pass
        pass
