$("#notification_link").click(function () {
    var url = $("#notification").attr("view-url");
     var notification_id = $("#notification_id").val();

      $.ajax({
      url: url,
      data: {
            'notification_id': notification_id,
      },
      success: function (data) {
//         alert(data.msg)
       }
      });

});