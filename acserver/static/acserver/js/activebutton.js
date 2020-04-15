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
            let baliseBtn = `<a href='/download/${serverId}' type='button' class='btn btn-info' id="dlPackServ${serverId}" data-server-id='${serverId}' download>Télécharger le pack</a>`;
            $(baliseBtn).appendTo($(server.children[2]));
            document.getElementById(`dlPackServ${serverId}`).addEventListener('click', function() {$('#modalSuccessDl').modal();});
        } else {
            let baliseInfo = "<h6><strong class='text-info'>Inclus de base dans le jeu</strong></h5>";
            $(baliseInfo).appendTo($(server.children[2]));
        }
    }
}

activeButton($("#cardServ").children());
