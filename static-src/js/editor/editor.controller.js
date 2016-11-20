'use strict';

var EditorController = function($scope, logger, menu, moment, Article, Autosave, Editable, $window) {
    var vm = this;
    
    vm.article = {
        article_style: "informational",
        article_type: "regular",
        author: "",
        category: "",
        co_author: "",
        content: "",
        cycle: "",
        cycle_article: "",
        description: "",
        display_date: moment().format("MM/DD/YYYY"),
        feature_image: "",
        header_image: "",
        photo_credit: "",
        published_date: "",
        search_terms: "",
        slug: "",
        status: "",
        tags: "",
        title: ""
    };     // default article data
    vm.goBack = goBack;
    vm.articlePublish = articlePublish;
    vm.articleSave = articleSave;
    vm.articleDelete = articleDelete;
    vm.toggleMenu = toggleMenu;
    vm.setLayout = setLayout;
    vm.getCategories = getCategories;

    activate();

    $scope.$on('setHTML', function() {
        Editable.setHTML(vm.article.content);
    });

    $scope.$on('loadArticle', loadArticle);

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    */
    function activate() {
        logger.log('EditorController activated');
        menu.init();

        /* loop through all of the data and update the view */
        $('[data-ng-model*=vm]').each(function() {
            var $this = $(this),
                name = $this.attr('name'),
                val = $this.attr('value');
            vm.article[name] = val;
        });

        Article.data = vm.article;
        vm.drafts = Autosave.drafts;
    }

    function toggleMenu() {
        if ( $('.hmbrgr').hasClass('expand') ) {
            logger.log('EditorController.toggleMenu()  - close menu');
            menu.close();
        } else {
            logger.log('EditorController.toggleMenu()  - open menu');
            menu.open();
        }
    }

    function loadArticle() {
        logger.log('EditorController.loadArticle()');
        
        vm.article = Article.data;
    }

    function goBack() {
        $window.history.back();
    }

    function articlePublish() {
        Article.publish(vm.article);
    }

    function articleSave() {
        Article.save(vm.article);
    }

    function articleDelete() {
        logger.log('EditorController.articleDelete()');
        $('#deleteModal').modal('show');
        // Article.delete(vm.article);
    }

    function setLayout( layout ) {
        logger.log('EditorController.setLayout()');
        vm.article.article_type = layout;
    }

    function getCategories() {
        logger.log('EditorController.getCategories()');
        var cat = $('#categories').dropdown('get value');
        vm.article.category = cat;
    }
    
    /**
    * @name postArticle
    * @desc Log the user in
    */
    // function postArticle() {
        // var title           = $('#post input[name=title]').val(),
        //     author          = $('#post input[name=author]').val(),
        //     description     = $('#post textarea[name=description]').val(),
        //     content         = $('#editor').editable('getHTML', false, true),
        //     featureIMG      = $('#post input[name=featureIMGurl]').val(),
        //     releaseDate     = $('input[name=release]').val(),
        //     doctype         = $('#post input[name=doctype]:checked').val(),
        //     docstyle        = $('#post input[name=docstyle]:checked').val(),
        //     cycle           = $('#post input[name=feature-cycle]:checked').val(),
        //     headerIMG       = $('#post input[name=headerIMGurl]').val(),
        //     photoCred       = $('#post input[name=photo_cred]').val(),
        //     selected        = [],
        //     options         = [],
        //     release         = "",
        //     coAuthors       = [],
        //     currentCycle    = "";

        // $('#tags_list p').each(function() {
        //     selected.push($(this).text());
        // });
        // var tags = selected.join(", ");

        // $('#category input:checkbox:checked').each(function() {
        //     options.push($(this).val());
        // });
        // var category = options.join(", ");

        // if (title == "") {
        //     var date = moment().format("MM/D/YYYY");
        //     title = "Article "+ date;
        // }

        // if (releaseDate == "") {
        //     release = null;
        // }

        // if (releaseDate != "") {
        //     release = moment(releaseDate).toArray().toString();
        // }

        // if (featureIMG === "") {
        //     if ($('#headerSame').prop("checked")) {
        //         featureIMG = headerIMG || 'same';
        //     }
        //     else {
        //         featureIMG = '';
        //     }
        // }

        // $('#more-authors input:checkbox:checked').each(function() {
        //     coAuthors.push($(this).val());
        // });
        // var ca = coAuthors.join(", ");

        // $.post('/submit', {
        //     title: title,
        //     author: author,
        //     description: description,  
        //     content: content, 
        //     featureIMG: featureIMG,
        //     status: action,
        //     releaseDate: release, 
        //     doctype: doctype,  
        //     docstyle: docstyle,
        //     cycle: cycle,
        //     headerIMG: headerIMG,    
        //     coAuthor: ca,      
        //     tags: tags,
        //     category: category,
        //     photoCred: photoCred
        // }).done(function(message) {
        //     if (message['success']) {
        //         $('#success_msg > .message').empty().append(message['success']);
        //         $('#success_msg').show();
        //         localStorage.clear();
        //         setTimeout('window.location = "/dashboard";', 3500);
        //     }

        //     if (message['error']) {
        //         $('#errorAlert > .message').empty().append(message['error']);
        //         $('#errorAlert').show();
        //     }
        // }).fail(function() {
        //     $('#errorAlert > .message').empty().append('<strong>Error: </strong> An error occured while trying to save your article. Please try again.');
        //     $('#errorAlert').show();
        // });

        // dataservice.postData(data);
    // }
};

module.exports = EditorController;