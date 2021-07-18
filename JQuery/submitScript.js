$(function(){

    $("#btn1").click(function () { 
        $(this).attr("value","กรุณารอสักครู...");
    });
    $("#confirm").submit(function(){
        var user = $('#user').val();
        $("#display").html("ขอบคุณ Email = " + user)
    });
    $("#txt").select(function(){
        $("#span").html("เลือกข้อความ");
    });

});