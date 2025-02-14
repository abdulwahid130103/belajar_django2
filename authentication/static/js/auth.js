$.ajaxSetup({
    headers: {
        'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
    }
});
$(document).ready(function () {

   $("#btn-sign-in").click(function(e){

        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


        var requestData = {
            username: $("#username").val(),
            password: $("#password").val(),
        };

        
        $.ajax({
            url: `{% url 'api:sign_in' %} `,
            type: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            mode: 'same-origin',// Atur tipe konten permintaan sebagai JSON
            data: requestData,
            success: function(response) {
                if(response.status == 200){
                    toastr.success(response.message,"success" );
                    document.location.href = `{% url 'api:siswa-list' %}` 
                }else{
                    toastr.error("Gagal login!","success" );
                    document.location.href = ''
                }
                
            }
        });
   });

});