document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("taskForm");
  const list = document.getElementById("taskList");

  // Add new task
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const response = await fetch("/add/", {
      method: "POST",
      body: formData,
    });
    const data = await response.json();
    if (data.title) {
      const li = document.createElement("li");
      li.dataset.id = data.id;
      li.innerHTML = `<span class="title">${data.title}</span>
                      <button class="toggle">✔</button>
                      <button class="delete">🗑</button>`;
      list.prepend(li);
      form.reset();
    }
  });

  // Toggle & Delete
  list.addEventListener("click", async (e) => {
    const li = e.target.closest("li");
    if (!li) return;
    const id = li.dataset.id;

    if (e.target.classList.contains("toggle")) {
      const res = await fetch(`/toggle/${id}/`);
      const data = await res.json();
      li.classList.toggle("completed", data.completed);
    }

    if (e.target.classList.contains("delete")) {
      await fetch(`/delete/${id}/`);
      li.remove();
    }
  });
});
