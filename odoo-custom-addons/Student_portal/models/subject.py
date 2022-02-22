from odoo import api, fields, models
from datetime import date
from dateutil.relativedelta import relativedelta
class Subject(models.Model):
    
    _name = 'subject_details'
    _description ='subject'
    id=fields.Integer('subject_id',required=True)
    Name=fields.Char(string="Name",required=True)
    branch=fields.Many2one("branch_detail", string="branch", required=True)
    teacher_id=fields.Many2one("teacher_details", string="teacher" , required=True)
