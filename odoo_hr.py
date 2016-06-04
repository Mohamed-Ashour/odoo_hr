import datetime

from time import strptime
from datetime import datetime

from openerp import models,fields,api

from dateutil import relativedelta

class odooHrInhired(models.Model):

    _inherit ="hr.attendance"
    image=fields.Binary()

    #@api.onchange('employee_id','image')
    @api.model
    def create(self, values):
        contacts1 = self.env['hr.employee'].search([('id','=',values['employee_id'])])
        values['image']=contacts1.image
        return super(odooHrInhired,self).create(values)

    @api.multi
    def write(self, values):
        contacts1 = self.env['hr.employee'].search([('id','=',values['employee_id'])])
        values['image']=contacts1.image
        return super(odooHrInhired,self).write(values)


#______________________________________________________________________________


class odooHrEmployeeInherit(models.Model):

    _inherit ="hr.employee"
    #upload file for  new employee
    #____________ attachment _____________
    data= fields.Binary('File')
    graduation_certificate=fields.Binary()
    #_______________  experience ____________
    experience_ids=fields.One2many("odoo_hr.exprience","employee_id",string="Experience")

    #_______________ Eduvation _________________
    degree_level=fields.Selection(selection=[('V','Vocational'),('TD','Technical Diploma'),('CD','Collage Diploma'),('BD','Bachelors Degree'),('MD','Master Degree'),('MBA','MBA'),('DD','Doctorate Degree')])
    degree_from= fields.Date(string='From')
    degree_to= fields.Date(string='To')
    #-------------- test ---------------------

    university_name=fields.Char()
    fields_study=fields.Char()
    grade=fields.Selection(selection=[('A','A / Excellent / 85-100 %'),('B','B / Very good / 75-85 %'),('C','C / Good / 65-75 %'),('NS','Not Specified')])
    note=fields.Text()


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


    job_title=fields.Char(string="Job Title")
    city=fields.Char(string="City")
    website=fields.Char(string="Website")
    date_from= fields.Date()
    date_to= fields.Date()
    total_years_create=fields.Integer()
    total_years=fields.Integer(compute=_comp_years,store=True)
    ecertificate=fields.Binary()
    employee_id=fields.Many2one("hr.employee")
    country= fields.Selection(selection=[('E','Egypt')])
