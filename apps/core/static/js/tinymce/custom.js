
tinymce.init({
  selector: 'textarea',
      setup: function (editor) {
          editor.on('change', function () {
              editor.save();
          });
          },
  height: 360,
  menubar: false,
  plugins: [
    'spellchecker advlist autolink lists link image charmap print preview anchor',
    'searchreplace visualblocks code fullscreen',
    'insertdatetime media table paste code help wordcount'
  ],
  toolbar: 'undo redo | formatselect | bold italic backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat | help',
});

