from odoo import api, fields, models
from datetime import date
from dateutil.relativedelta import relativedelta
class Student(models.Model):
    
    _name = 'student_details'
    _description ='Student'
    id=fields.Integer('student_id',required=True)
    name=fields.Char(string="Name",required=True)
    roll_no=fields.Char(string='roll_no',required=True)
    batch=fields.Char(string="batch")
    Dob=fields.Date(string='date')
    year=fields.Selection([('first','first_year'),('second','second_year'),('third','third_year'),('fourth','fourth_year')],required=True,default='first')
    image=fields.Binary(string="image")
    age=fields.Integer(compute='_calculate_age')
    _sql_constraints=[("unique_roll_no","unique(roll_no)","this roll_no is already exist"),]
    
    @api.depends('Dob')
    def _calculate_age(self):
        for record in self:
            if record.Dob:
                d1=record.Dob
                d2=date.today()
                record.age=relativedelta(d2,d1).years
            else:
                record.age=0
                 

             
