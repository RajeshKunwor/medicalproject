<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>

<script>
    $(document).ready(function(){

        $("#check").click(function(){
            if ($(this).prop("checked")){
                var province = $("#id_p_province").val()
                var municipality = $("#id_p_municipality").val()
                var district = $("#id_p_district").val()
                var ward = $("#id_p_ward_no").val()
                var street = $("#id_p_street").val()

                $("#id_t_province").val(province)
                $("#id_t_district").val(district)
                $("#id_t_municipality").val(municipality)
                $("#id_t_ward_no").val(ward)

                $("#id_t_street").val(street)

            }

            else{
                $("#id_t_province").val('')
                $("#id_t_district").val('')
                $("#id_t_municipality").val('')
                $("#id_t_ward_no").val('')
                $("#id_t_street").val('')
            }
        });
    });
</script>
  <script>
    $("#id_p_province").change(function () {
      var url = $("#patientForm").attr("data-districts-url");  // get the url of the `load_districts` view

      var provinceId = $(this).val();  // get the selected province ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
          'province': provinceId       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_districts` view function
          $("#id_p_district").html(data);  // replace the contents of the district input with the data that came from the server
        }
      });

    });


    //For Municipality

    $("#id_p_district").change(function () {
      var url = $("#patientForm").attr("data-muni-url");  // get the url of the `load_districts` view

      var districtId = $(this).val();  // get the selected province ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
          'district':districtId       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_districts` view function
          $("#id_p_municipality").html(data);  // replace the contents of the district input with the data that came from the server
        }
      });

    });


    //For Ward

    $("#id_p_municipality").change(function () {
      var url = $("#patientForm").attr("data-ward-url");  // get the url of the `load_districts` view

      var muniId = $(this).val();  // get the selected province ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
          'municipality': muniId       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_districts` view function
          $("#id_p_ward_no").html(data);  // replace the contents of the district input with the data that came from the server
        }
      });

    });
  </script>



<!-- for temporary address -->
<script>
    $("#id_t_province").change(function () {
      var url = $("#patientForm").attr("data-districts-url");  // get the url of the `load_districts` view

      var provinceId = $(this).val();  // get the selected province ID from the HTML input

                  $.ajax({                       // initialize an AJAX request
                    url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
                    data: {
                      'province': provinceId       // add the country id to the GET parameters
                    },
                    success: function (data) {   // `data` is the return of the `load_districts` view function
                      $("#id_t_district").html(data);  // replace the contents of the district input with the data that came from the server
                    }
                  });

    });


    //For Municipality

    $("#id_t_district").change(function () {
      var url = $("#patientForm").attr("data-muni-url");  // get the url of the `load_districts` view

      var districtId = $(this).val();  // get the selected province ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
          'district':districtId       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_districts` view function
          $("#id_t_municipality").html(data);  // replace the contents of the district input with the data that came from the server
        }
      });

    });


    //For Ward

    $("#id_t_municipality").change(function () {
      var url = $("#patientForm").attr("data-ward-url");  // get the url of the `load_districts` view

      var muniId = $(this).val();  // get the selected province ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
          'municipality': muniId       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_districts` view function
          $("#id_t_ward_no").html(data);  // replace the contents of the district input with the data that came from the server
        }
      });

    });
  </script>

<!-- for temporary addreess-->
<script>
 $(document).ready(function(){

        $("#check").click(function(){
            if ($(this).prop("checked")){


                  var url = $("#patientForm").attr("data-districts-url");  // get the url of the `load_districts` view

                  var provinceId = $("#id_t_province").val();  // get the selected province ID from the HTML input
                   var district = $("#id_p_district").val();

                              $.ajax({                       // initialize an AJAX request
                                url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
                                data: {
                                  'province': provinceId       // add the country id to the GET parameters
                                },
                                success: function (data) {   // `data` is the return of the `load_districts` view function
                                  $("#id_t_district").html(data);  // replace the contents of the district input with the data that came from the server
                                  $('#id_t_district').val(district);
                                }
                              });



                    var url = $("#patientForm").attr("data-muni-url");  // get the url of the `load_districts` view

                  var districtId = $("#id_p_district").val();  // get the selected province ID from the HTML input
                  var municipality = $("#id_p_municipality").val();

                  $.ajax({                       // initialize an AJAX request
                    url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
                    data: {
                      'district':districtId       // add the country id to the GET parameters
                    },
                    success: function (data) {   // `data` is the return of the `load_districts` view function
                      $("#id_t_municipality").html(data);  // replace the contents of the district input with the data that came from the server
                      $("#id_t_municipality").val(municipality);
                    }
                  });



                  var url = $("#patientForm").attr("data-ward-url");  // get the url of the `load_districts` view

                  var municipalityID = $("#id_p_municipality").val();  // get the selected province ID from the HTML input
                  var ward = $("#id_p_ward_no").val();

                  $.ajax({                       // initialize an AJAX request
                    url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
                    data: {
                      'municipality':municipalityID       // add the country id to the GET parameters
                    },
                    success: function (data) {   // `data` is the return of the `load_districts` view function
                      $("#id_t_ward_no").html(data);  // replace the contents of the district input with the data that came from the server
                      $("#id_t_ward_no").val(ward);
                    }
                  });



            }
         });
 });
</script>