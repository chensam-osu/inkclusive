// function deleteNote(noteId) {
//     fetch("/delete-note", {
//       method: "POST",
//       body: JSON.stringify({ noteId: noteId }),
//     }).then((_res) => {
//       window.location.href = "/";
//     });
//   }

function highlightBlue() {
  return $('#blue-word').val();
}

function highlightPink() {
  return $('#pink-word').val();
}

function updateHighlights() {
  $('textarea').highlightWithinTextarea('update');
}

$('textarea').highlightWithinTextarea({
  highlight: [
    {
      highlight: highlightBlue,
      className: 'blue'
    },
    {
      highlight: highlightPink,
      className: 'pink'
    }
  ]
});

$('input').on('input', updateHighlights);