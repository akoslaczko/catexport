# -*- coding: utf-8 -*-
from odoo import http

# class Catexport(http.Controller):
#     @http.route('/catexport/catexport/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/catexport/catexport/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('catexport.listing', {
#             'root': '/catexport/catexport',
#             'objects': http.request.env['catexport.catexport'].search([]),
#         })

#     @http.route('/catexport/catexport/objects/<model("catexport.catexport"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('catexport.object', {
#             'object': obj
#         })