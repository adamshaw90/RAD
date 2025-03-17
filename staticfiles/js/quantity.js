document.addEventListener("DOMContentLoaded", function () {
    const decreaseBtn = document.getElementById("decreaseQuantity");
    const increaseBtn = document.getElementById("increaseQuantity");
    const quantityInput = document.getElementById("quantity");

    decreaseBtn.addEventListener("click", function () {
        let currentValue = parseInt(quantityInput.value);
        if (currentValue > 1) {
            quantityInput.value = currentValue - 1;
        }
    });

    increaseBtn.addEventListener("click", function () {
        let currentValue = parseInt(quantityInput.value);
        quantityInput.value = currentValue + 1;
    });
});
