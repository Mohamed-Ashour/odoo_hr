from openerp import models,fields,api

class odooContractInhired(models.Model):
    _inherit ="hr.contract"
    variable=fields.Float(string='Variable', required=True)
