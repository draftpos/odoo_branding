/** @odoo-module **/

import { NavBar } from "@web/webclient/navbar/navbar";
import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";
import { onMounted } from "@odoo/owl";

patch(NavBar.prototype, {
    setup() {
        super.setup(...arguments);
        onMounted(() => {
            this.applyBrandingStyles();
        });
    },

    get brandingConfig() {
        return session.odoo_branding || {};
    },

    get brandingLogoUrl() {
        const config = this.brandingConfig;
        if (config.has_navbar_logo && config.logo_url) {
            return config.logo_url;
        }
        if (session.company_id) {
            return `/web/image?model=res.company&id=${session.company_id}&field=logo`;
        }
        return "";
    },

    get brandingLogoHeight() {
        return this.brandingConfig.navbar_logo_height || 32;
    },

    get brandingCompanyName() {
        return this.brandingConfig.company_name || (session.user_companies?.current_company?.name) || "";
    },

    get brandingShowCompanyName() {
        return Boolean(this.brandingConfig.navbar_show_company_name);
    },

    onBrandingLogoClick() {
        if (this.env.isSmall) {
            if (this._openAppMenuSidebar) {
                this._openAppMenuSidebar();
            }
        } else if (this.hm && typeof this.hm.toggle === "function") {
            this.hm.toggle();
        } else {
            window.location.href = "/odoo";
        }
    },

    applyBrandingStyles() {
        const config = this.brandingConfig;
        if (!config || !config.navbar_bg_color) return;

        const root = document.documentElement;
        if (config.navbar_bg_color) {
            root.style.setProperty("--odoo-branding-navbar-bg", config.navbar_bg_color);
        }
        if (config.navbar_text_color) {
            root.style.setProperty("--odoo-branding-navbar-text", config.navbar_text_color);
        }
        if (config.navbar_active_color) {
            root.style.setProperty("--odoo-branding-navbar-active", config.navbar_active_color);
        }
        if (config.navbar_hover_bg_color) {
            root.style.setProperty("--odoo-branding-navbar-hover-bg", config.navbar_hover_bg_color);
        }
        if (config.navbar_logo_height) {
            root.style.setProperty("--odoo-branding-logo-height", `${config.navbar_logo_height}px`);
        }
        if (config.custom_brand_title && config.custom_brand_title.trim()) {
            document.title = config.custom_brand_title.trim();
        }
    }
});
