const urlInput = document.getElementById("url");
const clearInput = document.getElementById("clear");

clearInput.addEventListener('click', () => {
    urlInput.value = "";
});
