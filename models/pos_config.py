from odoo import models, fields, _, api
from odoo.exceptions import ValidationError


class PosConfig(models.Model):
    _inherit = 'pos.config'

    pos_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Default partner',
        default=lambda self: self.env.ref('l10n_do_pos.default_pos_partner', raise_if_not_found=False),
    )

    # l10n_latam_use_documents = fields.Boolean(
    #     string='Fiscal POS',
    #     related='invoice_journal_id.l10n_latam_use_documents',
    # )