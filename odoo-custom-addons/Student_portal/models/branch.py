from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
class Branch(models.Model):
    
    _name = 'branch_detail'
    _description ='branch'
    id=fields.Integer('branch_id',required=True)
    Name=fields.Char(string="Name",required=True)
