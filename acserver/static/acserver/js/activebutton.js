function downloadPack() {
    let csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        url: '/download',
        type: 'POST',
        dataType: 'json',
        data: {'id_server': this.getAttribute('data-server-id')},
        success: function (data) {
            if (data['success'] === true) {
                $("<div class='spinner-border text-info' role='status'><span class='sr-only'>Loading...</span></div>").appendTo('#modalHeaderDl');
                $("<iframe src='https://giphy.com/embed/GD5xkDtFPUpY4' width='480' height='165' rameBorder='0' class='giphy-embed' allowFullScreen></iframe>").appendTo('#modalBodyDl');
                $('#modalSuccessDl').modal();
            }
        },
        error: function (err) {
            console.warn(err);
        }
    });
}

function activeButton(listServCard) {
    for (const server of listServCard) {
        // defined if the button is to be actived or not
        let serverId = Number(server.getAttribute('data-id'));
        let customTrack = false;
        let customCar = false;
        if ($(`#serverTrack${serverId}`).data('addon') === "True") {
            customTrack = true;
        }
        for (const car of $(`.vehicle${serverId}`)) {
            if (car.getAttribute('data-addon') === "True") {
                customCar = true;
            }
        }
        if (customCar == true || customCar == true) {
            let baliseBtn = `<button type='button' class='btn btn-info' id="dlPackServ${serverId}" data-server-id='${serverId}'>Télécharger le pack</button>`;
            $(baliseBtn).appendTo($(server.children[2]));
            document.getElementById(`dlPackServ${serverId}`).addEventListener('click', downloadPack);
        } else {
            let baliseInfo = "<h6><strong class='text-info'>Inclus de base dans le jeu</strong></h5>";
            $(baliseInfo).appendTo($(server.children[2]));
        }
    }
}

activeButton($("#cardServ").children());
