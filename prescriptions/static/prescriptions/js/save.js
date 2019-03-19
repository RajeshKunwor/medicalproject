$(document).ready(function () {
                         $("#saveandadd").hide();
                          $("#save").show();
                            $("#switch1").click(function () {
                                    if ($(this).is(":checked")) {
                                        $("#save").hide();
                                        $("#saveandadd").show();


                                    } else {
                                        $("#saveandadd").hide();
                                        $("#save").show();
                                    }
                                });
                             });