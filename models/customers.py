# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api
import re


class Customer(models.Model):
    _name = 'customers.customer'
    name = fields.Char(string="Nombre Completo", required=True)
    company = fields.Many2one('customers.company', ondelete='cascade',string="Empresa")
    phone_ids = fields.One2many('customers.phone', 'customer_id', string="Teléfono")
    email = fields.Char(string="Correo Electrónico")
    active = fields.Boolean(default=True, string="Activo")
    province = fields.Many2one('customers.province', ondelete='cascade', string="Provincia")
    canton = fields.Many2one('customers.canton', ondelete='cascade', string="Cantón")
    district = fields.Many2one('customers.district', ondelete='cascade', string="Distrito")
    address = fields.Text(string="Otras Señas")

    @api.onchange('province')
    def _get_cantons(self):
        self.canton = self.env['customers.canton']
        vals = {}
        if self.province:
            vals['domain'] = {
                'canton': [('province_id', 'in', self.province._ids)]
            }
        return vals

    @api.onchange('canton')
    def _get_districts(self):
        self.district = self.env['customers.district']
        vals = {}
        if self.canton:
            vals['domain'] = {
                'district': [('canton_id', 'in', self.canton._ids)]
            }
        return vals

class Phone(models.Model):
    _name = 'customers.phone'
    name = fields.Char(string="Teléfono", required=True)
    customer_id = fields.Many2one('customers.customer', ondelete='cascade', string="Propietario")

class Company(models.Model):
    _name = 'customers.company'
    name = fields.Char(string="Empresa", required=True)


