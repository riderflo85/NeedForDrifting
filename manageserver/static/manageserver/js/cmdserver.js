let csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function runCmd(listServer) {
    for (const server of listServer) {
        let serverId = Number(server.getAttribute('data-id'));
        for (const btn of $(`#groupBtnAction${serverId}`).children()) {
            btn.addEventListener('click', function() {
                let cmd = this.getAttribute('data-cmd');
                let roundStat = $(`#roundStat${serverId}`);
                $.ajax({
                    url: `/manage_server/command/${serverId}/${cmd}`,
                    type: 'GET',
                    success: function (res) {
                        if (res['error'] === false) {
                            roundStat.removeClass('status-running status-stoping status-reboot');
                            if (res['status_cmd'] === "running" || res['status_cmd'] === "run") {
                                roundStat.addClass('status-running');
                            } else if (res['status_cmd'] === "restarting") {
                                roundStat.addClass('status-reboot');
                                setTimeout(function () {
                                    roundStat.removeClass('status-reboot');
                                    roundStat.addClass('status-running');
                                },2000);
                            } else if (res['status_cmd'] === "stoping" || res['status_cmd'] === "kill") {
                                roundStat.addClass('status-stoping');
                            }
                        } else {
                            let balise = `<p class='text-warning' id='errorMsg${serverId}'>Une erreur c'est produite</p>`;
                            $(balise).appendTo(`#bodyBtn${serverId}`)
                        }
                    },
                    error: function (err) {
                        console.warn(err);
                    }
                });
            });
        }
    }
    
}

runCmd($("#serversAction").children());