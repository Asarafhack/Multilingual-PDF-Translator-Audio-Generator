document.getElementById("pdfInput").addEventListener("change", function() {
    let fileName = this.files[0].name;
    document.querySelector(".upload-box label").textContent = fileName;
});

document.getElementById("convertBtn").addEventListener("click", function() {
    let progressBar = document.querySelector(".progress-bar");
    let progressContainer = document.querySelector(".progress-container");
    let downloadLink = document.getElementById("downloadLink");

    // Reset previous state
    progressContainer.style.display = "block";
    progressBar.style.width = "0%";
    downloadLink.style.display = "none";

    let width = 0;
    let interval = setInterval(() => {
        if (width >= 100) {
            clearInterval(interval);
            downloadLink.style.display = "block";
        } else {
            width += 10;
            progressBar.style.width = width + "%";
        }
    }, 500);
});
