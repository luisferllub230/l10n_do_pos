import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";

patch(PosStore.prototype, {
    getReceiptHeaderData(order) {
        let headerData = super.getReceiptHeaderData(...arguments);
        headerData.pos_ncf = order.pos_ncf;
        headerData.partner = order.get_partner();
        headerData.pos_latam_document_type_name = order.pos_latam_document_type_name;
        headerData.pos_date = order.date_order;
        headerData.pos_reference = order.pos_reference;
        return headerData;
    }
});
