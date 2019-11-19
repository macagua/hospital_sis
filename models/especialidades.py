# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields
from odoo.osv import osv


class Especialidades(osv.osv):
    # the model name (in dot-notation, module namespace)
    _name = 'sis.especialidades'
    # field to use for labeling records
    _rec_name = 'nombre'
    # the model's informal name
    _description = 'Hospital Specialties'
    # default order field for searching results
    _order = 'nombre'

    nombre = fields.Char(string="Nombre", size=80, required=True, help='Ingrese el nombre de la especialidad')


Especialidades();
