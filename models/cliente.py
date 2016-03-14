# -*- coding: utf-8 -*-
from openerp import models, fields, api
class Cliente(models.Model):
	_name = 'clientes.cliente'
	name = fields.Char(string="Nombre Completo", required=True)
	empresa = fields.Char(string="Empresa")
	telefono = fields.Char(string="Teléfono")
	correo = fields.Char(string="Correo Electrónico")
	active = fields.Boolean(default=True)
	provincia = fields.Selection([('A', "Alajuela"),('H', "Heredia"),('C', "Cartago"),('SJ', "San Jose"),('P', "Puntarenas"),('G', "Guanacaste"),('L', "Limon"),])
	canton = fields.Char(string="Cantón")
	distrito = fields.Char(string="Distrito")
	otrassenas = fields.Text(string="Otras Señas")
	