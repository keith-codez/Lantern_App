function toggleMenu() {
    const menu = document.getElementById("mobile-menu");
    
    // Check if the menu is currently hidden
    if (menu.classList.contains("hidden")) {
      menu.classList.remove("hidden"); // Show the menu
      menu.style.height = "0"; // Start from 0 height
      menu.style.transition = "height 0.3s ease-in-out"; // Add transition
      setTimeout(() => {
        menu.style.height = menu.scrollHeight + "px"; // Expand to full height
      }, 10);
    } else {
      menu.style.height = "0"; // Collapse the menu
      menu.style.transition = "height 0.3s ease-in-out"; // Add transition
      setTimeout(() => {
        menu.classList.add("hidden"); // Hide the menu after collapse
      }, 300); // Match the duration of the transition
    }
  };

   // Toggle the menu visibility on mobile
   function toggleMenu() {
    const menu = document.getElementById("mobile-menu");
    menu.classList.toggle("hidden");
  };

  const nextButton = document.getElementById("next");
  const prevButton = document.getElementById("prev");
  const carouselImages = document.querySelector(".carousel-images");
  const totalImages = document.querySelectorAll(".carousel-item").length;
  let currentIndex = 0;

  nextButton.addEventListener("click", () => {
    if (currentIndex < totalImages - 1) {
      currentIndex++;
      updateCarousel();
    }
  });

  prevButton.addEventListener("click", () => {
    if (currentIndex > 0) {
      currentIndex--;
      updateCarousel();
    }
  });

  function updateCarousel() {
    const offset = -currentIndex * 100;
    carouselImages.style.transform = `translateX(${offset}%)`;
  };

  const phoneInput = document.querySelector("#phone");
  const iti = intlTelInput(phoneInput, {
    initialCountry: "auto",
    geoIpLookup: function(callback) {
      fetch("https://ipinfo.io?token=YOUR_TOKEN")
        .then((resp) => resp.json())
        .then((data) => callback(data.country))
        .catch(() => callback("us")); // Default fallback
    },
    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.19/js/utils.js",
  });