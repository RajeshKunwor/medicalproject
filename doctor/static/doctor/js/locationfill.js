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