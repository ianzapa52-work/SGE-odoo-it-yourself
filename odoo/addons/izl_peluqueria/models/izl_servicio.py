from odoo import models, fields

class IzlServicio(models.Model):
    _name = 'izl_peluqueria.servicio'
    _description = 'Servicios de la peluquería'

    nombre = fields.Char(string='Nombre del servicio', required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio')
