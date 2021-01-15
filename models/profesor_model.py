# -*- coding: utf-8 -*-
import random
from datetime import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class profesor_model(models.Model):
    _name='convalidaciones.profesor_model'
    _description = 'Modelo de Profesores'


    name =fields.Char(string="Nombre",required=True,index=True,help="Nombre")
    apellidos =fields.Char(string="Apellidos",required=True,index=True,help="Apellidos")
    foto=fields.Binary()
    dni=fields.Char(string="DNI",required=True,size=9,help="DNI")
    alumnos = fields.Many2many("convalidaciones.alumno_model",relation="alumnos2profes_rel" ,string="Alumnos")
    numAlumnos = fields.Integer(string="Numero de Alumnos", compute="_calcAlumnos", storage=True)

    @api.depends("alumnos")
    def _calcAlumnos(self):
        self.numAlumnos = len(self.alumnos)

    @api.constrains("dni")
    def _check_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra=self.dni[:-1]
        num = int(self.dni[:-1])
        if letras[num%23]!=letra:
            raise ValidationError("DNI invalido")
        