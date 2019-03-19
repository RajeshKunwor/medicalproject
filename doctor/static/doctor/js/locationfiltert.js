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