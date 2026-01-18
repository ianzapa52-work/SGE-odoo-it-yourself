from odoo import models, fields, api
from odoo.exceptions import ValidationError

class IzlCita(models.Model):
    _name = 'izl_peluqueria.cita'
    _description = 'Citas de la peluquería'

    codigo = fields.Char(string='Código', readonly=True, copy=False)

    cliente_id = fields.Many2one('izl_peluqueria.cliente', string='Cliente', required=True)
    servicio_id = fields.Many2one('izl_peluqueria.servicio', string='Servicio', required=True)
    empleado_id = fields.Many2one('izl_peluqueria.empleado', string='Empleado', required=True)
    fecha = fields.Datetime(string='Fecha y hora', required=True)
    nota = fields.Text(string='Notas adicionales')

    @api.model
    def create(self, vals):
        if vals.get('codigo', 'Nuevo') == 'Nuevo':
            vals['codigo'] = self.env['ir.sequence'].next_by_code('izl_peluqueria.cita') or 'Nuevo'
        return super().create(vals)

    @api.constrains('fecha')
    def _check_fecha_futura(self):
        for cita in self:
            if cita.fecha and cita.fecha < fields.Datetime.now():
                raise ValidationError('No se pueden crear citas en el pasado.')
