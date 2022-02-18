// หน้าที่ใช้รับข้อมูล Address

$(document).ready(function () {
  $("#myform").submit(function (e) {
    e.preventDefault();
    $(".name").empty();
    var name = $(".name").val();
    $("#name").html(name);
    $('input[name="name"]').val(name);
    $("name").attr("required", "true");

    var phone = $(".phone").val();
    $("#phone").html(phone);
    $('input[name="phone"]').val(phone);

    var address = $(".address").val();
    $("#address").html(address);
    $('input[name="address"]').val(address);

    var zone = $(".zone").val();
    $("#zone").html(zone);
    $('input[name="zone"]').val(zone);

    var district = $(".district").val();
    $("#district").html(district);
    $('input[name="district"]').val(district);

    var province = $(".province").val();
    $("#province").html(province);
    $('input[name="province"]').val(province);

    var ZIP_code = $(".ZIP_code").val();
    $("#ZIP_code").html(ZIP_code);
    $('input[name="ZIP_code"]').val(ZIP_code);

    // var Diamond = $(".Diamond").val();
    // $("#Diamond").html(Diamond);
    // $('input[name="package"]').val(Diamond);

    // var Silver = $(".Silver").val();
    // $("#Silver").html(Silver);
    // $('input[name="package"]').val(Silver);

    // var Vip = $(".VIP").val();
    // $("#Vip").html(Vip);
    // $('input[name="package"]').val(VIP);

    _reset();
  });
});

function _reset() {
  $("#id01").hide();
  $('#myform input[name="name"]').val("");
  $('#myform input[name="phone"]').val("");
  $('#myform input[name="address"]').val("");
  $('#myform input[name="zone"]').val("");
  $('#myform input[name="district"]').val("");
  $('#myform input[name="province"]').val("");
  $('#myform input[name="district"]').val("");
  $('#myform input[name="ZIP_code"]').val("");
  $('#myform input[class="name"]').val("");
  $('#myform input[class="phone"]').val("");
  $('#myform input[class="address"]').val("");
  $('#myform input[class="zone"]').val("");
  $('#myform input[class="district"]').val("");
  $('#myform input[class="province"]').val("");
  $('#myform input[class="district"]').val("");
  $('#myform input[class="ZIP_code"]').val("");
}
