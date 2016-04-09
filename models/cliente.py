# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class Cliente(models.Model):

    _name = 'clientes.cliente'
    name = fields.Char(string="Nombre Completo", required=True)
    empresa = fields.Char(string="Empresa")
    telefono = fields.Char(string="Teléfono")
    correo = fields.Char(string="Correo Electrónico")
    active = fields.Boolean(default=True, string="Activo")
    provincia = fields.Many2one('clientes.provincia', ondelete='cascade',
                                string="Provincia")
    canton = fields.Many2one('clientes.canton', ondelete='cascade',
                             string="Cantón")
    distrito = fields.Many2one('clientes.distrito', ondelete='cascade',
                               string="Distrito")
    otrassenas = fields.Text(string="Otras Señas")

    @api.onchange('provincia')
    def _get_canton(self):
        self.canton = self.env['clientes.canton']
        vals = {}
        if self.provincia:
            vals['domain'] = {
                'canton': [('provincia_id', 'in', self.provincia._ids)]
            }
        return vals

    @api.onchange('canton')
    def _get_distrito(self):
        self.distrito = self.env['clientes.distrito']
        vals = {}
        if self.canton:
            vals['domain'] = {
                'distrito': [('canton_id', 'in', self.canton._ids)]
            }
        return vals
