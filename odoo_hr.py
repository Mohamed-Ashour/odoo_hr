import datetime

from time import strptime
#from datetime import datetime

import exceptions

from openerp import models,fields,api,exceptions
import math
from openerp import tools



class odooHrEmployeeInherit(models.Model):

    _inherit ="hr.employee"
    #upload file for  new employee
    #____________ attachment _____________
    data= fields.Binary('File')
    graduation_certificate = fields.Binary()
    #_______________  experience ____________
    experience_ids = fields.One2many("odoo_hr.exprience","employee_id",string="Experience")

    #_______________ Eduvation _________________
    degree_level = fields.Selection(selection=[('V','Vocational'),('TD','Technical Diploma'),('CD','Collage Diploma'),('BD','Bachelors Degree'),('MD','Master Degree'),('MBA','MBA'),('DD','Doctorate Degree')])
    @api.depends('degree_from','degree_to')
    def onchange_date_from_to(self,cr, uid, ids, degree_to, degree_from):
        # date_to has to be greater than date_from
        if (degree_from and degree_to) and (degree_from > degree_to):
            raise exceptions.ValidationError("The start date must be anterior to the end date. ")

    degree_from= fields.Date(string='From')
    degree_to= fields.Date(string='To')
    #-------------- test ---------------------

    university_name=fields.Char()
    fields_study=fields.Char()
    grade=fields.Selection(selection=[('A','A / Excellent / 85-100 %'),('B','B / Very good / 75-85 %'),('C','C / Good / 65-75 %'),('NS','Not Specified')])
    note=fields.Text()
    user_id=fields.Many2one("res.users")

    #----------------- security ---------------
    user_id=fields.Many2one("res.users")


class MyOdooexperiance(models.Model):

    _name = "odoo_hr.exprience"

    @api.model
    def create(self, values):
        print values['date_from']
        change_format_date_from = datetime.strptime(str(values['date_from']), '%Y-%m-%d')
        change_format_date_to = datetime.strptime(str(values['date_to']), '%Y-%m-%d')
        values['total_years_create']=(change_format_date_to - change_format_date_from).days/356
        return super(MyOdooexperiance,self).create(values)


    #@api.model
    @api.depends('date_from','date_to')
    def _comp_years(self):
        for rec in self:
            b_date = datetime.strptime(str(rec.date_from), '%Y-%m-%d')
            c_date = datetime.strptime(str(rec.date_to), '%Y-%m-%d')
            rec.total_years=((c_date - b_date).days/365)
            print "years : %d" % ((c_date - b_date).days/365)


    @api.depends('date_from','date_to')
    def onchange_date_from(self,cr, uid, ids, date_to, date_from):
        # date_to has to be greater than date_from
        if (date_from and date_to) and (date_from > date_to):
            raise exceptions.ValidationError("The start date must be anterior to the end date. ")

        result = {'value': {}}

        # No date_to set so far: automatically compute one 8 hours later
        if date_from and not date_to:
            date_to_with_delta = datetime.strptime(str(date_from), "%Y-%m-%d")
            result['value']['date_to'] = str(date_to_with_delta)

        # Compute and update the number of days
        if (date_to and date_from) and (date_from <= date_to):
            diff_day = self._get_number_of_days(date_from, date_to)
            result['value']['total_years_create'] = round(math.floor(diff_day))
        else:
            result['value']['total_years_create'] = 0

        return result

    @api.depends('date_from','date_to')
    def onchange_date_to(self, cr , uid , ids, date_to , date_from):
        """
        Update the number_of_days.
        """
        # date_to has to be greater than date_from
        if (date_from and date_to) and (date_from > date_to):
            raise exceptions.ValidationError(" The start date must be anterior to the end date. ")

        result = {'value': {}}

        # Compute and update the number of days
        if (date_to and date_from) and (date_from <= date_to):
            diff_day = self._get_number_of_days(date_from, date_to)
            result['value']['total_years_create'] = round(math.floor(diff_day))
        else:
            result['value']['total_years_create'] = 0
        return result

    @api.depends('date_from','date_to')
    def _get_number_of_days(self, date_from, date_to):

        DATETIME_FORMAT = "%Y-%m-%d"
        from_dt = datetime.strptime(str(date_from), DATETIME_FORMAT)
        to_dt = datetime.strptime(str(date_to), DATETIME_FORMAT)
        timedelta = to_dt - from_dt
        print timedelta
        diff_day = (timedelta.days)/365
        return diff_day

    #_______________ field in database ____________________

    job_title=fields.Char(string="Job Title")
    city=fields.Char(string="City")
    website=fields.Char(string="Website")
    date_from= fields.Date()
    date_to= fields.Date()
    total_years_create=fields.Integer(store=True)
    total_years=fields.Integer(compute=_comp_years,store=True)
    ecertificate=fields.Binary()
    employee_id=fields.Many2one("hr.employee")
    country= fields.Selection(selection=[('E','Egypt')])




    ########################Absence  ########################
class odooAbsence(models.Model):
    _inherit = "hr.payslip"
    absence= fields.Integer()
    unpaid_holiday=fields.Integer()
    @api.model
    def create(self, vals):
        vals['absence']=5
        ch_date=0
        ho_date=0
        unpaid=0

        DATETIME_FORMAT = "%Y-%m-%d"

        attendance_data=self.env["hr.attendance"].search([])
        listdate=[]
        holid_data=0

        count=0
        for rec in attendance_data:
            count=0
            att_date=rec.check_date
            if len(listdate) != 0:
                for x in listdate:
                    if x == att_date :
                        count+=1
                #print count
                if count == 0:
                    listdate.append(att_date)
            else:
                listdate.append(att_date)


        print listdate
        if listdate[0] >= vals['date_from']:
            print "Trueee"
        for lo in listdate:
            ch_date+=self.env["hr.attendance"].search_count([('employee_id','=',vals['employee_id']),('check_date','=',lo),('num_log','=',1)])
        holiday_date=self.env["hr.holidays"].search([('employee_id','=',vals['employee_id'])])
        for rec in holiday_date:
            for x in rec.holiday_status_id.ids:
                if x !=4 :
                    if rec.date_from >= vals['date_from'] and rec.date_from <= vals['date_to'] and (rec.state == "validate" or rec.state== "confirm" ) and rec.type== "remove":
                        holid_data+=rec.number_of_days_temp

        final_cal= 20-(holid_data+ch_date)
        if final_cal <0 :
            vals['absence']= -1 * final_cal
        else:
            vals['absence']=final_cal
    #########Unpaid Holiday######################

        for rec in holiday_date:
            #print "data6"
            #print rec.holiday_status_id.ids
            for x in rec.holiday_status_id.ids:
                #print x
                if x == 4:
                    if rec.date_from >= vals['date_from'] and rec.date_from <= vals['date_to']  and (rec.state =="validate" or rec.state=="confirm" )and rec.type== "remove":
                       unpaid+=rec.number_of_days_temp
                      # print "date5"
        vals['unpaid_holiday']=unpaid

        return super(odooAbsence,self).create(vals)
##########Add Date to attendence###########################################
class odooAddDateAttendence(models.Model):
    _inherit ="hr.attendance"
    check_date=fields.Date()
    num_log=fields.Integer()
    @api.model
    def create(self,vals):
        vals['check_date']= datetime.datetime.now()
        number_log=self.search_count([('employee_id','=',vals['employee_id']),('action','=','sign_in'),('check_date','=',vals['check_date'])])
        if number_log == 0 and vals['action'] == 'sign_in':
            vals['num_log']=1
        else:
            vals['num_log']=-1
        print vals['action']
        print number_log


        return super(odooAddDateAttendence,self).create(vals)
###Hierarchy########################################s
class odooHierarchyEmployees(models.Model):
    _inherit="hr.department"

    default_department_id = fields.Many2one('employee.department',
                                        string='My User',
                                        )


