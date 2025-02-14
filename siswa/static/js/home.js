function getSiswaAll(){
    $.ajax({
        url: `{% url 'api:siswa-getall' %}`,
        type: 'GET',
        success: function(response) {

            $('#table-siswa > tbody').empty();
            let alldata = '';
            let no = 0;
            $.each(response,function(index,data){
                no += 1;
                alldata += `
                    <tr>
                        <td>${no}</td>
                        <td>${data.nama}</td>
                        <td>${data.kelas}</td>
                        <td>${data.alamat}</td>
                        <td>${data.nilai}</td>
                        <td>
                            <a class="btn btn-warning tombol-edit" href="javascipt:void(0)" data-id="${data.id}" role="button">Edit</a>
                            <a class="btn btn-danger tombol-hapus" href="javascipt:void(0)" data-id="${data.id}" role="button">Hapus</a
                        </td>
                    </tr>
                `;
            });

            $('#table-siswa > tbody').append(alldata);
        }
    });
}
$(function () {

    $.ajaxSetup({
        headers: {
            'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
        }
    });
    
    getSiswaAll();
    // index table show data    

    $('body').on('click', '.tombol-tambah', function(e) {
        e.preventDefault();

        const currentDate = new Date();
        const formattedDate = currentDate.getFullYear() + '-' +
                              ('0' + (currentDate.getMonth() + 1)).slice(-2) + '-' +
                              ('0' + currentDate.getDate()).slice(-2);

        console.log(formattedDate);
        
        const judul = $(this).data("title");
        $('#modaltambah').modal('show');
        $('.simpan-data').off('click').on('click',function() {        
            $.ajax({
                url: 'siswa-list/create',
                type: 'POST',
                data: {
                    nama : $("#namasiswa").val(),
                    kelas : $("#kelassiswa").val(),
                    alamat : $("#alamatsiswa").val(),
                    nilai : $("#nilaisiswa").val(),
                    created_at : formattedDate,
                    update_at : formattedDate,
                },
                success: function(response) {
                    console.log(response);
                    if(response.status == 200){
                        toastr.success(response.message,"success" );
                    }else{
                        toastr.error(response.message,"error" );
                    }
                    $('#modaltambah').modal('hide');
                    getSiswaAll();
                }
            });
            $('#addForm')[0].reset();
        });
    });

    $('body').on('click', '.tombol-edit', function(e) {
        e.preventDefault();
        const idSiswa = $(this).data("id");
        $('#modaledit').modal('show');
        $.ajax({
            url: 'siswa-list/' + idSiswa + '/edit',
            type: 'GET',
            success: function(response) {
                
                $("#namasiswaedit").val(response.nama);
                $("#kelassiswaedit").val(response.kelas);
                $("#alamatsiswaedit").val(response.alamat);
                $("#nilaisiswaedit").val(response.nilai);

                var idNew = response.id;
                $('.update-data').off('click').on('click',function() {
                    $.ajax({
                        url: 'siswa-list/' + idNew + '/update',
                        type: 'PUT',
                        data: {
                            nama : $("#namasiswaedit").val(),
                            kelas : $("#kelassiswaedit").val(),
                            alamat : $("#alamatsiswaedit").val(),
                            nilai : $("#nilaisiswaedit").val(),
                        },
                        success:function(response){
                            if(response.status == 200){
                                toastr.success(response.message,"success" );
                            }else{
                                toastr.error(response.message,"error" );
                            }
                            $('#modaledit').modal('hide');
                            getSiswaAll();
                        }
                    })
                });
            }
        });
        
    });

    
    $('body').on('click', '.tombol-hapus', function(e) {
        e.preventDefault();
        var id = $(this).data('id');
        Swal.fire({
        title: 'Apakah anda yakin?',
        text: 'ingin menghapus data ini!',  
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Iya, Delete"          
        })
        .then((result) => {
            if (result.isConfirmed) {
                $.ajax({
                    url: 'siswa-list/' + id + '/delete',
                    type: 'DELETE',
                    success:function(response){
                        toastr.success(response.message,"success" );
                        getSiswaAll();
                    }
                });
            } 
        
        });
    });
    

});