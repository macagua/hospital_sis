# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields
from odoo.osv import osv
# from odoo.tools.translate import _

class res_partner(osv.osv):
    # the model name (in dot-notation, module namespace)
    _name = 'res.partner'
    # python-inherited models
    _inherit = 'res.partner'

    rut = fields.Char(string="Rut", required=False, size=10, help='Ingrese el RUT')
    edad = fields.Integer(string="Edad", required=False, size=3, help='Ingrese la edad')
    profesion = fields.Char(string="Profesión", required=False, size=10, help='Ingrese la profesión')

res_partner();
