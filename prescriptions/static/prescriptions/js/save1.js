$("#switch1").click(function(){
                             var url = $("#prescriptionForm").attr("action");
                            if ($(this).is(":checked")){
                                $.ajax({
                                            url: url,
                                            data:{
                                                'value':'true'
                                            },

                                });
                            }
                            else{
                                 $.ajax({

                                            url: url,
                                            data:{
                                                'value':'false'
                                            },

                                });
                            }
                        });