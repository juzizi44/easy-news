$(document).ready(function () {

    ClassicEditor
        .create(document.querySelector('#id_content'), {

            licenseKey: '',

            ckfinder:{
                uploadUrl:'/uploads/'

            }


        })
        .then(editor => {
            window.editor = editor;


        })
        .catch(error => {
            console.error('Oops, something went wrong!');
            console.error('Please, report the following error on https://github.com/ckeditor/ckeditor5/issues with the build id and the error stack trace:');
            console.warn('Build id: vhxnhzcek3al-6ocs3mn8uw2f');
            console.error(error);
        });

})

