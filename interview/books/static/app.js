  var main = new Vue({
    el: '#main',
    delimiters: ['[[', ']]'],
    data: {
        q:'',
        results:[]
    },
    computed:{

    },
    methods:{
        doSearch:function(){
            var self = this;
            let q_encoded = encodeURIComponent(this.q);
            axios.get('http://openlibrary.org/search.json?q='+q_encoded)
              .then(function (response) {
                self.results = [];
                console.log(response);
                if (response.status == 200){
                    let temp_results = response.data.docs;
                    for(let i = 0; i < temp_results.length; i++){
                        let authors = temp_results[i].author_name;
                        let isbn = (temp_results[i].isbn.length>0)?temp_results[i].isbn[0]:false;
                        let author = (authors.length>0)?authors[0]:'-';
                        temp_results[i]['computed_author'] = author;
                        temp_results[i]['computed_isbn'] = isbn;
                        temp_results[i]['computed_cover'] = 'http://covers.openlibrary.org/b/isbn/'+isbn+'-M.jpg';
                        if (isbn){
                            self.results.push(temp_results[i]);
                        }
                    }
                }else{
                    console.log('error!!!');
                }
              })
              .catch(function (error) {
                console.log(error);
              });
        }
    }
  });