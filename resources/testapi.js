$(function() {
    $("#cat1").click(function () {                  
        $.ajax({               
            url: "/spring/api/catTwo",            
            method: "GET",            
            dataType: "json",            
            success: function(response) {            
                $("#cat1_area").text("이름:" + response.name + " 나이:" + response.age);         
            },            
            error: function(xhr, status, error) {            
                console.error(error);         
            }            
        });               
    });   

    $("#cat2").click(function () {                  
        $.ajax({               
            url: "/spring/api/catTwo",            
            method: "GET",            
            dataType: "json",            
            success: function(response) {            
                $("#cat2_area").text("이름:" + response.name + " 나이:" + response.age);         
            },            
            error: function(xhr, status, error) {            
                console.error(error);         
            }            
        });               
    });      
});
