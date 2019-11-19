# -*- coding: utf-8 -*-

import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)


class TestHospital(common.TransactionCase):

    def setUp(self):
        super(TestHospital, self).setUp()
        # 'sis.hospital' instance model
        self.hospital = self.env['sis.hospital']

        # create an 'hospital' record
        self.hospital1 = self.hospital.create({
            'nombre': 'Sor Juana Ines de la Cruz',
            'country_id': self.env.ref('base.cl').id,
        })

        self.hospital2 = self.hospital.create({
            'nombre': 'Hospital Universitario de Los Andes',
            'country_id': self.env.ref('base.cl').id,
        })

    def test_hospitals_creation(self):
        # This function test the 'sis.hospital' instances creation functionality

        # check 'nombre' of the 'hospital1'
        self.assertEqual(self.hospital1.nombre, 'Sor Juana Ines de la Cruz')
        _logger.info("Created the {0}'s Hospital!".format(self.hospital1.nombre))

        # check 'nombre' of the 'hospital2'
        self.assertEqual(self.hospital2.nombre, 'Hospital Universitario de Los Andes')
        _logger.info("Created the {0}'s Hospital!".format(self.hospital2.nombre))

        # Do a little print to show it visually for this demo - in production you don't really need this.
        _logger.info("Your 'TestHospital' test was successful!")