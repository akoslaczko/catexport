from odoo import models, fields


class CatPartner(models.Model):
    _name = 'cat.partner'

    name = fields.Char(string='Name', required=True)
    company = fields.Char(string='Company', required=True)
    country = fields.Many2one('res.country', string='Country', required=True)
    orders = fields.Integer(string='Orders', required=True)
