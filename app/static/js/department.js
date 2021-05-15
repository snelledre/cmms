$(function () {

    $('#basic-datatable').DataTable({
        "responsive": true,
        "lengthMenu": [
            [10, 25, 50, -1],
            [10, 25, 50, "All"]
        ],
        "language": {
            "lengthMenu": "_MENU_ resultaten weergeven",
            "zeroRecords": "Geen resultaten gevonden",
            "info": "_START_ tot _END_ van _TOTAL_ resultaten",
            "infoEmpty": "Geen resultaten om weer te geven",
            "infoFiltered": "(gefilterd uit _MAX_ resultaten)",
            "infoThousands": ".",
            "search": "Zoeken: ",
            "loadingRecords": "Een moment geduld aub - bezig met laden...",
            "paginate": {
                "first": "Eerste",
                "last": "Laatste",
                "next": "<i class='mdi mdi-chevron-right'>",
                "previous": "<i class='mdi mdi-chevron-left'>"
            },
        }, drawCallback: function () {
            $(".dataTables_paginate > .pagination").addClass("pagination-rounded")
        }
    });

});