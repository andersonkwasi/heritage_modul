# -*- coding: utf-8 -*-

from odoo import models, fields, api


class first_modul(models.Model):
     _name = 'first_modul.first_modul' #nom du model
     
     nom = fields.Char('Nom')
     prenoms = fields.Char('Prenoms')
     genre = fields.Selection([('m','Masculin'),('f','Feminin')])
     piece_Identite = fields.Char('N°Pièce d\'Identité')
     telephone = fields.Char('Numero de Téléphone')
     date_Naissance = fields.Date("Date de Naissance")
     email = fields.Char()
     niveau = fields.Selection([('1','BEPC'),('2','BAC'),('3','LICENCE')], string="Niveau d'Etude")
     date_inscription = fields.Datetime('Date d\'inscription', default=fields.Datetime.now())
     question = fields.Boolean(string="Avez-vous un Ordinateur ?")
     fichier = fields.Binary(string="Charger votre CV ici", help="veillez télécharger ici votre CV")
     competence = fields.Selection([('1','OUi'),('2','Non')],string="Avez-vous des Competences ?", default="1")
     domaine_competence = fields.Selection([('1','Commerce'),('2','Marketing'),('3','Comptabilité')], string="Domaine de competence")
     
