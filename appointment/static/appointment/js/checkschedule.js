$("#id_appointment_schedule").change(function () {
     $("#savebtn").removeAttr("disabled");
                          var appointment =$(this).val();
                          var doctor = $("#id_doctor").val();
                          var patient = $("#patient_id").val();
                          var form = $(this).closest("form");
                          $.ajax({
                            url: form.attr("check-appointment-url"),
                            data: {
                                'appointment':appointment,
                                'doctor':doctor,
                                'patient':patient,
                            },
                            dataType: 'json',
                            success: function (data) {
                              if (data.is_taken) {
                               $("#savebtn").attr("disabled","disabled");
                                alert(data.error_message);
                              }
                            }
                          });

                        });