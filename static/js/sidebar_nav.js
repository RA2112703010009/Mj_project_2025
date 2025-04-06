document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".nav-link").forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent default link behavior

            const pageUrl = this.getAttribute("href"); // Get page route

            fetch(pageUrl)
                .then(response => {
                    if (!response.ok) {
                        console.error(`HTTP error! status: ${response.status}`);
                        throw new Error(`Could not load ${pageUrl}`);
                    }
                    return response.text();
                })
                .then(html => {
                    document.getElementById("contentContainer").innerHTML = html; // Load content
                    window.history.pushState({}, "", pageUrl); // Update URL properly
                })
                .catch(error => console.error("Error loading page:", error));
        });
    });

    // Handle back navigation
    window.addEventListener("popstate", function () {
        const currentPath = window.location.pathname;
        fetch(currentPath)
            .then(response => response.text())
            .then(html => {
                document.getElementById("contentContainer").innerHTML = html;
            })
            .catch(error => console.error("Error fetching page:", error));
    });
});