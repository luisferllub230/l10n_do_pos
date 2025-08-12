odoo.define('l10n_do_pos.OrderReceipt', function (require) {
    'use strict';

    const OrderReceipt = require('point_of_sale.OrderReceipt');
    const Registries = require('point_of_sale.Registries');

    const L10nDoPosOrderReceipt = OrderReceipt => class extends OrderReceipt {
        isSimple(line) {
            
            if (this.env.pos.config.l10n_latam_use_documents){
                return false;
            }

            return super.isSimple(line);
        }
    }
    
    Registries.Component.extend(OrderReceipt, L10nDoPosOrderReceipt);

});
