# -*- coding: utf-8 -*-
from openerp import models, fields, api
class Cliente(models.Model):
	_name = 'clientes.cliente'
	name = fields.Char(string="Nombre Completo", required=True)
	empresa = fields.Char(string="Empresa")
	telefono = fields.Char(string="Teléfono")
	correo = fields.Char(string="Correo Electrónico")
	active = fields.Boolean(default=True, string="Activo")
	provincia=fields.Many2one('clientes.provincia',ondelete='cascade', string="Provincia")
	canton=fields.Many2one('clientes.canton',ondelete='cascade', string="Cantón")
	distrito=fields.Many2one('clientes.distrito',ondelete='cascade', string="Distrito")
	otrassenas = fields.Text(string="Otras Señas")

