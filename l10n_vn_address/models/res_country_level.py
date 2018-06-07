# -*- coding: utf-8 -*-

from odoo import models, api, fields

class ResCountrylevel(models.Model):
    _name = 'res.country.level'
    _description = 'Res Country Level'

    name = fields.Char('Name', size=256, required=True)
    active = fields.Boolean('Active', default=True)