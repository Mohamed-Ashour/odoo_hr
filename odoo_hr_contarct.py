from openerp import models, fields, api

class odooContractInhired(models.Model):
    _inherit ="hr.contract"
    variable=fields.Float(string='Variable', required=True)
    working_from=fields.Float(string="workig hours from", required=True)
    working_to=fields.Float(string="workig hours to", required=True)
