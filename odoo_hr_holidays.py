from openerp import models, fields, api
from datetime import datetime
from dateutil import relativedelta

class odooHolidaysInhired(models.Model):

   _inherit ="hr.holidays"
   is_check = fields.Boolean()


   # @api.depends('is_check')
   #@api.model
   #def _checkDays(self):
    #    all = self.env['hr.contract'].search([("totalMonth","=",1)])
     #   for record in all:
            # record.is_check = True
      #      self.create({
       #         'employee_id': self.employee_id.id,
        #        'user_id': self.env.user.id,
         #       'name': 'zahra',
          #      'payslip_status': False,
           #     'holiday_type': 'category',
            #    'number_of_days_temp': 21,
             #   'state': 'validate',
              #  'number_of_days': 21,
               # 'type': 'add',
                #'holiday_status_id': 1,
            #})




    # @api.onchange('number_of_days')
    # def _compute_days (self):
        # # self.env['hr.contract'].search([])
        # print self.env['hr.contract'].totalMonth
        # if self.env['hr.contract'].totalMonth == 1:
        #     all = self.search(['holiday_status_id','=','1'])
        #     for a in all:
        # allDays = allDays + number_of_days
        # print allDays


    # number_of_days_temp = fields.float('Allocation', readonly=True, states={'draft':[('readonly',False)], 'confirm':[('readonly',False)]}, copy=False)
    # number_of_days = fields.float(compute=_compute_days , string='Number of Days', store=True)

    # @api.depends('hr_contract.totalMonth')
    # def _compute_days(self):
    #     for record in self:
    #         if self.env['hr.contract.totalMonth'] == 1:
    #             print "yeeeeeeeees"
    #             record.leaves_days = 21
    #             print record.leaves_days
    #         else:
    #             record.leaves_days = 0
    #             print record.leaves_days

        # test = self.env['hr.contract.totalMonth']
        # print test
        # for record in self:
        #     if self.env['hr.contract.totalMonth'] == 1:
        #         print "yeeeeeeeees"
        #         print "id self ===> "
        #         print self.employee_id.id
        #         print "self ===>"
        #         print self.env.user.id
        #
        #         record.employee_id = self.employee_id.id
        #         record.user_id = self.env.user.id
        #         record.name =  'zahra'
        #         record.payslip_status = False
        #         record.holiday_type= "category"
        #         record.number_of_days_temp = 21
        #         record.state = 'validate'
        #         record.number_of_days = 21
        #         record.type = 'add'
        #         record.holiday_status_id = 1
        #
        #
        #             # self.env.cr.commit()
        #         print "heeeeeeeeeeeeeeere"
        # return super(odooHolidaysInhired,self).create(values)

    # leaves_days=fields.float(compute=_compute_days)