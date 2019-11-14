# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class Laboratorios(models.Model):
    # the model name (in dot-notation, module namespace)
    _name = 'sis.laboratorios'
    # field to use for labeling records
    _rec_name = 'nombre'
    # the model's informal name
    _description = 'Hospital Laboratories'

    nombre = fields.Char(string="Nombre", required=True)
    user_id = fields.Many2one(comodel_name="res.users", string="Responsable", required=True)
    hospital_id = fields.Many2one(comodel_name="sis.hospital", string="Hospital", required=True)
