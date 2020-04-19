let btnEdit = $('#btnEdit');
let btnSave = $('#btnSave');
let btnCancel = $('#btnCancel');
let preview = $('#prePreview');
let textArea = $('#editor');
let oldContent;
let check = 1;
let csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function defineConfig(url) {
    let comp1 = 'editcarlist';
    let comp2 = 'editcfg';
    if (url.includes(comp1)) {
        return comp1;
    } else if (url.includes(comp2)) {
        return comp2;
    }
}

function sendConfig(data) {
    let url = document.location.href;
    let idServer = Number(url.substring(url.lastIndexOf('/')+1));
    let configType = defineConfig(url);
    let animSave = $('#saving');
    let animSaveSuccess = $('#savingSuccess');
    let animSaveFailed = $('#savingFailed');

    animSave.fadeIn('slow', function () {
        setTimeout(function () {
        $.ajax({
            url: `/manage_server/${configType}/${idServer}`,
            type: 'POST',
            dataType: 'json',
            data: {'new_config': data},
            success: function (res) {
                if (res['status'] === "updated") {
                    animSave.fadeOut('slow', function () {
                        animSaveSuccess.fadeIn('slow');
                        setTimeout(function () {
                            animSaveSuccess.fadeOut('slow');
                        }, 3000);
                    });
                } else if (res['status'] === "not-updated") {
                    animSave.fadeOut('slow', function () {
                        animSaveFailed.fadeIn('slow');
                        setTimeout(function () {
                            animSaveFailed.fadeOut('slow');
                        }, 3000);
                    });
                }
            },
            errror: function (err) {
                console.warn(err);
            },
        });
        },2000);
    });
    
}

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

    sendConfig(content);

    btnSave.fadeOut('slow');
    btnCancel.fadeOut('slow', function() {
        btnEdit.fadeIn('slow');
    });

    textArea.fadeOut('slow', function() {
        $(codeBalise).appendTo(preview);
        $('#preview').text(content);
        hljs.highlightBlock(document.getElementById('prePreview'));
        check = 1;
        textArea[0].value = content;
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