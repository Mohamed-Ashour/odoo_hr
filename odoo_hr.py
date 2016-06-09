import datetime

from time import strptime
#from datetime import datetime

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
    Personal_card_front=fields.Binary()
    Personal_card_back=fields.Binary()
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
    ########################to copy imployee data in another #####
class OdooDisplayId(models.Model):
        _name = "odoo_hr.display"

        #@api.model
        # def create(self,values):
        #     print "done enter "
        #     result=self.env["hr.employee"].search([])
        #     print result[1]['id']
        #     for x in result:
        #         values["display_data"]=x['id']
        #         print values["display_data"]
        #         super(OdooDisplayId,self).create(values)
        #     pass

        def _dis_data(self):
            Employee_ids=self.env['hr.employee'].search([])
            print Employee_ids[1]['id']
           # print "ffff"
            #print Date.today()+8
            #for x in Employee_ids:
             #  x['display_data']=x['id']
            #pass
            format = "%a %b %d %H:%M:%S %Y"

            today = datetime.datetime.today()
            print 'ISO     :', today

            s = today.strptime(format)
            print 'strftime:', s
            m= s.days
            print s

            d = datetime.datetime.strptime(s, format)
            print 'strptime:', d.strptime(format)


           #Employee_ids=[1,2,3,4,5]
           # Employee_ids=self.env['hr.employee'].search([])
           #  print "enteeeeeeeeeeeeer"
           #  for x in [1,2,3,4]:
           #      for rec in self:
           #      #self.create({'display_data': x.id})
           #       print x
           #       rec.display_data=x

        display_data=fields.Integer(compute= _dis_data)
