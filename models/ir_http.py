# -*- coding: utf-8 -*-
from odoo import models

class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super().session_info()
        company = self.env.company
        if company:
            has_logo = bool(company.navbar_logo or company.logo)
            logo_field = 'navbar_logo' if company.navbar_logo else 'logo'
            logo_url = f"/web/image?model=res.company&id={company.id}&field={logo_field}" if has_logo else ""
            
            result['odoo_branding'] = {
                'navbar_bg_color': company.navbar_bg_color or '#1e293b',
                'navbar_text_color': company.navbar_text_color or '#f8fafc',
                'navbar_active_color': company.navbar_active_color or '#38bdf8',
                'navbar_hover_bg_color': company.navbar_hover_bg_color or '#334155',
                'navbar_logo_height': company.navbar_logo_height or 32,
                'navbar_show_company_name': company.navbar_show_company_name or False,
                'custom_brand_title': company.custom_brand_title or '',
                'has_navbar_logo': has_logo,
                'logo_url': logo_url,
                'company_name': company.name or '',
            }
        return result
