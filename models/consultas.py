# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields
from odoo.osv import osv

class Consultas(osv.osv):
    # the model name (in dot-notation, module namespace)
    _name = 'sis.consultas'
    # field to use for labeling records
    _rec_name = 'nombre'
    # the model's informal name
    _description = 'Hospital Searching'

    nombre = fields.Char(string="Nombre", size=80, requerid=True, help='Ingrese su nombre')
    partner_id = fields.Many2one(comodel_name="res.partner", string="Paciente", ondelete='restrict', required=False)
    especialidades = fields.Many2one(comodel_name="sis.especialidades", string="Especialidad", ondelete='restrict', required=False)

Consultas();
