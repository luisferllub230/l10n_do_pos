from odoo import api, fields, models, _

class PosPaymentMethod(models.Model):
    _inherit = 'pos.payment.method'

    
    is_credit_note = fields.Boolean(
        string='Credit Note',
    )