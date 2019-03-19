$("#id_prescription").change(function () {
                          var url = $("#billForm").attr("load-service-url");  // get the url of the `load_districts` view

                          var prescriptionId = $(this).val();  // get the selected province ID from the HTML input


                          $.ajax({                       // initialize an AJAX request
                            url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
                            data: {
                              'prescription': prescriptionId       // add the country id to the GET parameters
                            },
                            success: function(data) {   // `data` is the return of the `load_districts` view function
                              //$("#id_service").html(data);   replace the contents of the district input with the data that came from the server
                            }
                          });

                        });