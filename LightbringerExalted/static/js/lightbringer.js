$(function(){
    $('body').on('click', '.btn-add', function(){
        var $selector = $($(this).attr('rel'));
        var model = $selector.attr('name'); // field name
        modelModal.show(model, $selector);
    })

    $('[data-toggle-controller]').each(function(){
        var controller = '[name=' + $(this).attr('data-toggle-controller') + ']'
        var hide_target = $(this).parents('.form-group')
        if (hide_target.length == 0){  //Sometimes it's not in a form group
            hide_target = $(this)
        }
        var disabled_value = $(this).attr('data-disabled-value')
        if (typeof disabled_value !== 'undefined'){
            hide_target.hide()
        }
        var required_value = $(this).attr('data-required-value')

        $('body').on('change', controller, function(){
            if($(this).val() == disabled_value){
                hide_target.hide()
            }else{
                if (typeof required_value !== 'undefined'){ //required value is specified
                    if($(this).val() == required_value || $(this).val() == ''){
                        hide_target.show()
                    }else{
                        console.log("Hiding", hide_target)
                        hide_target.hide()
                    }
                }else{
                    hide_target.show()
                }
            }
        })
    })

    $('.collapse').collapse()
})

var modelModal = {

    ajax_submit: function($form, url, success_callback, fail_callback){
        return $.post(url, $form.serialize(), function(data, status, xhr){
            if(typeof(data) == 'object') {
                if (data['status']=='success') { //redundant for now
                    success_callback(data)
                }
            } else {//html dataType  == failure probably validation errors
                fail_callback(data)
            }
        });
    },

    ajax_success: function(modal, selectInput){
        return function(data) {
            console.log('ajax_success', modal, selectInput, data)
            selectInput.find('option').removeAttr('selected');
            selectInput.append($('<option value="'+data['pk']+'" selected>'+data['title'] + '</option>'));// update original select input
            modal.modal('hide');// close modal
        }
    },

    validation_error: function(modal){
        return function(data) {
            console.log('validation_error', modal, data)
            var $form = $(data).find('form');
            $form.find('button[type=submit]').remove();
            modal.find('.modal-body').html($form);
        }
    },

    show: function(model, selectInput) {
        var self = this;
        var modal = this.template.clone();
        modal.attr('id', model+'_modal');
        var url = selectInput.attr('data-new-item-url');
        $.get(url, function(newForm){
            var $newForm = $($.parseHTML(newForm));

            modal.find('.modal-title').html($newForm.find('h1:not(.filename)').html());
            var $form = $newForm.find('form');
            $form.find('button[type=submit]').remove();
            modal.find('.modal-body').html($form);
            $('body').append(modal);
            modal.find('.modal-footer .btn-primary').on('click', function() {
                self.ajax_submit($form, url, self.ajax_success(modal, selectInput), self.validation_error(modal));
            });

            modal.modal('show');
        })

        },
    template: $('<div class="modal fade">\
                  <div class="modal-dialog">\
                    <div class="modal-content">\
                      <div class="modal-header">\
                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\
                        <h4 class="modal-title">Modal title</h4>\
                      </div>\
                      <div class="modal-body">\
                      </div>\
                      <div class="modal-footer">\
                        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\
                        <button type="button" class="btn btn-primary">Save changes</button>\
                      </div>\
                    </div>\
                  </div>\
                </div>')
}