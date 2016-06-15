# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import time

from openerp import models,fields,api,exceptions

class hr_holidays_summary_employee(models.Model):
    _inherit = 'hr.holidays.summary.employee'
    #_name = 'hr.holidays.summary.employee'

    date_from=fields.Date('From',required=True)
    emp=fields.Many2one('hr.employee' ,string="Employee")
    holiday_type=fields.Selection([('Approved','Approved'),('Confirmed','Confirmed'),('both','Both Approved and Confirmed')], 'Select Leave Type', required=True)

    _defaults = {
         'date_from': lambda *a: time.strftime('%Y-%m-01'),
         'holiday_type': 'Approved',
    }

    def print_report(self, cr, uid, ids, context=None):
        data = self.read(cr, uid, ids, context=context)[0]
        data['emp'] = context.get('active_ids',[])
        datas = {
             'ids': [],
             'model': 'hr.employee',
             'form': data
            }
        return self.pool['report'].get_action(cr, uid, data['emp'], 'hr_holidays.report_holidayssummary', data=datas, context=context)

