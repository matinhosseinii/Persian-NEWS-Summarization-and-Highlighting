function click_agency_button_event(agency){
    // Select all buttons within the .choose-agency-buttons container
    const buttons = document.querySelectorAll('.choose-agency button');

    // Add click event listener to each button
    buttons.forEach(button => {
            // Toggle 'active' class on click
            if (button.parentElement.classList.contains(agency)) {
                button.classList.add('active');
            }
            else{
                button.classList.remove('active');
            }
    });
}

function select_agency(agency) {
    // Show loading indicator
    click_agency_button_event(agency);
    $('#loading').show();
    $('.choose-news').hide();
    $('.news-original-article-container').hide();
    $('.news-highlighted-article-container').hide();
    $('.news-summary-article-container').hide();
    // Make AJAX request
    $.ajax({
        type: 'GET',
        url: '/get_titles/',  // URL to your process_request view
        data: {'agency': agency},
        success: function(response) {
            // Hide loading indicator
            $('#loading').hide();
            $('.choose-news').show();

            // Populate dropdown menu with headings
            var headings = response.headings; // Assuming headings is passed in response
            var dropdownMenu = document.getElementById('dropdownMenu');

            // Clear existing items
            dropdownMenu.innerHTML = '';

            // Add new items
            headings.forEach(function(headings) {
                var li = document.createElement('li');
                var a = document.createElement('a');
                a.setAttribute('class', 'dropdown-item');
                a.setAttribute('href', '#');
                a.textContent = headings;
                a.onclick = function(){
                    get_article_by_title(headings);
                }
                li.appendChild(a);
                dropdownMenu.appendChild(li);
            });

        },
        error: function(xhr, status, error) {
            // Handle error
            $('#loading').hide();
            $('#error').html('<p style="color:red;">'+ error +'!</p>').show();

            console.error('Error:', status, error);
        }
    });
}

function get_article_by_title(title) {
    // Show loading indicator
    $('#loading').show();
    $('.news-original-article-container').hide();
    $('.news-highlighted-article-container').hide();
    $('.news-summary-article-container').hide();
    // Make AJAX request
    $.ajax({
        type: 'GET',
        url: '/get_article_using_title/',  // URL to your process_request view
        data: {'title': title},
        success: function(response) {
            // Hide loading indicator
            $('#loading').hide();
            $('.news-original-article-container').show();

            // Populate dropdown menu with headings
            var article = response.article;
            var show_article = document.getElementById('original-article');

            // Clear existing items
            show_article.innerHTML = '';

            var p = document.createElement('p');
            p.textContent = article;
            show_article.appendChild(p);

            get_highlighted_text();
            
        },
        error: function(xhr, status, error) {
            // Handle error
            $('#loading').hide();
            $('#error').html('<p style="color:red;">'+ error +'!</p>').show();

            console.error('Error:', status, error);
        }
    });
}

function get_article_by_url(url) {
    // Show loading indicator
    $('#loading').show();
    $('.news-original-article-container').hide();
    $('.news-highlighted-article-container').hide();
    $('.news-summary-article-container').hide();
    // Make AJAX request
    $.ajax({
        type: 'GET',
        url: '/get_article_using_url/',  // URL to your process_request view
        data: {'url': url},
        success: function(response) {
            // Hide loading indicator
            $('#loading').hide();
            $('.news-original-article-container').show();

            // Populate dropdown menu with headings
            var article = response.article;
            var show_article = document.getElementById('original-article');

            // Clear existing items
            show_article.innerHTML = '';

            var p = document.createElement('p');
            p.textContent = article;
            show_article.appendChild(p);

            get_highlighted_text();

        },
        error: function(xhr, status, error) {
            // Handle error
            $('#loading').hide();
            $('#error').html('<p style="color:red;">'+ error +'!</p>').show();

            console.error('Error:', status, error);
        }
    });
}

function get_highlighted_text() {
    // Show loading indicator
    $('#loading').show();

    // Make AJAX request
    $.ajax({
        type: 'GET',
        url: '/get_extractive/',  // URL to your process_request view
        data: {},
        success: function(response) {
            // Hide loading indicator
            $('#loading').hide();
            $('.news-highlighted-article-container').show();

            var frequency_based = response.frequency_based;
            var luhn = response.luhn
            var textrank = response.textrank

            var show_freqbased = document.getElementById('frequency-based-article');
            var show_luhn = document.getElementById('luhn-article');
            var show_textrank = document.getElementById('text-rank-article');

            show_freqbased.innerHTML = frequency_based;
            show_luhn.innerHTML = luhn;
            show_textrank.innerHTML = textrank;
            
            get_summary_text();

        },
        error: function(xhr, status, error) {
            // Handle error
            $('#loading').hide();
            $('#error').html('<p style="color:red;">'+ error +'!</p>').show();

            console.error('Error:', status, error);
        }
    });
}

function get_summary_text(){
    // Show loading indicator
    $('#loading').show();

    // Make AJAX request
    $.ajax({
        type: 'GET',
        url: '/get_abstractive/',  // URL to your process_request view
        data: {},
        success: function(response) {
            // Hide loading indicator
            $('#loading').hide();
            $('.news-summary-article-container').show();

            var p_b2b = response.p_b2b;
            var f_b2b = response.f_b2b;
            var p_mt5 = response.p_mt5;
            var f_mt5 = response.f_mt5;

            var show_p_b2b = document.getElementById('p-b2b-article');
            var show_f_b2b = document.getElementById('f-b2b-article');
            var show_p_mt5 = document.getElementById('p-mt5-article');
            var show_f_mt5 = document.getElementById('f-mt5-article');


            show_p_b2b.innerHTML = p_b2b;
            show_f_b2b.innerHTML = f_b2b;
            show_p_mt5.innerHTML = p_mt5;
            show_f_mt5.innerHTML = f_mt5;

        },
        error: function(xhr, status, error) {
            // Handle error
            $('#loading').hide();
            $('#error').html('<p style="color:red;">'+ error +'!</p>').show();

            console.error('Error:', status, error);
        }
    });
}

function showArticle(articleId) {
    var mode_element = document.getElementById(articleId.replace('-article', ''));
    mode = mode_element.name
    if (mode == 'extractive'){
        var articles = document.querySelectorAll('.extractive-articles');
    }
    else if (mode == 'abstractive'){
        var articles = document.querySelectorAll('.abstractive-articles');
    }
    // Hide all articles

    articles.forEach(function(article) {
        if(article.id == articleId){
            article.style.display = 'block';
        }
        else{
            article.style.display = 'none';
        }
    });
}
