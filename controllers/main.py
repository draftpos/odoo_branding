# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class OdooBrandingController(http.Controller):

    @http.route('/odoo_branding/theme.css', type='http', auth='public', methods=['GET'], cors="*")
    def branding_css(self, company_id=None, **kwargs):
        company = None
        if company_id:
            company = request.env['res.company'].sudo().browse(int(company_id))
        if not company or not company.exists():
            company = request.env.company
        
        bg_color = company.navbar_bg_color or '#1e293b'
        text_color = company.navbar_text_color or '#f8fafc'
        active_color = company.navbar_active_color or '#38bdf8'
        hover_bg_color = company.navbar_hover_bg_color or '#334155'
        logo_height = company.navbar_logo_height or 32

        css = f"""
        :root {{
            --odoo-branding-navbar-bg: {bg_color};
            --odoo-branding-navbar-text: {text_color};
            --odoo-branding-navbar-active: {active_color};
            --odoo-branding-navbar-hover-bg: {hover_bg_color};
            --odoo-branding-logo-height: {logo_height}px;
        }}
        header.o_navbar,
        header.o_navbar > nav.o_main_navbar {{
            background-color: var(--odoo-branding-navbar-bg) !important;
            background: var(--odoo-branding-navbar-bg) !important;
            color: var(--odoo-branding-navbar-text) !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
        }}
        header.o_navbar .o_menu_sections,
        header.o_navbar .o_navbar_breadcrumbs,
        header.o_navbar .o_menu_systray,
        header.o_navbar .o_menu_toggle {{
            background-color: transparent !important;
            background: transparent !important;
        }}
        header.o_navbar .o_menu_sections .dropdown-toggle,
        header.o_navbar .o_menu_sections a,
        header.o_navbar .o_menu_sections button,
        header.o_navbar .o_menu_systray button,
        header.o_navbar .o_menu_systray a,
        header.o_navbar .o_menu_systray i,
        header.o_navbar .o_menu_systray span {{
            color: var(--odoo-branding-navbar-text) !important;
            background-color: transparent !important;
        }}
        header.o_navbar .o_menu_sections .dropdown-toggle:hover,
        header.o_navbar .o_menu_sections a:hover,
        header.o_navbar .o_menu_systray button:hover,
        header.o_navbar .o_menu_systray a:hover {{
            background-color: var(--odoo-branding-navbar-hover-bg) !important;
            color: var(--odoo-branding-navbar-text) !important;
        }}
        .o_branding_navbar_logo {{
            max-height: var(--odoo-branding-logo-height) !important;
            width: auto;
            object-fit: contain;
        }}
        """
        return request.make_response(css, headers=[('Content-Type', 'text/css; charset=utf-8')])
