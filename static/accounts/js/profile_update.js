function image() {
    let input = document.querySelector('#id_image')
    let div_img = document.querySelector('.img img')

    input.addEventListener('change', e => {
        // console.log(e)
        // console.log(e.srcElement.value)
        div_img.setAttribute("src", e.srcElement.value)
    })
}

// image();

{
    /* <img id="uploadPreview" style="width: 100px; height: 100px;" />
    <input id="uploadImage" type="file" name="myPhoto" onchange="PreviewImage();" />    */
}

// function PreviewImage() {
//     var oFReader = new FileReader();
//     oFReader.readAsDataURL(document.getElementById("uploadImage").files[0]);

//     oFReader.onload = function (oFREvent) {
//         document.getElementById("uploadPreview").src = oFREvent.target.result;
//     };
// };