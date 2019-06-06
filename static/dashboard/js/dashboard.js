$(function () {

  'use strict';

  (function () {

    let logout = document.querySelector('.mynav .logout');
    let count_one = document.querySelector('.count-one');
    let count_two = document.querySelector('.count-two');
    let drop_bar = document.querySelector('.drop-bar');
    let drop__bar = document.querySelector('#drop_bar');
    let drop__aside = document.querySelector('.drop_aside');


    var aside = $('.side-nav'),

      showAsideBtn = $('.show-side-btn'),

      contents = $('#contents');

    showAsideBtn.on("click", function () {

      $("#" + $(this).data('show')).toggleClass('show-side-nav');

      contents.toggleClass('margin');

    });

    if ($(window).width() <= 767) {

      aside.addClass('show-side-nav');
      logout.style.display = 'none';
      drop_bar.style.display = 'block';

      count_one.style.display = 'none';
      count_two.style.display = 'block';
    }
    $(window).on('resize', function () {

      if ($(window).width() > 767) {

        aside.removeClass('show-side-nav');
        contents.removeClass('margin');
        logout.style.display = 'block';
        drop_bar.style.display = 'none';
        drop__aside.style.display = 'none';

        count_two.style.display = 'none';
        count_one.style.display = 'block';

      } else {
        aside.addClass('show-side-nav');
        contents.addClass('margin');
        logout.style.display = 'none';
        drop_bar.style.display = 'block';

        count_two.style.display = 'block';
        count_one.style.display = 'none';
      }

    });

    // dropdown menu in the side nav
    var slideNavDropdown = $('.side-nav-dropdown');

    $('.side-nav .categories li').on('click', function () {

      $(this).toggleClass('opend').siblings().removeClass('opend');

      if ($(this).hasClass('opend')) {

        $(this).find('.side-nav-dropdown').slideToggle('fast');

        $(this).siblings().find('.side-nav-dropdown').slideUp('fast');

      } else {

        $(this).find('.side-nav-dropdown').slideUp('fast');
      }

    });

    // dropdown menu on resizing
    var resizeSideNav = $('.resize-nav-dropdown');

    $('.drop_aside .categories li').on('click', function () {

      $(this).toggleClass('opend').siblings().removeClass('opend');

      if ($(this).hasClass('opend')) {

        $(this).find('.resize-nav-dropdown').slideToggle('fast');

        $(this).siblings().find('.resize-nav-dropdown').slideUp('fast');

      } else {

        $(this).find('.resize-nav-dropdown').slideUp('fast');
      }

    });

    // toggle the display of the drop on window resize
    drop__bar.addEventListener('click', e => {
      if (drop__aside.style.display == 'block') {
        drop__aside.style.display = 'none';
      } else {
        // drop__aside.style.tra
        drop__aside.style.display = 'block';
      }
    })

  }());

});