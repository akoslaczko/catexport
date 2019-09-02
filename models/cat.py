from odoo import models, fields


class CatCat(models.Model):
    _name = 'cat.cat'

    breed = fields.Char(string='Breed', required=True)
    stock = fields.Integer(string='Stock', required=True)
