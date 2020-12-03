(function () {
    let jquery_version = '3.4.1';
    let site_url = 'https://127.0.0.1:8000/';
    let static_url = site_url + 'static/';
    let min_width = 100;
    let min_height = 100;

    function bookmarklet(msg) {
       let css = jQuery('<link>')
        css.attr({
            rel: 'stylesheet',
            type: 'text/css',
            href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.random() * 99999999999999)
        })
        jQuery('head').append(css)
        let box_html = `<div id="bookmarklet"><a href="#" id="close">&times</a> <h1>Select an Image to bookmark:</h1><div class="images"></div></div>`
        jQuery('body').append(box_html)

        //close event
        jQuery('#bookmarklet #close').click(function () {
            jQuery('#bookmarklet').remove();
        })

        //find images and display them
        jQuery.each(jQuery('img[src$="jpg"]'), function(index, image) {
            if (jQuery(image).width() >= min_width && jQuery(image).height() >= min_height) {
                let image_url = jQuery(image).attr('src')
                jQuery('#bookmarklet .images').append('<a href="#"><img src="'+ image_url +'" </a>');
            }
        })

        jQuery('#bookmarklet .images a').click(function(e) {
            let selected_image = jQuery(this).children('img').attr('src')
            jQuery('#bookmarklet').hide();
            window.open(site_url + 'images/create/?url='
            + encodeURI(selected_image)
            + '&title='
            + encodeURIComponent(jQuery('title').text()),
                '_blank')
        })
    }

    //Check if jquery is loaded
    if (typeof window.jquery != "undefined") {
        bookmarklet()
    }else {
        let conflict = typeof window.$ != "undefined";

        //Create the script and point to Google API
        let script = document.createElement('script')
        script.src = '//ajax.googleapis.com/ajax/libs/jquery/' + jquery_version + '/jquery.min.js';

        //Add script to head for processing
        document.head.appendChild(script)

        //create a way to wait until script is loaded
        let attempts = 15;
        (function () {
            //check again if jquery is undefined
            if (typeof window.jquery != "undefined") {
               if (--attempts > 0) {
                   window.setTimeout(arguments.callee, 250)
               }else {
                   //Too much attempts to load
                   alert('An error occurred while loading jquery')
               }
            }else {
                bookmarklet()
            }
        })()
    }
})()