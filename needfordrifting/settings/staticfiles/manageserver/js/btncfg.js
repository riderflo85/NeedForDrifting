let btnCfg = $("#editCfg");
let btnCarList = $("#editCarList");
let divCfg = $("#divEditCfg");
let divCarList = $("#divEditCarList");

btnCfg.click(function () {
    if (divCfg.data('display') === 'hidden') {
        divCfg.slideDown("slow", function() {
            divCfg.data('display', 'show');
        });
    } else if (divCfg.data('display') === 'show') {
        divCfg.slideUp("slow", function() {
            divCfg.data('display', 'hidden');
        });
    }
});

btnCarList.click(function () {
    if (divCarList.data('display') === 'hidden') {
        divCarList.slideDown("slow", function() {
            divCarList.data('display', 'show');
        });
    } else if (divCarList.data('display') === 'show') {
        divCarList.slideUp("slow", function() {
            divCarList.data('display', 'hidden');
        });
    }
});