$(document).ready(function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').click(function () {
    $('ul.my_list li')[0].remove();
  });
  $('div#clear_list').click(function () {
    $('ul.my_list li').remove();
  });
});
