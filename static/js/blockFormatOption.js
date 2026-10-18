document.addEventListener('DOMContentLoaded', () => {
  const placeSelect = document.querySelector('#place_format_input'); // place
  const formatSelect = document.querySelector('#format_format_input'); // format

  const placeOptions = placeSelect.querySelectorAll('.format-select__option');
  const formatOptions = formatSelect.querySelectorAll('.format-select__option');
  const formatLabelSpan = formatSelect.querySelector('.format-select__trigger span[data-label]');

  // Находим нужные опции по data-value
  const inklusionOption = Array.from(placeOptions).find(o => o.getAttribute('data-value') === 'inklusion');
  const zaochnoOption = Array.from(formatOptions).find(o => o.getAttribute('data-value') === 'onn'); // у тебя data-value="onn" для заочно
  const ochnoOption = Array.from(formatOptions).find(o => o.getAttribute('data-value') === 'off'); // очно

  if (!inklusionOption || !zaochnoOption || !ochnoOption) {
    console.warn('Не найдены нужные опции — проверь data-value в HTML.');
    return;
  }

  inklusionOption.addEventListener('click', () => {
    // 1. Сначала сбрасываем выделение у всех в format
    formatOptions.forEach(opt => opt.setAttribute('aria-selected', 'false'));

    // 2. Выбираем заочно
    zaochnoOption.setAttribute('aria-selected', 'true');
    if (formatLabelSpan) {
      formatLabelSpan.textContent = zaochnoOption.textContent.trim();
    }

    // 3. Блокируем очно: убираем возможность кликнуть и визуально делаем неактивным
    ochnoOption.style.pointerEvents = 'none';
    ochnoOption.style.opacity = '0.5';
    ochnoOption.classList.add('is-disabled'); // опционально, если есть стили для disabled

    // Если в форме есть скрытый инпут format, который хранит значение — нужно тоже поставить туда 'onn'
    // Скорее всего, Django-поле {{registerForm.format}} — это скрытый input или select.
    // Самый простой способ — найти input внутри formatSelect и поставить value='onn':
    const hiddenInput = formatSelect.querySelector('input[name="format"], select[name="format"]');
    if (hiddenInput) {
      hiddenInput.value = 'onn';
    }
  });

  // Опционально: если пользователь выберет другой пункт в place — можно разблокировать очно обратно
  placeOptions.forEach(opt => {
    if (opt !== inklusionOption) {
      opt.addEventListener('click', () => {
        ochnoOption.style.pointerEvents = 'auto';
        ochnoOption.style.opacity = '1';
        ochnoOption.classList.remove('is-disabled');
        // Тут можно не менять выбор, а просто разрешить выбирать любой вариант.
        // Или, если хочешь, сбрасывать на "Очно" по умолчанию — раскомментируй:
        /*
        formatOptions.forEach(o => o.setAttribute('aria-selected', 'false'));
        ochnoOption.setAttribute('aria-selected', 'true');
        if (formatLabelSpan) formatLabelSpan.textContent = ochnoOption.textContent.trim();
        const hiddenInput = formatSelect.querySelector('input[name="format"], select[name="format"]');
        if (hiddenInput) hiddenInput.value = 'off';
        */
      });
    }
  });
});
