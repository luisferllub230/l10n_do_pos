from odoo import models, fields, api, _

class PosConfig(models.Model):

    _inherit = 'pos.config'

    l10n_default_partner_id = fields.Many2one(
        'res.partner', 
        string=_('Default Customer'),
        help=_('Default Customer, this client will be used for final customers invoices'),
        default= lambda self: self.env.ref('l10n_do_pos.default_pos_partner', raise_if_not_found=False)
    )