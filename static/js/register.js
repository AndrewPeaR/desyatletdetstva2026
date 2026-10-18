document.addEventListener("DOMContentLoaded", () => {
  const selectContainer = document.getElementById("format_city_other");
  const otherWrapper = document.getElementById("input_city_other");

  if (!selectContainer || !otherWrapper) {
    console.warn(
      "Не найдены элементы format-select-city или input_city_other — логика не подключится.",
    );
    return;
  }

  const options = selectContainer.querySelectorAll(".format-select__option");
  const triggerLabelSpan = selectContainer.querySelector(
    ".format-select__trigger span[data-label]",
  );
  const otherInput = otherWrapper.querySelector('input[type="text"], textarea');

  options.forEach((option) => {
    option.addEventListener("click", () => {
      // Сбрасываем aria-selected у всех опций внутри этого селекта
      options.forEach((opt) => opt.setAttribute("aria-selected", "false"));
      option.setAttribute("aria-selected", "true");

      const selectedValue = option.getAttribute("data-value") || "";
      const selectedText = option.textContent.trim();

      // Обновляем видимый текст в триггере
      if (triggerLabelSpan) {
        triggerLabelSpan.textContent = selectedText;
      }

      // Показываем/скрываем блок «другой город»
      if (otherInput) {
        if (selectedValue === 'drugoe') {
          // Выбираем «Другое»: показываем, делаем required, очищаем, ставим фокус
          otherWrapper.style.display = 'block';
          otherInput.required = true;
          otherInput.value = '';
          otherInput.focus();
        } else {
          // Любой другой вариант: скрываем, снимаем required, очищаем
          otherWrapper.style.display = 'none';
          otherInput.required = false;
          otherInput.value = '';
        }
      }
    });
  });
});
