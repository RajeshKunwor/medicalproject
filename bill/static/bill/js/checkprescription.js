$("#id_prescription").change(function () {
                         $("#savebtn").removeAttr("disabled");
                          $("#generatebtn").removeAttr("disabled");
                          var prescription =$(this).val();

                          var form = $(this).closest("form");
                          $.ajax({
                            url: form.attr("check-prescription-url"),
                            data: {
                                'prescription':prescription,

                            },
                            dataType: 'json',
                            success: function (data) {
                              if (data.is_taken) {
                                 $("#savebtn").attr("disabled","disabled");
                                $("#generatebtn").attr("disabled","disabled");
                                alert(data.error_message);

                              }
                            }
                          });

                        });