# -*- coding: utf-8 -*-
# from odoo import http


# class FirstModul(http.Controller):
#     @http.route('/first_modul/first_modul/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/first_modul/first_modul/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('first_modul.listing', {
#             'root': '/first_modul/first_modul',
#             'objects': http.request.env['first_modul.first_modul'].search([]),
#         })

#     @http.route('/first_modul/first_modul/objects/<model("first_modul.first_modul"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('first_modul.object', {
#             'object': obj
#         })
