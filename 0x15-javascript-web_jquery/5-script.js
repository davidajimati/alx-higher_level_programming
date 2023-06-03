const adder = document.querySelector("#add_item");
const list = document.querySelector(".my_list")

adder.onclick = () => {
  const item = document.createElement('li');
  item.textContent = "New item added"
  list.append(item);
}
