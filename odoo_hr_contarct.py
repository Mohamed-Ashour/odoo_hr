from openerp import models,fields,api

class odooContractInhired(models.Model):
    _inherit ="hr.contract"
    net=fields.Float(string='Net', required=True)
