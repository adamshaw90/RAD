document.addEventListener("DOMContentLoaded", function () {
    function updateCartTotal() {
        fetch("/shop/cart/total/")
            .then(response => response.json())
            .then(data => {
                let cartTotalElement = document.getElementById("cart-total");
                if (cartTotalElement) {
                    cartTotalElement.textContent = `£${data.cart_total || "0.00"}`;
                }
            })
            .catch(error => console.error("Error updating cart total:", error));
    }

    updateCartTotal();
});


document.addEventListener("DOMContentLoaded", function() {
    let toastEl = document.querySelector('.toast');
    if (toastEl) {
        let toast = new bootstrap.Toast(toastEl);
        toast.show();
    }
});