 $("#id_citizenship_number").change(function () {
      var citizenship =$(this).val();
      var form = $(this).closest("form");
      $.ajax({
        url: form.attr("data-validate-citizenship-url"),
        data: {
            'citizenship':citizenship
        },
        dataType: 'json',
        success: function (data) {
          if (data.is_taken) {
            alert(data.error_message);
          }
        }
      });

    });