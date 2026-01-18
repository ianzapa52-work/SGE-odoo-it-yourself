from odoo import models, fields

class IzlEmpleado(models.Model):
    _name = 'izl_peluqueria.empleado'
    _description = 'Empleados de la peluquería'

    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo electrónico')
    especialidad = fields.Char(string='Especialidad')
