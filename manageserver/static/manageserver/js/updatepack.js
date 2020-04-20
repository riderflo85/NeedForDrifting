// let csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function updatePack(listServer) {
    for (const server of listServer) {
        let serverId = Number(server.getAttribute('data-id'));
        let btnUpdate = $(`#updatePack${serverId}`);
        let btnConfirm = $(`#confirmUpdate${serverId}`);
        let btnAddSelectCar = $(`#addCar${serverId}`);
        let selectTrack = $(`#selectTrack${serverId}`);
        let allSelectCars = $(`#parentSelectCar${serverId}`);

        btnUpdate.click(function () {$(`#modalPackServ${serverId}`).modal()});

        btnAddSelectCar.click(function () {
            $(`#baseSelect${serverId}`).clone().appendTo(allSelectCars);
        });

        btnConfirm.click(function () {
            let cars = [];
            let track = selectTrack.val();
            for (const selectCar of allSelectCars.children()) {
                cars.push(selectCar.value);
            }
            $.ajax({
                url: '/manage_server/update_pack/',
                type: 'POST',
                dataType: 'json',
                data: {'server': serverId, 'cars': cars.toString(), 'track': track},
                success: function (data) {
                    if (data['updated'] === true) {
                        $(`#notifToastSuccess${serverId}`).removeClass('d-none');
                        $(`#notifToastSuccess${serverId}`).toast('show');
                    } else {
                        $(`#notifToastError${serverId}`).removeClass('d-none');
                        $(`#notifToastError${serverId}`).toast('show');
                    }
                },
                error: function (err) {
                    console.warn(err);
                }
            });
        });
    }
}

updatePack($("#serversAction").children());