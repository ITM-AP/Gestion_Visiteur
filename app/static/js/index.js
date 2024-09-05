
document.addEventListener("DOMContentLoaded", function () {
    const rdv = document.querySelectorAll(".delete-rdv");
  
    rdv.forEach((icon) => {
      icon.addEventListener("click", function () {
        const rdvId = this.getAttribute("rdv-id");
  
        function getCookie(name) {
          let cookieValue = null;
          if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              // Vérifie si le nom du cookie correspond
              if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(
                  cookie.substring(name.length + 1)
                );
                break;
              }
            }
          }
          return cookieValue;
        }
        fetch("delete-rdv/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
          },
          body: JSON.stringify({rdv_id: rdvId})
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.success) {
              location.reload();
            } else {
              console.error(data.error);
            }
          })
          .catch((error) => {
            console.error("Erreur lors de la supression du rendez-vous", error);
          });
      });
    });
  });
  