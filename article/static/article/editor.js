$(document).ready(function(){

    /**************************************************************************
    *
    *                                      Gestion ADD REMOVE Formset 
    *
    ***************************************************************************/

    index_form = function( fset, index ){

        $(fset).find('input').each(function() {
            var name = $(this).attr('name').replace( new RegExp('(\_\_prefix\_\_|\\d)') , index );
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id});
        });
        $(fset).find('textarea').each(function() {
            var name = $(this).attr('name').replace( new RegExp('(\_\_prefix\_\_|\\d)') , index );
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id});
        });

        $(fset).find('label').each(function() {
            var newFor = $(this).attr('for').replace( new RegExp('(\_\_prefix\_\_|\\d)') , index );
            var id = 'label_' + newFor;
            $(this).attr({'id':id, 'for':newFor});
        });

    };

    reindex_formset = function( formset_zone ){

        var formset = $(formset_zone).find( '.npart' );
        for( var cpt=0;cpt<formset.length;cpt++ ){
            index_form( formset[cpt], cpt );
        };

        $("#id_form-TOTAL_FORMS").val( parseInt( cpt ) );

    };



    /**************************************************************************
    *
    *                               Gestion Des evenements formulaire
    *
    ***************************************************************************/


    set_event = function(){
            //Bind le(s) bt delete sorte
            $(".bt_rm_sorte").on('click',function(){
                $(this).parents(".npart").remove();
                reindex_formset( "#formsetZone" );
            });
    };

    $("#bt_add_part").on('click',function(){

        //Copy eform
        $( "#epart" ).clone(true).appendTo( $("#formsetZone") );

        reindex_formset( "#formsetZone" );

    });

    set_event();


});
