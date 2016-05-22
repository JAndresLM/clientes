# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class Province(models.Model):
    _name = 'customers.province'
    name = fields.Char(string="Provincia", required=True)
    canton_id = fields.One2many('customers.canton', 'province_id')

    _sql_constraints = [
        ('name_unique',
            'UNIQUE(name)',
            "No se admiten nombres repetidos en provincias"),
    ]

class Canton(models.Model):
    _name = 'customers.canton'
    name = fields.Char(string="Cantón", required=True)
    province_id = fields.Many2one('customers.province', ondelete='cascade', string="Provincia", required=True)
    district_id = fields.One2many('customers.district', 'canton_id')

    _sql_constraints = [
        ('name_unique',
            'UNIQUE(name)',
            "No se admiten nombres repetidos en cantones"),
    ]

class District(models.Model):
    _name = 'customers.district'
    name = fields.Char(string="Distrito", required=True)
    canton_id = fields.Many2one('customers.canton', ondelete='cascade', string="Canton", required=True)
