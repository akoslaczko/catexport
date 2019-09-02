from odoo import models, fields

class PartnerPartner(models.Model):
    _name = 'partner.partner'

    name = fields.Char(string='Name', required=True)
    company = fields.Char(string='Company', required=True)
    country = fields.Many2one('res.country', string='Country', required=True)
    orders = fields.Integer(string='Orders', required=True)