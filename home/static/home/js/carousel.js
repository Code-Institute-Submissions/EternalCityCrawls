
    /** 
     *  code for carousel adapted from this link here:  https://azmind.com/bootstrap-carousel-multiple-items 
     *  check number of items and connect the next one
     * @param {object} carousel on which implement the method 
     * @param {string} string to compose the item to attach when sliding
     */
    function slideCustom(carousel, suffix) {

        let $e = $(carousel.relatedTarget);
        let idx = $e.index();
        let itemsPerSlide = 5;
        let totalItems = $('.item-'.concat(suffix)).length;
        
        if (idx >= totalItems - (itemsPerSlide - 1)) {
            let it = itemsPerSlide - (totalItems - idx);
            for (let i = 0; i < it; i++) {
                if (carousel.direction == "left") {
                    $('.item-'.concat(suffix)).eq(i).appendTo('.carousel-inner-'.concat(suffix));
                } else {
                    $('.item-'.concat(suffix)).eq(0).appendTo('.carousel-inner-'.concat(suffix));
                }
            }
        }
    };


    $(document).ready(function () {


        $('#carousel-hot').on('slide.bs.carousel', function (e) {
            slideCustom(e, 'hot')
        });



    });