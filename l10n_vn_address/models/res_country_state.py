# -*- coding: utf-8 -*-
# Copyright (C): khuongphampn@gmail.com

from odoo import models, api, fields

class CountryState(models.Model):
    _inherit = 'res.country.state'

    level_id = fields.Many2one('res.country.level', 'Level')
    active = fields.Boolean('Active', default=True)
    district_ids = fields.One2many('res.country.district', 'state_id', 'Districts', redonly=True)