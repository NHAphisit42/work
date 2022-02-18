$(document).ready(function() {
    // This button will increment the value
    $('.qtyplus').click(function(e) {
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var fieldName = $(this).prev();
        // Get its current value
        var currentVal = parseInt(fieldName.val());
        // If is not undefined
        if (!isNaN(currentVal) && currentVal < 5) {
            // Increment
            fieldName.val(currentVal + 1);
        } else {
            // Otherwise put a 0 there
            fieldName.val(100);
        }
    });
    // This button will decrement the value till 0
    $(".qtyminus").click(function(e) {
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var fieldName = $(this).next();
        // Get its current value
        var currentVal = parseInt(fieldName.val());
        // If it isn't undefined or its greater than 0
        if (!isNaN(currentVal) && currentVal > 0) {
            // Decrement one
            fieldName.val(currentVal - 1);
        } else {
            // Otherwise put a 0 there
            fieldName.val(0);
        }
    });
});

// modal address
//-------------------delivery address-------------------------
// Get the modal 
var modal = document.getElementById('id001');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Get the modal 
var modal = document.getElementById('id002');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

$(function() {
    $('input[name="daterange"]').daterangepicker({
        opens: 'left'
    }, function(start, end, label) {
        console.log("A new date selection was made: " + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD'));
    });
});

$(document).ready(function() {
    $('li.active').removeClass('active');
    $('a[href="' + location.pathname + '"]').closest('li').addClass('active');
});