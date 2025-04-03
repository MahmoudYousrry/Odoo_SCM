from odoo import models,fields

class ScmTrack(models.Model):
    _name = 'scm.track'

    name = fields.Char()
    is_open = fields.Boolean()
    capacity = fields.Integer()
    student_ids = fields.One2many("scm.student","track_id")
