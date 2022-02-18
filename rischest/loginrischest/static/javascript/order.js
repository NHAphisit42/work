// หน้าที่ใช้รับข้อมูล Address

$(document).ready(function () {
    $("#mylog").submit(function (e) {
      e.preventDefault();

      var name = $(".name").val();
      $("#name").html(name);
      $('input[name="name"]').val(name);
  
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
  
      var post_code = $(".post_code").val();
      $("#post_code").html(post_code);
      $('input[name="post_code"]').val(post_code);
  
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
    $("#id001").hide();
    $('#mylog input[name="name"]').val("");
    $('#mylog input[name="phone"]').val("");
    $('#mylog input[name="address"]').val("");
    $('#mylog input[name="zone"]').val("");
    $('#mylog input[name="district"]').val("");
    $('#mylog input[name="province"]').val("");
    $('#mylog input[name="district"]').val("");
    $('#mylog input[name="post_code"]').val("");
    $('#mylog input[class="name"]').val("");
    $('#mylog input[class="phone"]').val("");
    $('#mylog input[class="address"]').val("");
    $('#mylog input[class="zone"]').val("");
    $('#mylog input[class="district"]').val("");
    $('#mylog input[class="province"]').val("");
    $('#mylog input[class="district"]').val("");
    $('#mylog input[class="post_code"]').val("");
  }
  