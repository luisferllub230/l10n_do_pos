import { PosOrder } from "@point_of_sale/app/models/pos_order";
import { patch } from "@web/core/utils/patch";

patch(PosOrder.prototype, {

    setup(order) {
        super.setup(...arguments);
        this.to_invoice = true;
        
        console.log(this.get_partner());
        if (!this.get_partner()) {
            const l10n_do_deafult_partner = this.config.l10n_default_partner_id;
            if (l10n_do_deafult_partner && !this.finalized) {
                this.set_partner(l10n_do_deafult_partner);
            }
        }
    }
})