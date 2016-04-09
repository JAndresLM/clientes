# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class Provincia(models.Model):
    _name = 'clientes.provincia'
    name = fields.Char(string="Provincia", required=True)
    canton_id = fields.One2many('clientes.canton', 'provincia_id')


class Canton(models.Model):
    _name = 'clientes.canton'
    name = fields.Char(string="Canton", required=True)
    provincia_id = fields.Many2one('clientes.provincia', ondelete='cascade',
                                   string="Provincia", required=True)
    distrito_id = fields.One2many('clientes.distrito', 'canton_id')


class Distrito(models.Model):
    _name = 'clientes.distrito'
    name = fields.Char(string="Distrito", required=True)
    canton_id = fields.Many2one('clientes.canton', ondelete='cascade',
                                string="Canton", required=True)
