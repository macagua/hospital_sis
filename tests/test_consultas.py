# -*- coding: utf-8 -*-

import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)


class TestConsulta(common.TransactionCase):

    def setUp(self):
        super(TestConsulta, self).setUp()
        # 'sis.consultas' instance model
        self.consulta = self.env['sis.consultas']

        # create an 'consulta' record
        self.consulta1 = self.consulta.create({
            'nombre': 'Hematología',
            'partner_id': self.env.ref('base.res_partner_1').id,
            'especialidades': self.env.ref('hospital_sis.especialidades2').id,
        })

        self.consulta2 = self.consulta.create({
            'nombre': 'Ecocardiografía',
            'partner_id': self.env.ref('base.res_partner_1').id,
            'especialidades': self.env.ref('hospital_sis.especialidades3').id,
        })

    def test_consultas_creation(self):
        # This function test the 'sis.consulta' instances creation functionality

        # check 'nombre' of the 'consulta1'
        self.assertEqual(self.consulta1.nombre, 'Hematología')
        _logger.info("Created the {0}'s Consulta at {1}!".format(self.consulta1.nombre, self.env.ref('hospital_sis.hospital1').nombre))

        # check 'nombre' of the 'consulta2'
        self.assertEqual(self.consulta2.nombre, 'Ecocardiografía')
        _logger.info("Created the {0}'s Consulta at {1}!".format(self.consulta2.nombre, self.env.ref('hospital_sis.hospital1').nombre))

        # Do a little print to show it visually for this demo - in production you don't really need this.
        _logger.info("Your 'TestConsulta' test was successful!")
