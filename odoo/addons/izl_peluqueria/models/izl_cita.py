from odoo import models, fields

class IzlCita(models.Model):
    _name = 'izl_peluqueria.cita'
    _description = 'Citas de la peluquería'

    cliente_id = fields.Many2one('izl_peluqueria.cliente', string='Cliente', required=True)
    servicio_id = fields.Many2one('izl_peluqueria.servicio', string='Servicio', required=True)
    empleado_id = fields.Many2one('izl_peluqueria.empleado', string='Empleado', required=True)
    fecha = fields.Datetime(string='Fecha y hora', required=True)
    nota = fields.Text(string='Notas adicionales')
