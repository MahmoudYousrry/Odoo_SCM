from dataclasses import Field
from email.policy import default
from os import name
from odoo import models, fields, api
from odoo.exceptions import UserError

class ScmStudent(models.Model):
    _name = 'scm.student'
    _sql_constraints = [
        ("unique_Name","UNIQUE(name)","Name already exists")
    ]

    name = fields.Char(required=True)
    email = fields.Char()
    birth_date = fields.Date()
    salary = fields.Float()
    tax = fields.Float(compute="calc_tax")
    net_salary = fields.Float(compute="calc_tax",store=True)
    address = fields.Text()
    gender = fields.Selection(
        [('m','Male'),('f','Fmale')]
        )
    accepted = fields.Boolean()
    level = fields.Integer()
    image = fields.Binary()
    cv = fields.Html()
    loging_time = fields.Datetime()
    track_id = fields.Many2one("scm.track")
    track_capacity = fields.Integer(related='track_id.capacity')
    skills_ids = fields.Many2many("scm.skill")
    grade_ids = fields.One2many("scm_student.course.line","student_id")
    track_domain_ids = fields.Many2many('scm.track',compute='_compute_track_domain',string="Available Tracks")
    state =fields.Selection([
        ('applied','Applied'),
        ('first','First Interview'),
        ('second','Second Interview'),
        ('passed','Passed'),
        ('rejected','Rejected')
    ],default="applied")

    @api.depends("salary")
    def calc_tax(self):
        for record in self:
            if record.salary:
                record.tax = (20/100) * record.salary
                record.net_salary = record.salary - record.tax
            else:
                record.tax = 0
                record.net_salary = 0

    @api.constrains('track_id')
    def check_track_id(self):
        track_count = len(self.track_id.student_ids)
        track_capacity = self.track_id.capacity
        if track_count > track_capacity:
            raise UserError("Track is full")

    @api.model
    def create(self, vals):
        name_split = vals['name'].split()
        if len(name_split) > 1:
            vals['email'] = f"{name_split[0][0]}{name_split[1]}@gmail.com"
        else:
            vals['email'] = f"{name_split[0]}@gmail.com"
            
        search_student = self.search([('email','=',vals['email'])])
        if search_student:
            raise UserError('Email already exist')
        
        return super().create(vals)
    
    def write(self, vals):
        if name in vals:
            name_split = vals['name'].split()
            if len(name_split) > 1:
                vals['email'] = f"{name_split[0][0]}{name_split[1]}@gmail.com"
            else:
                vals['email'] = f"{name_split[0]}@gmail.com"
        return super().write(vals)  
        
    def unlink(self):
        for rec in self:
            if rec.state in ['passed','rejected']:
                raise UserError("You can't delete passed/rejected students")
        super().unlink()




    def change_state(self):
        if self.state == 'applied':
            self.state = 'first'
        elif self.state == 'first':
            self.state = 'second'
        elif self.state in ['passed','rejected']:
            self.state = 'applied'

    def set_passed(self):
        self.state = "passed"
    
    def set_rejected(self):
        self.state = "rejected"

    @api.depends('gender')
    def _compute_track_domain(self):
        for rec in self:
            if rec.gender == 'm':
                rec.track_domain_ids = self.env['scm.track'].search([('is_open', '=', True)])
            else:
                rec.track_domain_ids = self.env['scm.track'].search([])  
        
    @api.onchange("gender")
    def _on_change_gender(self):
        if not self.gender:
            self.gender = "m"
            return {}
        if self.gender == 'm':
            self.salary = 10000
        else:
            self.salary = 5000
        return{
            'warning' : {
                'title' : 'Hello',
                'message' : 'You have changed the gender'
            },
        }


class ScmCourse(models.Model):
    _name = "scm.course"

    name = fields.Char()


class StudentCourseGrades(models.Model):
    _name = "scm_student.course.line"

    student_id = fields.Many2one("scm.student")
    course_id = fields.Many2one("scm.course")
    grade = fields.Selection([
        ("g","Good"),
        ("vg","Very Good")
    ])





