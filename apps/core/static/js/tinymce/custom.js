
tinymce.init({
  selector : "textarea:not(.mceNoEditor)",
      setup: function (editor) {
          editor.on('change', function () {
              editor.save();
          });
          },
  height: 300,
  menubar: false,
  plugins: [
    'spellchecker advlist autolink lists link image charmap print preview anchor',
    'visualblocks code fullscreen',
    'insertdatetime media paste code wordcount'
  ],
  toolbar: 'undo redo | formatselect | bold italic backcolor | bullist numlist outdent indent | removeformat',
});

