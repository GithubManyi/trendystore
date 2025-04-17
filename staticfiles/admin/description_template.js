document.addEventListener('DOMContentLoaded', function () {
    const textarea = document.getElementById('id_description');

    if (!textarea) return;

    const template = `Top Notes:\n\nMiddle Notes:\n\nBase Notes:\n`;

    // Insert template only if empty
    if (textarea.value.trim() === '') {
        textarea.value = template;
    }

    // Prevent editing of the section headers
    textarea.addEventListener('keydown', function (e) {
        const labels = ['Top Notes:', 'Middle Notes:', 'Base Notes:'];
        const cursorPos = textarea.selectionStart;

        for (let label of labels) {
            const index = textarea.value.indexOf(label);
            const end = index + label.length;

            if (cursorPos > index && cursorPos <= end) {
                // Block typing inside the label
                e.preventDefault();
                textarea.setSelectionRange(end + 1, end + 1);
                return;
            }

            // Block deletion of label
            if ((e.key === 'Backspace' || e.key === 'Delete') && (
                cursorPos === end || cursorPos === end + 1
            )) {
                e.preventDefault();
                return;
            }
        }
    });
});
