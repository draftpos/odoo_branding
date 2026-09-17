# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    navbar_bg_color = fields.Char(
        string="Navbar Background Color",
        default="#1e293b",
        help="Background color or CSS gradient for the top navigation bar."
    )
    navbar_text_color = fields.Char(
        string="Navbar Text & Icon Color",
        default="#f8fafc",
        help="Color for navbar text, icons, and menus."
    )
    navbar_active_color = fields.Char(
        string="Navbar Active/Highlight Color",
        default="#38bdf8",
        help="Color for the active menu item and highlights."
    )
    navbar_hover_bg_color = fields.Char(
        string="Navbar Hover Background Color",
        default="#334155",
        help="Background color when hovering over navbar elements."
    )
    navbar_logo = fields.Binary(
        string="Custom Navbar Logo",
        help="Custom logo specifically optimized for the top navigation bar. If left empty, the standard company logo will be used."
    )
    navbar_logo_height = fields.Integer(
        string="Navbar Logo Height (px)",
        default=32,
        help="Target height in pixels for the navbar company logo (recommended 24-40px)."
    )
    navbar_show_company_name = fields.Boolean(
        string="Show Company Name in Navbar",
        default=False,
        help="Display company name in text next to the logo in the top navbar."
    )
    custom_brand_title = fields.Char(
        string="Custom Brand / System Title",
        help="Custom title displayed in the browser tab and navbar."
    )
