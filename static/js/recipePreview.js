function titlePreview(title) {
    let previewText = title.value;
    if (previewText.length > 20) {
        previewText = previewText.slice(0, 20) + "...";
    }
    document.getElementById("titlePreview").innerHTML = previewText;
}

function descPreview(description) {
    let previewText = description.value;
    if (previewText.length > 150) {
        previewText = previewText.slice(0, 150) + "...";
    }
    document.getElementById("descPreview").textContent = previewText;
}

const input = document.getElementById('id_image');
const previewPhoto = () => {
    const file = input.files;
    if (file) {
        const fileReader = new FileReader();
        const preview = document.getElementById('imagePreview');
        fileReader.onload = function (event) {
            preview.setAttribute('src', event.target.result);
        }
        fileReader.readAsDataURL(file[0]);
    }
}
input.addEventListener("change", previewPhoto);