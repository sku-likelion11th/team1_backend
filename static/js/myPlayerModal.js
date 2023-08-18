const tapeImages = document.querySelectorAll(".modal-on");
const modals = document.querySelectorAll(".modal_content");


const modalOverlay = document.getElementById("modal-overlay");
const closeBtn = modalOverlay.querySelector(".close-area");

const noneModalTapeImages = document.querySelector(".page>img");

if (tapeImages) {
  tapeImages.forEach((image) => {
    image.addEventListener("click", () => {
      const postId = image.getAttribute("post"); // postId를 image 요소의 post 속성으로부터 가져옴
      modals.forEach((modal) => {
        if (modal.getAttribute("post") === postId) {
          modal.style.display = "block";
        } else {
          modal.style.display = "none";
        }
      });
      modalOn();
    });
  });
}



function modalOn() {
  modal.style.display = "flex";
  modalOverlay.style.display = "block";
}

function modalOff() {
  modalOverlay.style.display = "none";
  modal.style.display = "none";
}

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    modalOff();
  }
});

closeArea.addEventListener("click", () => {
  modalOff();
});



