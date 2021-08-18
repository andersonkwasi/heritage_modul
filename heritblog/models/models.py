# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HeritBlog(models.Model):
     _inherit = 'blog.post'

     description = fields.Html('Description')
     date_poste = fields.Date('Date poster')
         