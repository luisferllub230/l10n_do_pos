from odoo import models, fields, api, _


class PosOrder(models.Model):
    _inherit = 'pos.order'

    l10n_default_partner_id = fields.Many2one(
        'res.partner', 
        string=_('Default Customer'),
        help=_('Default Customer, this client will be used for final customers invoices'),
        related='config_id.l10n_default_partner_id',
        readonly=True
    )