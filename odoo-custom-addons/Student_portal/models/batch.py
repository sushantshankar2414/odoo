from odoo import api, fields, models
from datetime import date
from dateutil.relativedelta import relativedelta
class Batch(models.Model):
    
    _name = 'batch_detail'
    _description ='batch'
    id=fields.Integer('batch_id',required=True)
    Name=fields.Char(string="Name",required=True)
    branch=fields.Many2one("branch_detail" ,string="branch", required=True)
