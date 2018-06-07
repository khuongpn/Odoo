# -*- coding: utf-8 -*-
# Copyright (C): khuongphampn@gmail.com

from odoo import models, api, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    res_district_id = fields.Many2one('res.country.district', 'District', ondelete='restrict')
    res_ward_id = fields.Many2one('res.country.ward', 'Ward', ondelete='restrict')
    country_id = fields.Many2one('res.country',
                                 string='Country',
                                 default=lambda self: self.env.ref('base.vn'),
                                 ondelete='restrict')

    @api.multi
    def _display_address(self, without_company=False):

        '''
        The purpose of this function is to build and return an address formatted accordingly to the
        standards of the country where it belongs.

        :param address: browse record of the res.partner to format
        :returns: the address formatted in a display that fit its country habits (or the default ones
            if not country is specified)
        :rtype: string
        '''
        # get the information that will be injected into the display format
        # get the address format
        # address_format = self.country_id.address_format or \
        #                  "%(street)s\n%(street2)s\n%(city)s %(state_code)s %(zip)s\n%(country_name)s"
        args = {
            'state_code': self.state_id.code or '',
            'state_name': self.state_id.name or '',
            'district_code': self.res_district_id.code or '',
            'district_name': self.res_district_id.name or '',
            'ward_code': self.res_ward_id.code or '',
            'ward_name': self.res_ward_id.name or '',
            'country_code': self.country_id.code or '',
            'country_name': self.country_id.name or '',
            'company_name': self.commercial_company_name or '',
        }
        for field in self._address_fields():
            args[field] = getattr(self, field) or ''
        if args.get('ward_name', '') == '':
            address_format = '%(street)s, %(district_name)s, %(state_name)s'
        else:
            address_format = '%(street)s, %(ward_name)s, %(district_name)s, %(state_name)s'
        if without_company:
            args['company_name'] = ''
        elif self.commercial_company_name:
            address_format = '%(company_name)s\n' + address_format
        return address_format % args
