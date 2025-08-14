from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    l10n_default_partner_id = fields.Many2one(
        'res.partner',
        related='pos_config_id.l10n_default_partner_id', 
        readonly=False,
    )