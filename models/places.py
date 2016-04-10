# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class Province(models.Model):
    _name = 'customers.province'
    name = fields.Char(string="Provincia", required=True)
    cantons_ids = fields.One2many('customers.canton', 'province_id')


class Canton(models.Model):
    _name = 'customers.canton'
    name = fields.Char(string="Canton", required=True)
    province_id = fields.Many2one('customers.province', ondelete='cascade', string="Provincia", required=True)
    districts_ids = fields.One2many('customers.district', 'canton_id')


class District(models.Model):
    _name = 'customers.district'
    name = fields.Char(string="Distrito", required=True)
    canton_id = fields.Many2one('customers.canton', ondelete='cascade', string="Canton", required=True)
