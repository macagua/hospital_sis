[![Python 3.7](https://img.shields.io/badge/Python-3.7-blue)](https://www.python.org/downloads/release/python-375/)
[![LGPL-3.0](https://img.shields.io/github/license/macagua/hospital_sis.svg)](https://github.com/macagua/hospital_sis/blob/master/LICENSE)
[![Tech Doc](http://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.youtube.com/watch?v=ibwZs-dL5H8)
[![Help](http://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)

Sistema de Información Hospitalario SIS-1
-----------------------------------------

Sistema de Información Hospitalario SIS-1, is an Odoo 13 module to ease the 
management of hospitals, you can manage registration of patients and her 
medical appointments, etc.

This Odoo module let you manage:

- manage hospitals.

- manage specialties.

- manage medical appointments.

- manage patients using 'res_company' model overriding with new fields added.


Dependencies
------------

This module requires the following dependencies:

- odoo 13 > https://github.com/odoo/odoo


Install
-------

Download the source code:

```
$ git clone https://github.com/macagua/hospital_sis.git
```

Move ``hospital_sis`` folder into ``extra-addons`` Odoo directory:

```
$ mv hospital_sis /full/path/to/extra-addons/
```

Restart the Odoo instance server, login and got to **Apps** > **Sistema de Información Hospitalario SIS-1** > **Install**

![Install 'Sistema de Información Hospitalario SIS-1' Module](https://raw.githubusercontent.com/macagua/hospital_sis/master/static/description/install_module.png "Install 'Sistema de Información Hospitalario SIS-1' Module")

Then go to Main menu at left top corner and click to **Hospital**.

![Access 'Hospital' Menu](https://raw.githubusercontent.com/macagua/hospital_sis/master/static/description/manage_hospital.png "Access 'Hospital' Menu")


References
----------

- [Curso de programación en Odoo: Clase 05 Crear un Sistema Hospitalario - Chile - Youtube](https://www.youtube.com/watch?v=ibwZs-dL5H8).
