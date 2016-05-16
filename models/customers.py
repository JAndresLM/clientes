# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api
import re


class Customer(models.Model):
    _name = 'customers.customer'
    name = fields.Char(string="Nombre Completo", required=True)
    company = fields.Many2one('customers.company', ondelete='cascade',string="Empresa")
    phone_ids = fields.One2many('customers.phone', 'customer_id', string="Teléfono")
    email_ids = fields.One2many('customers.email', 'customer_id', string="Correo Electrónico")
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
    customer_id = fields.Many2one('customers.customer', ondelete='cascade', string="Propietario", required=True)

    @api.multi
    def _validate_phone(self):
        for x in self:
            if re.match("^[0-9]{4}-[0-9]{4}$", self.name) == None:
                return False
        return True

    _constraints = [
        (_validate_phone, '\n\nPor favor ingrese un teléfono válido. \nFormato correcto: 9999-9999', ['name']),
    ]

class Email(models.Model):
    _name = 'customers.email'
    name = fields.Char(string="Correo Electrónico", required=True)
    customer_id = fields.Many2one('customers.customer', ondelete='cascade', string="Propietario", required=True)

    @api.multi
    def _validate_email(self):
        for x in self:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.name) == None:
                return False
        return True

    _constraints = [
        (_validate_email, '\n \n Por favor ingrese un correo válido. \nFormato correcto: usuario@dominio.com', ['name']),
    ]

class Company(models.Model):
    _name = 'customers.company'
    name = fields.Char(string="Empresa", required=True)

class Laboratory(models.Model):
    _inherit = 'res.company'
    university = fields.Char("Universidad")
    school=fields.Char("Escuela")
    campus=fields.Char("Sede")
    coordinator=fields.Char("Coordinador del laboratorio")
    title=fields.Char("Descripción del coordinador")


