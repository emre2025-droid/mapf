# Copyright (C) 2022 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model
    def get_default_leaflet_position(self, model_name):
        current_partner = self.env.user.partner_id
        return {
            "lat": current_partner.lat,
            "lng": current_partner.lng,
        }
