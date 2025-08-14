from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _load_pos_data_domain(self, data):
        """Add default_pos_partner id to domain"""

        if not data:
            return super(ResPartner, self)._load_pos_data_domain(data)

        result = super(ResPartner, self)._load_pos_data_domain(data)
        default_pos_partner = self.env.ref('l10n_do_pos.default_pos_partner', raise_if_not_found=False)

        if not default_pos_partner:
            return result

        return [('id', 'in', result[0][-1] + [default_pos_partner.id])]