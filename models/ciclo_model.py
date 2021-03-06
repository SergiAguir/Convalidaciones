# -*- coding: utf-8 -*-

from odoo import models, fields, api
class ciclo_model(models.Model):
    _name='convalidaciones.ciclo_model'
    _description = 'Modelo de ciclos'
    _sql_constraints = [ 
        ("ciclos_name_uniq","UNIQUE(name)","No puede haber 2 ciclos con el mismo nombre")
        ,]

    name =fields.Char(string="Código del Ciclo",size=10,required=True,index=True,help="Código del Ciclo")
    descripcion=fields.Html(string="Descripción",required=True,help="Descripción del Ciclo")
    modulos = fields.One2many("convalidaciones.modulo_model","ciclo",string="Módulos")


