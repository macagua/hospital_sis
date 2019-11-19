# -*- coding: utf-8 -*-

import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)


class TestEspecialidades(common.TransactionCase):

    def setUp(self):
        super(TestEspecialidades, self).setUp()
        # 'sis.especialidades' instance model
        self.especialidad = self.env['sis.especialidades']

        # create an 'especialidad' record
        self.especialidad1 = self.especialidad.create({
            'nombre': 'Angiología',
        })

        self.especialidad2 = self.especialidad.create({
            'nombre': 'Cardiología',
        })

    def test_especialidads_creation(self):
        # This function test the 'sis.especialidades' instances creation functionality

        # check 'nombre' of the 'especialidad1'
        self.assertEqual(self.especialidad1.nombre, 'Angiología')
        _logger.info("Created the {0}'s Especialidad!".format(self.especialidad1.nombre))

        # check 'nombre' of the 'especialidad2'
        self.assertEqual(self.especialidad2.nombre, 'Cardiología')
        _logger.info("Created the {0}'s Especialidad!".format(self.especialidad2.nombre))

        # Do a little print to show it visually for this demo - in production you don't really need this.
        _logger.info("Your 'TestEspecialidades' test was successful!")
