import logging

from odoo import api, fields, models, tools, _, Command
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class PosOrder(models.Model):
    _inherit = 'pos.order'

    pos_ncf = fields.Char(
        string=_("NCF"),
        related='account_move.l10n_do_fiscal_number',
    )

    pos_latam_document_type_id = fields.Many2one(
        'l10n_latam.document.type',
        string=_('Document Type'),
        related='account_move.l10n_latam_document_type_id',
    )

    pos_latam_document_type_name = fields.Char(
        string=_("Document Type Name"),
        compute='_compute_pos_latam_document_type_name',
        store=True
    )

    pos_do_income_type = fields.Selection(
        string=_("Income Type"),
        related='account_move.l10n_do_income_type',
    )


    @api.depends('pos_latam_document_type_id')
    def _compute_pos_latam_document_type_name(self):
        for order in self:
            if order.pos_latam_document_type_id:
                order.pos_latam_document_type_name = order.pos_latam_document_type_id.name
    
    def _create_invoice(self, move_vals):
        """Create the invoice and force to create the fiscal sequence for the invoice"""

        invoice = super()._create_invoice(move_vals)

        if not invoice:
            return invoice
        
        for move in invoice.filtered(
            lambda x: x.country_code == "DO"
            and x.l10n_latam_document_type_id
            and not x.l10n_latam_manual_document_number
            and not x.l10n_do_enable_first_sequence
            and x.state == "draft"
            and not x.l10n_do_fiscal_number
        ):
            move.with_context(is_l10n_do_seq=True)._set_next_sequence()
        
        return invoice
    