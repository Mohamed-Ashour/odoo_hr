from openerp import models, fields, api
import datetime
from time import strptime
from dateutil import relativedelta


class odooContractInhired(models.Model):

    _inherit = "hr.contract"

    @api.model
    @api.depends('date_start')
    def _compute_days(self):
        for record in self:
            date1 = datetime.datetime.strptime(str(self.date_today), '%Y-%m-%d')
            date2 = datetime.datetime.strptime(str(self.date_start), '%Y-%m-%d')
            result = ((date1 - date2).days / 30)
            record.totalMonth = result
            print record.totalMonth
        return record.totalMonth

    # ======================================================================================
    # @api.model
    # @api.depends('totalMonth')
    # def _insertHolidays(self):
    #     if self.totalMonth == 1:
    #         self.env['hr.holidays'].create({
    #             'employee_id': self.employee_id.id,
    #             'user_id': self.env.user.id,
    #             'name': 'zahra',
    #             'payslip_status': False,
    #             'holiday_type': 'category',
    #             'number_of_days_temp': 21,
    #             'state': 'validate',
    #             'number_of_days': 21,
    #             'type': 'add',
    #             'holiday_status_id': 1,
    #         })
    #         # self.env.cr.commit()
    #         print "heeeeeeeeeeeeeeere"


    variable = fields.Float(string='Variable', required=True)
    totalMonth = fields.Float(store=True, string='Total Month', compute=_compute_days)
    date_today = fields.Date.today()
            # =====================================================================================
    #
    # @api.model
    # @api.onchange('totalMonth')
    # def _insertHolidays(self):
    #     for record in self:
    #         if record.totalMonth == 1:
    #             result = {'value': {}}
    #             result['value']['employee_id'] = self.employee_id.id
    #             result['value']['user_id'] = self.env.user.id
    #             result['value']['name'] = 'zahra'
    #             result['value']['payslip_status'] = False
    #             result['value']['holiday_type'] = 'category'
    #             result['value']['number_of_days_temp'] = 21
    #             result['value']['state'] = 'validate'
    #             result['value']['number_of_days'] = 21
    #             result['value']['type'] = 'add'
    #             result['value']['holiday_status_id'] = 1
    #             self.env['hr.holidays'].create(result)
    #             print "heeeeeeeeeeeeeeere"
                # return super(odooContractInhired, self).create(result)

# =========================================================================
# if record.totalMonth == 1:
#     print "yeeeeeeeees"
#     print "id self ===> "
#     print self.employee_id.id
#     print "self ===>"
#     print self.env.user.id
#                  @api.model
# +    def create(self, values):
# +        print values['employee_id']
# +        contacts1 = self.env['hr.employee'].search([('id','=',values['employee_id'])])
# +        values['image']=contacts1.image
# +        return super(odooHrInhired,self).create(values)
#     def write(self, vals):
#         for record in self:
#             if record.totalMonth == 1 :
#                 print "teeeeeeee"
#                 self.env['hr.holidays'].create({
#                     'employee_id': self.employee_id.id,
#                     'user_id': self.env.user.id,
#                     'name': 'zahra',
#                     'payslip_status': False,
#                     'holiday_type': "category",
#                     'number_of_days_temp': 21,
#                     'state': 'validate',
#                     'number_of_days': 21,
#                     'type': 'add',
#                     'holiday_status_id':1,
#                      })
#
#                 # self.env.cr.commit()
#                 print "heeeeeeeeeeeeeeere"

# return super(odooContractInhired,self).create(vals)
# self.env['hr.holidays'].holidays_status_id = "1"
# self.env['hr.holidays'].number_of_days = "21"
# self.env['hr.holidays'].employee_id = self.employee_id
# self.env['hr.holidays'].holidays_type = "category"

#     leaves = self.env['hr.holidays'].search([('holiday_status_id','=','1')])
#     for leave in leaves:
#         leave.number_of_days = 21

    _inherit ="hr.contract"
    variable=fields.Float(string='Variable', required=True)
    working_from=fields.Float(string="workig hours from", required=True)
    working_to=fields.Float(string="workig hours to", required=True)

