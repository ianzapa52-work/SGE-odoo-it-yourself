from odoo import models, fields, api

class IzlEmpleado(models.Model):
    _name = 'izl_peluqueria.empleado'
    _description = 'Empleados de la peluquería'

    name = fields.Char(string='Nombre completo', required=True)

    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo electrónico')
    especialidad = fields.Char(string='Especialidad')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') and vals.get('nombre') and vals.get('apellido'):
                vals['name'] = f"{vals['nombre']} {vals['apellido']}"
        return super().create(vals_list)
