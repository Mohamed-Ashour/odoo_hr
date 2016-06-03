

from openerp import models,fields,api

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

    # @api.onchange('employee_id')
    # def _onchange_nameEmployee(self):
    #      return {
    #         'warning': {
    #             'title': "Something bad happened",
    #             'message': "It was very bad indeed",
    #         }
    #     }

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
    university_name=fields.Char()
    fields_study=fields.Char()
    grade=fields.Selection(selection=[('A','A / Excellent / 85-100 %'),('B','B / Very good / 75-85 %'),('C','C / Good / 65-75 %'),('NS','Not Specified')])
    note=fields.Text()


class MyOdooexperiance(models.Model):

    _name = "odoo_hr.exprience"
    job_title=fields.Char(string="Job Title")
    city=fields.Char(string="City")
    website=fields.Char(string="Website")
    date_from= fields.Date(string='From')
    date_to= fields.Date(string='To')
    total_years=fields.Integer()
    ecertificate=fields.Binary()
    employee_id=fields.Many2one("hr.employee")
    #country_i=fields.Char(related="employee_id.country_id")


