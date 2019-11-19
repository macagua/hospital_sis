# -*- coding: utf-8 -*-

import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)


class TestLaboratorio(common.TransactionCase):

    def setUp(self):
        super(TestLaboratorio, self).setUp()
        # 'sis.laboratorios' instance model
        self.laboratorio = self.env['sis.laboratorios']

        # create an 'laboratorio' record
        self.laboratorio1 = self.laboratorio.create({
            'nombre': 'Hematología',
            'user_id': self.env.ref('base.user_admin').id,
            'hospital_id': self.env.ref('hospital_sis.hospital1').id,
        })

        self.laboratorio2 = self.laboratorio.create({
            'nombre': 'Ecocardiografía',
            'user_id': self.env.ref('base.user_root').id,
            'hospital_id': self.env.ref('hospital_sis.hospital1').id,
        })

    def test_laboratorios_creation(self):
        # This function test the 'sis.laboratorio' instances creation functionality

        # check 'nombre' of the 'laboratorio1'
        self.assertEqual(self.laboratorio1.nombre, 'Hematología')
        _logger.info("Created the {0}'s Laboratorio at {1}!".format(self.laboratorio1.nombre, self.env.ref('hospital_sis.hospital1').nombre))

        # check 'nombre' of the 'laboratorio2'
        self.assertEqual(self.laboratorio2.nombre, 'Ecocardiografía')
        _logger.info("Created the {0}'s Laboratorio at {1}!".format(self.laboratorio2.nombre, self.env.ref('hospital_sis.hospital1').nombre))

        # Do a little print to show it visually for this demo - in production you don't really need this.
        _logger.info("Your 'TestLaboratorio' test was successful!")
