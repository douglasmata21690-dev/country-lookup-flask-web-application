const search = document.getElementById("search");
const resultsDropdown = document.getElementById("results-dropdown");
const countryMenu = document.getElementById("country-menu");

countryMenu.style.display = "none";

search.addEventListener("input", async function () {
    const userInput = search.value.trim();

    if (userInput.length < 1) {
        resultsDropdown.innerHTML = "";
        search.classList.remove("search-open");
        countryMenu.style.display = "none";
        return; 
    }

    const response = await fetch(
        `/menu/countries?country=${encodeURIComponent(userInput)}`
    );

    const countries = await response.json();
    resultsDropdown.innerHTML = "";

    countries.slice(0, 6).forEach(function(country) {

        const li = document.createElement("li");
        const link = document.createElement("a");
        link.textContent = country.names.common;
        link.href =
            `/country?country=${encodeURIComponent(country.names.common)}`;
            
        li.appendChild(link);
        resultsDropdown.appendChild(li);

    });

    if (resultsDropdown.children.length > 0) {
        countryMenu.style.display = "block";
        search.classList.add("search-open");
    } else {
        countryMenu.style.display = "none";
        search.classList.remove("search-open");
    }
});