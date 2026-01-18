from odoo import models, fields

class IzlCliente(models.Model):
    _name = 'izl_peluqueria.cliente'
    _description = 'Clientes de la peluquería'

    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo electrónico')
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')
    image_1920 = fields.Image(string='Foto')

    cita_ids = fields.One2many('izl_peluqueria.cita', 'cliente_id', string='Citas')
    total_citas = fields.Integer(compute='_compute_total_citas')

    def _compute_total_citas(self):
        for cliente in self:
            cliente.total_citas = len(cliente.cita_ids)
