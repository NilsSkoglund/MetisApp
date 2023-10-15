function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
document.addEventListener("DOMContentLoaded", function() {

    const csrftoken = getCookie('csrftoken');
    const deleteButtons = document.querySelectorAll(".delete-btn");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function() {
            const patientId = this.getAttribute("data-patient-id");
            fetch(`delete_patient/${patientId}/`, {
                method: 'DELETE',
                headers: {'X-CSRFToken': csrftoken}
            })
            .then(response => response.json())
            .then(data => {
                if(data.status === "success") {
                    // Remove the card for this patient or refresh the page
                    location.reload();
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        })
    })


})