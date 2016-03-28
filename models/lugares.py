# -*- coding: utf-8 -*-
from openerp import models, fields, api
class Provincia(models.Model):
	_name = 'clientes.provincia'
	name = fields.Char(string="Provincia", required=True)  

class Canton(models.Model):
	_name = 'clientes.canton'
	name = fields.Char(string="Canton", required=True)
	id_provincia=fields.Many2one('clientes.provincia',ondelete='cascade', string="Provincia", required=True)
    

class Distrito(models.Model):
	_name = 'clientes.distrito'
	name = fields.Char(string="Distrito", required=True)
	id_canton=fields.Many2one('clientes.canton',ondelete='cascade', string="Canton", required=True)