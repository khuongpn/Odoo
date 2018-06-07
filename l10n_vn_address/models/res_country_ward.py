# -*- coding: utf-8 -*-
# Copyright (C): khuongphampn@gmail.com

from odoo import models, api, fields

class ResCountryWard(models.Model):
    _name = 'res.country.ward'
    _description = 'Res Country Ward'

    code = fields.Char('Code', size=256, required=True)
    name = fields.Char('Name', size=256, required=True)
    district_id = fields.Many2one('res.country.district', 'District', required=True)
    level_id = fields.Many2one('res.country.level', 'Level', required=True)
    active = fields.Boolean('Active', default=True)