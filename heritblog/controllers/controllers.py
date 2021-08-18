# -*- coding: utf-8 -*-
# from odoo import http


# class Heritblog(http.Controller):
#     @http.route('/heritblog/heritblog/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/heritblog/heritblog/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('heritblog.listing', {
#             'root': '/heritblog/heritblog',
#             'objects': http.request.env['heritblog.heritblog'].search([]),
#         })

#     @http.route('/heritblog/heritblog/objects/<model("heritblog.heritblog"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('heritblog.object', {
#             'object': obj
#         })
