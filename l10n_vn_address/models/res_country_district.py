# -*- coding: utf-8 -*-
# Copyright (C): khuongphampn@gmail.com

from odoo import models, api, fields

class resCountryDistrict(models.Model):
    _name = 'res.country.district'
    _description = 'res Country District'

    code = fields.Char('Code', size=256, required=True)
    name = fields.Char('Name', size=256, required=True)
    state_id = fields.Many2one('res.country.state', 'State', required=True)
    level_id = fields.Many2one('res.country.level', 'Level', required=True)
    active = fields.Boolean('Active', default=True)
    ward_ids = fields.One2many('res.country.ward', 'district_id', 'Wards', readonly=1)