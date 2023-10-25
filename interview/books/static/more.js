var more_app = new Vue({
    el: '#main',
    data: {},
    methods:{
        addToList:function(){
            const csrf_token = document.querySelector('[name*="csrfmiddlewaretoken"]').value;
            const isbn = document.querySelector('[name*="isbn"]').value;
            axios.post('/addlist', {
                isbn: isbn,
              },{
                headers:{"X-CSRFToken": csrf_token}
              })
              .then(function (response) {
                console.log(response);
                if (response.data.code == 200){
                    console.log('success');
                    alert('Book added to your list')
                }else{
                    alert('Error: ' + response.data.message);
                }
              })
              .catch(function (error) {
                console.log(error);
              });
        }
    }
  });