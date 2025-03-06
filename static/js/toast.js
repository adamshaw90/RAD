<script>
    document.addEventListener("DOMContentLoaded", function() {
        let toastElements = document.querySelectorAll('.toast');
        toastElements.forEach(toastEl => {
            let toast = new bootstrap.Toast(toastEl);
            toast.show();
        });
    });
</script>
