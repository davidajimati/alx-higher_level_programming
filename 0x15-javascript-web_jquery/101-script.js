document.addEventListener("DOMContentLoaded", function () {
  const add = document.querySelector("#add_item");
  const remove = document.querySelector("#remove_item");
  const clear = document.querySelector("#clear_list");
  const list = document.querySelector(".my_list");

  add.onclick = () => {
    const item = document.createElement("li");
    item.textContent = "Item";
    list.appendChild(item)
  }

  remove.onclick = () => {
    const lastItem = list.lastElementChild;
    if (lastItem) {
      lastItem.remove();
    }
  }

  clear.onclick = () => {
    while (list.firstElementChild) {
      list.firstElementChild.remove();
    }
  }
})
