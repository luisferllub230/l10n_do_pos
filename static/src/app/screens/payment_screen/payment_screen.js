import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";

patch(PaymentScreen.prototype, {
    
    setup() {
        super.setup();
        this.printInvoice = this.currentOrder.is_to_invoice() || false;
    },
    
    toggleIsToInvoice() {
        this.currentOrder.set_to_invoice(!this.currentOrder.is_to_invoice());
        this.printInvoice = !this.printInvoice;
    },

    shouldDownloadInvoice() {
        return this.printInvoice;
    }
});