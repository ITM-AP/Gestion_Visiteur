document.addEventListener("DOMContentLoaded", function () {
  function afficherDateHeure() {
    // Obtiens la date actuelle
    var date = new Date();
    
    // Obtient les éléments de l'heure
    var heures = date.getHours();
    var minutes = date.getMinutes();
    
    // Ajoute un zéro en tête si les minutes ou les secondes sont inférieures à 10
    minutes = (minutes < 10 ? "0" : "") + minutes;
    
    // Crée une chaîne représentant l'heure actuelle
    var heureActuelle = heures + ":" + minutes;
    
    // Affiche l'heure dans un élément HTML avec l'ID "horloge"
    document.getElementById("horloge").innerText = heureActuelle;
  }

  // Met à jour l'heure toutes les secondes (1000 millisecondes)
  afficherDateHeure()
  setInterval(afficherDateHeure, 1000);
  

  const rdv = document.querySelectorAll(".rdv");

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
