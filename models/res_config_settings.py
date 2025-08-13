from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    l10n_latam_use_documents = fields.Boolean(
        related='pos_invoice_journal_id.l10n_latam_use_documents'
    )

    pos_partner_id = fields.Many2one(
        comodel_name='res.partner',
        related='pos_config_id.pos_partner_id', 
        readonly=False,
        default=lambda self: self.env.ref('l10n_do_pos.default_pos_partner', raise_if_not_found=False),
    )
    