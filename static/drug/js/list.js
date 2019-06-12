window.onload = function () {
    let drugItem = document.querySelectorAll(".drug_item");

    drugItem.forEach(item => {
        item.addEventListener('mouseover', e => {
            // document.querySelector('.drug_item a').style.display = "block";
        })
    })
}

// $(document).ready(function () {
//     let drugItem = $(".drug_item")
//     drugItem.each(item => {
//         item.
//     })
// })