from odoo import api, fields, models
from datetime import date
from dateutil.relativedelta import relativedelta
class Teacher(models.Model):
    
    
    _name = 'teacher_details'
    _description ='teacher'
    id=fields.Integer('teacher_id',required=True)
    Name=fields.Char(string="Name",required=True)
    subject_list=fields.One2many("subject_details","teacher_id",string="subjects")
    e_id=fields.Char(required=True)
    _sql_constraints=[("unique_e_id","unique(e_id)","this employee id is already exist"),]
    
