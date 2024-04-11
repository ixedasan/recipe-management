const profilePictureInput = document.getElementById('profile-picture');
const previewImage = document.getElementById('preview-image');
const previewPlaceholder = document.querySelector('.img-preview-placeholder');

profilePictureInput.addEventListener('change', () => {
  const file = profilePictureInput.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = () => {
      previewImage.classList.remove('hidden');
      previewImage.src = reader.result;
      previewPlaceholder.classList.add('hidden');
    };
    reader.readAsDataURL(file);
  } else {
    previewImage.classList.add('hidden');
    previewImage.src = '';
    previewPlaceholder.classList.remove('hidden');
  }
});