let btnEdit = $('#btnEdit');
let btnSave = $('#btnSave');
let btnCancel = $('#btnCancel');
let preview = $('#prePreview');
let textArea = $('#editor');
let oldContent;
let check = 1;

btnEdit.click(function() {
    if (check === 1){
        oldContent = textArea.val();
        check = 2;
    }
    btnEdit.fadeOut('slow', function() {
        btnSave.fadeIn('slow');
        btnCancel.fadeIn('slow');
    });
    preview.fadeOut('slow', function() {
        preview.children()[0].remove();
        textArea[0].value = oldContent;
        textArea.fadeIn('slow');
    });
});

btnSave.click(function() {
    let content = textArea.val();
    let codeBalise = `<code class="ini,toml hljs" id="preview"></code>`;

    btnSave.fadeOut('slow');
    btnCancel.fadeOut('slow', function() {
        btnEdit.fadeIn('slow');
    });

    textArea.fadeOut('slow', function() {
        $(codeBalise).appendTo(preview);
        $('#preview').text(content);
        hljs.highlightBlock(document.getElementById('prePreview'));
        preview.fadeIn('slow');
    });
});

btnCancel.click(function() {
    let codeBalise = `<code class="ini,toml hljs" id="preview"></code>`;

    btnSave.fadeOut('slow');
    btnCancel.fadeOut('slow', function() {
        btnEdit.fadeIn('slow');
    });

    textArea.fadeOut('slow', function() {
        $(codeBalise).appendTo(preview);
        $('#preview').text(oldContent);
        hljs.highlightBlock(document.getElementById('prePreview'));
        preview.fadeIn('slow');
    });
});