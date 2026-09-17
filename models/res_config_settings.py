# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    navbar_bg_color = fields.Char(
        related='company_id.navbar_bg_color',
        readonly=False,
        string="Navbar Background Color"
    )
    navbar_text_color = fields.Char(
        related='company_id.navbar_text_color',
        readonly=False,
        string="Navbar Text & Icon Color"
    )
    navbar_active_color = fields.Char(
        related='company_id.navbar_active_color',
        readonly=False,
        string="Navbar Active/Highlight Color"
    )
    navbar_hover_bg_color = fields.Char(
        related='company_id.navbar_hover_bg_color',
        readonly=False,
        string="Navbar Hover Background Color"
    )
    navbar_logo = fields.Binary(
        related='company_id.navbar_logo',
        readonly=False,
        string="Custom Navbar Logo"
    )
    navbar_logo_height = fields.Integer(
        related='company_id.navbar_logo_height',
        readonly=False,
        string="Navbar Logo Height (px)"
    )
    navbar_show_company_name = fields.Boolean(
        related='company_id.navbar_show_company_name',
        readonly=False,
        string="Show Company Name in Navbar"
    )
    custom_brand_title = fields.Char(
        related='company_id.custom_brand_title',
        readonly=False,
        string="Custom Brand / System Title"
    )
